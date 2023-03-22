from django.core.management.base import BaseCommand
from mongo.models import *
import random
import string
from django.conf import settings
from mongobench.utils import generate_random_text


class Command(BaseCommand):
    help = "Perform some action on mongo objects"

    def handle(self, *args, **options):
        from mongoengine import connect

        connect(host=settings.MONGO_DB_URI)

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
        Post.objects.insert(db_objs, load_bulk=False)

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
        Post.objects.insert(db_objs, load_bulk=False)
