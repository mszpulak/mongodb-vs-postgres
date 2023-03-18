from mongoengine import Document, StringField, ListField, LazyReferenceField


# Create your models here.
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(required=True)
    author = LazyReferenceField(User)
    tags = ListField(StringField())
    meta = {"allow_inheritance": True, "indexes": ["title"]}
