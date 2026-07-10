from django.db import models

# Create your models here.

# class User(models.Model):
#
#
#     name = models.CharField(max_length=32)
#
#     age = models.IntegerField(null=True)
#
#     create_time = models.DateField(auto_now_add=False)


#图书表
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    publish_date = models.DateField(auto_now_add=False)


    publish = models.ForeignKey(to='Publish',on_delete=models.CASCADE)

    authors = models.ManyToManyField(to='Author')

#出版社表
class Publish(models.Model):
    name = models.CharField(max_length=32)
    address = models.CharField(max_length=54)
    email = models.EmailField()


#作者表
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()


#作者详情表
class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=64)

    author = models.OneToOneField(to='Author',on_delete=models.CASCADE)


