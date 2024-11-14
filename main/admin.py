from django.contrib import admin
from main.models import Author, Category, Book, Loan, Reservation, Review, UserProfile

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("author_name", "bio")
    list_editable = ( "bio",)
    search_fields = ("author_name",)
    ordering = ('author_name',)


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "sort")
    list_editable = ("name", "sort")
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_date",
        "isbn",
        "available_copies",
        "is_visible",
    )
    list_editable = ("published_date", "available_copies", "is_visible")
    list_filter = ("category", "author", "is_visible")
    search_fields = ("title", "author__author_name")
    filter_horizontal = ('category',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("membership_date", "is_active_member", "phone_number" )
    search_fields = ("phone_number",)
    list_filter = ("is_active_member", )


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "loan_date", "return_date", "is_returned")
    list_editable = ("return_date", "is_returned")
    search_fields = ("book", "user",)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "rating", "comment", "created_at")
    list_editable = ("rating", "comment")
    search_fields = ("book", "user", "rating")

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "reservation_date", "is_active")
    list_editable = ("is_active",)
    search_fields = ("book", "user")

