from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from postgres.models import Post, User
import time
from django.conf import settings
import json
import timeit


class PostView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        n = 100
        dt = timeit.timeit(lambda: Post.objects.count(), number=n)
        resp = {"count": Post.objects.count()}
        resp["time_count"] = dt / n

        dt = timeit.timeit(lambda: Post.objects.filter(title="test").get(), number=n)
        resp["time_single_title"] = dt / n

        dt = timeit.timeit(
            lambda: Post.objects.filter(tags__contains=["test"]).get(), number=n
        )
        resp["time_single_tag"] = dt / n

        ross = User.objects.filter(first_name="Ross", last_name="Lawley").first()
        dt = timeit.timeit(
            lambda: [
                Post(
                    author=ross,
                    title="test2",
                    tags=["test2"],
                ).save()
                for i in range(100)
            ],
            number=n,
        )
        resp["time_insert"] = dt / n

        dt = timeit.timeit(
            lambda: Post.objects.filter(title="test2").delete(), number=1
        )
        resp["time_delete"] = dt / n


        dt = timeit.timeit(lambda: Post.objects.filter(title="test").select_related('author').get(), number=n)
        resp["time_relation"] = dt / n

        return Response(resp)
