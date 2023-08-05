from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.name}'


class Company(models.Model):
    main_text = models.TextField()
    image = models.ImageField(upload_to='company')
    second_text = models.TextField()

    def __str__(self):
        return f'{self.main_text}'


class Products(models.Model):
    image = models.ImageField(upload_to='chocolate')
    name = models.CharField(max_length=256)
    price = models.PositiveSmallIntegerField(default=0)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name}'


class Testimonials(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='user_image')
    text = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    full_name = models.CharField(max_length=256)
    phone_number = models.PositiveSmallIntegerField(default=0)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.full_name}'
