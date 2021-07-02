from django.contrib.auth import get_user_model

import factory
from factory import Faker, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory

faker = FakerFactory.create()


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')

    class Meta:
        model = get_user_model()


class TextFactory(factory.django.Django.ModelFactory):
    """Text factory."""

    created_by = SubFactory(UserFactory)
    name = LazyAttribute(lambda x: faker.name())
    text = LazyAttribute(lambda x: faker.sentence(nb_words=50))

    class Meta:
        model = 'src.new_words.models.Text'


class Word(factory.django.Django.ModelFactory):
    """Word factory."""

    created_by = SubFactory(UserFactory)
    name = LazyAttribute(lambda x: faker.name())

    class Meta:
        model = 'src.new_words.models.Word'
