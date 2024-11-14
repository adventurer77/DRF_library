# from rest_framework import generics
from rest_framework import viewsets

from main.utils.pagination import BookPagination
from .models import Book, Author, Category, Loan, Reservation, Review, UserProfile
from .serializers import BookSerializer, AuthorSerializer, CategorySerializer, LoanSerializer, ReservationSerializer, ReviewSerializer, UserProfileSerializer

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination

    # def get_queryset(self): # Overriding the method 
    #     pk = self.kwargs.get("pk")

    #     if not pk:
    #         return Book.objects.all()[:1]
        
    #     return Book.objects.filter(pk=pk)

    # @action(methods=["get"], detail=True) # Helps to create a non-standard route  
    # def author(self, request, pk=None):
    #     aut = Author.objects.get(pk=pk)
    #     return Response({"aut": aut.author_name})

    # @action(methods=["get"], detail=True) # /api/v1/books/1/category/
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({"aut": cats.name})


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# class BookViewSet(generics.ListAPIView): # CET
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class AuthorViewSet(generics.ListCreateAPIView): # CET, POST
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

# class AuthorAPIUpdate(generics.UpdateAPIView): # PUT, PATCH
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class AuthorAPIDetailViev(generics.RetrieveUpdateDestroyAPIView): # CRUD
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer