# from library.views import Book_ViewSet, User_ViewSet, Loan_ViewSet, Loan_List_Book, Loan_List_User
from library.views import Book_ViewSet, User_ViewSet, Loan_ViewSet
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register('livros', Book_ViewSet, basename='livros')
router.register('usuarios', User_ViewSet, basename='usuarios')
router.register('emprestimos', Loan_ViewSet, basename='emprestimos'),
# router.register('emprestimos/livros', Loan_List_Book, basename='emprestimos_livros'),
# router.register('emprestimos/usuarios', Loan_List_User, basename='emprestimos_usuarios'),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
