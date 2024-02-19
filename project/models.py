from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""""The Django User model already has the fields defined:
 username, password, email, first_name, last_name, is_activate,
 is_staff, is_superuser and date_joined"""
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    name_project = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    complete = models.BooleanField(default=False)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)