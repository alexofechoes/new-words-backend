from django.core.management.base import BaseCommand

from new_words.services import word_extractor_process


class Command(BaseCommand):
    help = 'processed texts'

    def handle(self, *args, **options):
        try:
            word_extractor_process()
            print('Success.')
        except Exception as e:
            print('error')
            raise e
