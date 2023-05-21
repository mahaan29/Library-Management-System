from django.db import models

# Create your models here.

class books(models.Model):
    accession_no = models.CharField(max_length=10)
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=50)
    book_price = models.CharField(max_length=10)

class issue(models.Model):
    customer_name = models.CharField(max_length=50)
    date_issued = models.DateField
    date_returned = models.DateField
    fine = models.CharField(max_length=10)

class customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    re_password = models.CharField(max_length=50)

