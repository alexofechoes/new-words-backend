from django.contrib import admin
from new_words import models


@admin.register(models.Text)
class TextAdmin(admin.ModelAdmin):
    model = models.Text
    fields = ('name', 'text', 'created_by')
    readonly_fields = ['state']


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):
    model = models.Word
    readonly_fields = ('name', 'popularity', 'created_by', 'is_familiar')
