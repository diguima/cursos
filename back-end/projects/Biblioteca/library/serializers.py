from rest_framework import serializers
from .models import Book, User, Loan


class Book_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Book
        fields = ['title', 'author', 'gender', 'publicationDate', 'isbn', 'description']


class User_Serializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'


class Loan_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Loan
        exclude = []


# class Loan_List_Book_Serializer(serializers.ModelSerializer):

#     class Meta:

#         model = Loan
#         fields = ['book', 'user', 'returnDate']


# class Loan_List_User_Serializer(serializers.ModelSerializer):

#     class Meta:

#         model = Loan
#         fields = ['user', 'book', 'returnDate']
