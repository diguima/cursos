from django.contrib import admin
from .models import Book, User, Loan

class BookAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'gender', 'publicationDate', 'isbn', 'description')
    list_display_links = ('title', 'author')
    list_per_page = 10
    search_fields = ('title', 'author', 'gender')

admin.site.register(Book, BookAdmin)

class UserAdmin(admin.ModelAdmin):    
    
    list_display = ('name', 'email', 'telephone', 'type')
    list_display_links = ('name', 'type')
    list_per_page = 10
    search_fields = ('name', 'type')

admin.site.register(User, UserAdmin)

class LoanAdmin(admin.ModelAdmin):    
    
    list_display = ('book', 'user', 'loanDate', 'returnDate', 'status')
    list_display_links = ('book', 'user')
    list_per_page = 10
    search_fields = ('book', 'user')

admin.site.register(Loan, LoanAdmin)