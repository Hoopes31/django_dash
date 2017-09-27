# from __future__ import unicode_literals
# from django.db import models

# Create your models here.
# class UserManager(models.Manager):
#     def user_validation(self, data):
#         errors = {}
#         if len(data['first_name']) < 2:
#             errors["first_name"] = 'First name must be longer than two characters.'
#         if len(data['last_name']) < 2:
#             errors['last_name'] = 'Last name must be longer than two characters.'
#         if len(data['email']) < 3:
#             errors['email'] = 'Email must be longer than three characters.'
#         if data['password'] != data['password_confirm']:
#             errors['password'] = 'Passwords must match!'
#         return errors
# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(max_length=255)
#     created_at = models.DateField(auto_now_add=True)
#     updated_at = models.DateField(auto_now=True)
#     # Connect an instance of your User Manager to this model, by overwriting the hidden objects property.
#     objects = UserManager()