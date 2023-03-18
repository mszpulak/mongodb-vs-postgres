from django.core.management.base import BaseCommand
from postgres.models import *
import random
import string
from django.conf import settings
from mongobench.mongobench.utils import generate_random_text


class Command(BaseCommand):
    help = "Perform some action on mongo objects"

    def generate_random_text(self, length):
        letters = string.ascii_letters
        return "".join(random.choice(letters) for _ in range(length))

    def handle(self, *args, **options):
        ross = User(email="ross@example.com", first_name="Ross", last_name="Lawley")
        ross.save()

        n = 250000
        db_objs = [
            Post(
                author=ross,
                title=generate_random_text(30),
                tags=[generate_random_text(10)],
            )
            for i in range(n)
        ]
        Post.objects.bulk_create(db_objs)

        db_obj = Post(author=ross, title="test", tags=["test"])
        db_obj.save()

        db_objs = [
            Post(
                author=ross,
                title=generate_random_text(30),
                tags=[generate_random_text(10)],
            )
            for i in range(n)
        ]
        Post.objects.bulk_create(db_objs)
