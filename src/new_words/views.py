from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from new_words.models import Text, Word

from rest_framework import viewsets
from new_words.serializers import WordsSerializer


class TextAdd(CreateView):
    model = Text
    fields = ['name', 'text']


class WordsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WordsSerializer

    def get_queryset(self):
        user = User.objects.get(id=1)
        # user = self.request.user

        return Word.objects.filter(created_by=user).order_by('-popularity')


def word_familiar(request, id):
    word = Word.objects.get(id=id)
    word.is_familiar = True
    word.save()
    return JsonResponse({'status': 'ok'})
