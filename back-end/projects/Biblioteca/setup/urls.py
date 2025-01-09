from library.views import Book_viewSet, User_viewSet, Loan_viewSet, Loan_List_Book, Loan_List_User
from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

router = routers.DefaultRouter()
router.register('book', Book_viewSet, basename='book')
router.register('user', User_viewSet, basename='user')
router.register('loan', Loan_viewSet, basename='loan')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('book/<int:pk>/enrollments/', Loan_List_User.as_view(), name='loan_book'),
    path('user/<int:pk>/enrollments/', Loan_List_Book.as_view(), name='loan_user'),
]
