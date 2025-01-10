from django.db import models


class Book(models.Model):

    title = models.CharField('Título', blank=False, max_length=100)
    author = models.CharField('Autor',blank=False, max_length=100)
    gender = models.CharField('Gênero', blank=False, max_length=50)
    publicationDate = models.DateField('Data de publicação')
    isbn = models.IntegerField('ISBN', blank=False)
    description = models.TextField('Descrição', max_length=300)

    def __str__(self):
        return self.title


class User(models.Model):

    TYPE = (
        ('A', 'Administradora'),
        ('L', 'Leitor'),
    )

    name = models.CharField('Nome', blank=False, max_length=100)
    email = models.CharField('E-mail', blank=False, max_length=100)
    telephone = models.CharField('Telefone', max_length=14)
    type = models.CharField('Tipo', max_length=1, choices=TYPE, blank=False, default='L')

    def __str__(self):
        return self.name

class Loan(models.Model):

    STATUS = (
        ('D', 'Disponível'),
        ('E', 'Emprestado'),
    )

    book = models.ForeignKey(Book, on_delete = models.CASCADE, )
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    loanDate = models.DateField('Data de empréstimo')
    returnDate = models.DateField('Data de devolução')
    status = models.CharField('Status', max_length = 1, choices = STATUS, blank = False, null = False, default = '')
