from django.contrib.auth.models import User
from django.db import models
from django_fsm import FSMField, transition


class Text(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    text = models.TextField()
    state = FSMField(default='new', protected=True)

    @transition(field=state, source='new', target='done')
    def processed(self):
        """
        Side effects
        """

    @transition(field=state, source='done', target='new')
    def renew(self):
        """
        Side effects
        """

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

    def __str__(self):
        return '{name} ({state})'.format(name=self.name, state=self.state)


class Word(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(unique=True, max_length=100)
    is_familiar = models.BooleanField(default=False)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
