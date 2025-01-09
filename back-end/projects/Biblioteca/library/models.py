from django.db import models


class Book(models.Model):

    title = models.CharField(blank=False, max_length=100)
    author = models.CharField(blank=False, max_length=100)
    gender = models.CharField(blank=False, max_length=50)
    publicationDate = models.DateField()
    isbn = models.IntegerField(blank=False)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title


class User(models.Model):

    TYPE = (
        ('A', 'Administradora'),
        ('L', 'Leitor'),
    )

    name = models.CharField(blank=False, max_length=100)
    email = models.CharField(blank=False, max_length=100)
    telephone = models.CharField(max_length=14)
    type = models.CharField(max_length=1, choices=TYPE, blank=False, default='L')

    def __str__(self):
        return self.name

class Loan(models.Model):

    STATUS = (
        ('D', 'Disponível'),
        ('E', 'Emprestado'),
        ('R', 'Reservado'),
        ('C', 'Consulta Local'),
    )

    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    loanDate = models.DateField()
    reservationDate = models.DateField()
    returnDate = models.DateField()
    status = models.CharField(max_length = 1, choices = STATUS, blank = False, null = False, default = '')
