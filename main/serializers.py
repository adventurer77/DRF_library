from rest_framework import serializers
from django.contrib.auth.models import User

# from drf_writable_nested import WritableNestedModelSerializer
from .models import Book, Author, Category, Loan, Reservation, Review, UserProfile


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = CategorySerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        # get data for the author and categories
        author_data = validated_data.pop("author")
        categories_data = validated_data.pop("category")

        # create or get an author
        author, created = Author.objects.get_or_create(**author_data)

        # create a book object with binding to the author
        book = Book.objects.create(author=author, **validated_data)

        # add categories to the book
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(**category_data)
            book.category.add(category)

        return book

    def update(self, instance, validated_data):
        # get data for the author and categories
        author_data = validated_data.pop("author", None)
        categories_data = validated_data.pop("category", None)

        # update author information, if available
        if author_data:
            Author.objects.filter(id=instance.author.id).update(**author_data)

        # update the remaining fields of the book
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # update categories if any
        if categories_data:
            
            instance.category.clear()
            # adding new categories
            for category_data in categories_data:
                category, created = Category.objects.get_or_create(**category_data)
                instance.category.add(category)

        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Loan
        fields = ["id", "book", "user", "loan_date", "return_date", "is_returned"]
        read_only_fields = ["loan_date"]

    def create(self, validated_data):
        book = validated_data.pop("book")
        user = validated_data.pop("user")

        loan = Loan.objects.create(book=book, user=user, **validated_data)

        return loan

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Review
        fields = ["id", "book", "user", "rating", "comment", "created_at"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        book = validated_data.pop("book")
        user = validated_data.pop("user")

        review = Review.objects.create(book=book, user=user, **validated_data)

        return review

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class ReservationSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Reservation
        fields = ["id", "book", "user", "reservation_date", "is_active"]
        read_only_fields = ["reservation_date"]

    def create(self, validated_data):
        book = validated_data.pop("book")
        user = validated_data.pop("user")

        reservation = Reservation.objects.create(book=book, user=user, **validated_data)

        return reservation

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
