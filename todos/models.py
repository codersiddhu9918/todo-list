from django.db import models
from django.contrib.auth.models import User

# class Todo(models.Model):
#     content = models.TextField()
#
# class user_login(models.Model):
#     user = models.CharField(max_length=100)
#     upass= models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.user
#
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

# Create your models here.
