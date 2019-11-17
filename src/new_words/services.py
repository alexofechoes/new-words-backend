from collections import Counter
from typing import List, Tuple
import string

import nltk
from django.db import transaction

from nltk.stem import WordNetLemmatizer

from new_words import models

lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')

STOP_WORDS = ["the", "'s", "'ll", "n't", "'re", "..."]


def word_extractor_process():
    texts = models.Text.objects.filter(state='new')
    for text in texts:
        words = get_words(text.text)
        save_words(words, text)


def get_words(text: str) -> List[Tuple[str, int]]:
    processed_words = []
    sentences = nltk.sent_tokenize(text)

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in words:
            if is_word_skip(word):
                continue
            process_words = lemmatizer.lemmatize(word)
            processed_words.append(process_words.lower())

    counter = Counter(processed_words)
    return counter.most_common()


def save_words(words: List[Tuple[str, int]], text: models.Text):
    with transaction.atomic():
        for word, count in words:
            try:
                word_model = models.Word.objects.get(
                    name=word, created_by=text.created_by
                )
                word_model.popularity = word_model.popularity + count
                word_model.save()
            except models.Word.DoesNotExist:
                word_model = models.Word(
                    created_by=text.created_by, name=word, popularity=count
                )
                word_model.save()
        text.processed()
        text.save()


def is_word_skip(word: str) -> bool:
    return len(word) < 2 or word in string.punctuation or word in STOP_WORDS
