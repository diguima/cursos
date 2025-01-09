from .serializers import Book_Serializer, User_Serializer, Loan_Serializer, Loan_List_Book_Serializer, Loan_List_User_Serializer
from .models import Book, User, Loan
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Book_viewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Book_Serializer

    def get_queryset(self):

        queryset = Book.objects.all()
        title = self.request.query_params.get('title')

        if title:

            queryset = queryset.filter(title=title)

        return queryset

class User_viewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = User_Serializer

    def get_queryset(self):

        queryset = User.objects.all()
        name = self.request.query_params.get('name')

        if name:

            queryset = queryset.filter(name=name)

        return queryset    


class Loan_viewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = Loan_Serializer


class Loan_List_Book(generics.ListAPIView):

    def get_queryset(self):

        queryset = Loan.objects.filter(book_id=self.kwargs['id'])

        return queryset

    serializer_class = Loan_List_Book_Serializer


class Loan_List_User(generics.ListAPIView):

    def get_queryset(self):

        queryset = Loan.objects.filter(user_id=self.kwargs['id'])

        return queryset

    serializer_class = Loan_List_User_Serializer
