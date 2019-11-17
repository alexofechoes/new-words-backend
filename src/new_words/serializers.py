from new_words import models
from rest_framework import serializers


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = ['id', 'name', 'popularity', 'is_familiar']
