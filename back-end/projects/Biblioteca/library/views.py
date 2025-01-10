# from .serializers import Book_Serializer, User_Serializer, Loan_Serializer, Loan_List_Book_Serializer, Loan_List_User_Serializer
from .serializers import Book_Serializer, User_Serializer, Loan_Serializer
from .models import Book, User, Loan
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Book_ViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Book_Serializer

    def get_queryset(self):

        queryset = Book.objects.all()
        title = self.request.query_params.get('titulo')
        gender = self.request.query_params.get('genero')

        if title:

            queryset = queryset.filter(title=title)

        if gender:

            queryset = queryset.filter(gender=gender)

        return queryset


class User_ViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = User_Serializer

    def get_queryset(self):

        queryset = User.objects.all()
        name = self.request.query_params.get('nome')

        if name:

            queryset = queryset.filter(name=name)

        return queryset


class Loan_ViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = Loan_Serializer


# class Loan_List_Book(viewsets.ModelViewSet):

#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Loan.objects.all()
#     serializer_class = Loan_List_Book_Serializer


# class Loan_List_User(viewsets.ModelViewSet):

#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Loan.objects.all()
#     serializer_class = Loan_List_User_Serializer
