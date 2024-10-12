from rest_framework import serializers
from .models import Publisher, Book, Author

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        # Extract nested author and publisher data
        author_data = validated_data.pop('author')
        publisher_data = validated_data.pop('publisher')

        # Create or get the author and publisher objects
        author, _ = Author.objects.get_or_create(**author_data)
        publisher, _ = Publisher.objects.get_or_create(**publisher_data)

        # Create the book with the author and publisher
        book = Book.objects.create(author=author, publisher=publisher, **validated_data)

        return book

    def update(self, instance, validated_data):
        # Extract nested author and publisher data
        author_data = validated_data.pop('author', None)
        publisher_data = validated_data.pop('publisher', None)

        # Update the author if author_data is present
        if author_data:
            author, _ = Author.objects.get_or_create(**author_data)
            instance.author = author

        # Update the publisher if publisher_data is present
        if publisher_data:
            publisher, _ = Publisher.objects.get_or_create(**publisher_data)
            instance.publisher = publisher

        # Update the rest of the book fields
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        return instance
