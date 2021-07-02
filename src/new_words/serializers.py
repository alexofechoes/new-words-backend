from rest_framework import serializers

from new_words import models


class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Word
        fields = ['id', 'name', 'popularity', 'is_familiar']
