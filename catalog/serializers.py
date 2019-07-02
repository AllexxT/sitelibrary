from .models import Book, Author
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(source='author.first_name', read_only=True)
    last_name = serializers.CharField(source='author.last_name', read_only=True)
    class Meta:
        model = Book
        fields = ( 'author', 'first_name', 'last_name', 'title', 'summary', 'isbn',)

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')