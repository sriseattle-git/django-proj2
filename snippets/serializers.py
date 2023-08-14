from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.email") # Use email instead of username which can be NULL
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = (
            "url",
            "id",
            "highlight",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        )

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):  # new
    snippets = serializers.HyperlinkedRelatedField(  # new
        many=True, view_name="snippet-detail", read_only=True
    )

    class Meta:
        model = User
        fields = ("url", "id", "username", "snippets")  # new

'''

"""

# Old SnippetSerializer & UserSerializer that doesn't hyperlink snippets and users based on IDs
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")    

    class Meta:
        model = Snippet
        fields = (
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        )


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ("id", "username", "snippets")

"""