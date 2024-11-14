from django.db import models
from django.contrib.auth.models import User

from main.utils.isbn import generate_isbn

# Create your models here.


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self) -> str:
        return self.author_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["sort"]

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    category = models.ManyToManyField(Category)
    published_date = models.DateField(null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    available_copies = models.PositiveIntegerField(default=1)
    is_visible = models.BooleanField(default=True)

    class Meta:
        db_table = "book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["time_create"]

    def __str__(self) -> str:
        return (
            f"{self.title} - Created: {self.time_create} | Updated: {self.time_update}"
        )

    def save(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = generate_isbn()
        super().save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    membership_date = models.DateField(auto_now_add=True)
    is_active_member = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=10, blank=True)

    class Meta:
        db_table = "User"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("id",)

    def __str__(self) -> str:
        return self.user.first_name


class Loan(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="loans")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)

    class Meta:
        db_table = "loan"
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        ordering = ("id",)

    # def __str__(self) -> str:
    #     return self.is_returned


class Review(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "review"
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        ordering = ("id",)

    def __str__(self) -> str:
        return f" Rating: {self.rating}, comment: {self.comment}"
    

class Reservation(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "reservation"
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"
        ordering = ("id",)

    # def __str__(self) -> str:
    #     return self.is_active