from django.db import models
from django.urls import reverse

from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import CustomUser


# Create your models here.

class CategoryBooks(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'category_books'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name




class Books(models.Model):
    category = models.ForeignKey(CategoryBooks, on_delete=models.CASCADE)
    book_lang = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='book/', default='media/default_img/default_book_img.jpg')
    page = models.IntegerField()

    created_at = models.DateField(auto_now_add=True)
    uptate_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})

    class Meta:
        db_table = 'books'

    def __str__(self):
        return f"{self.title} {self.title}"


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class BookAuthor(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f"{self.book.title} {self.author.first_name} {self.book.title}"



class Review(models.Model):
    comment = models.CharField(max_length=128)
    star_given = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(1)])
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    class Meta:
        db_table = 'review'


    def __str__(self):
        return f"{self.comment} - {self.star_given} {self.user.username}"




