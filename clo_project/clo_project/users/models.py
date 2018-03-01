from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
"""
#@python_2_unicode_compatible
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


#@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
"""
class BatchException(models.Model):

    class Meta:
        db_table = "batchException"
#        db_tablespace = "web"

    batchExceptionID = models.IntegerField(primary_key=True)
    batchID = models.IntegerField()
    createdBy = models.CharField(max_length=500)
    createdOn= models.DateField()
    modifiedBy = models.CharField(max_length=500)
    modifiedOn= models.DateField()
    fileName = models.CharField(max_length=500)
    exceptionReason = models.CharField(max_length=5000)
"""
class BatchException(models.Model):

    class Meta:
        db_table = "batchException"
#        db_tablespace = "web"

    batchExceptionID = models.IntegerField(primary_key=True)
    batchID = models.IntegerField()
    createdBy = models.CharField(max_length=500)
    createdOn= models.DateField()
    modifiedBy = models.CharField(max_length=500)
    modifiedOn= models.DateField()
    fileName = models.CharField(max_length=500)
    exceptionReason = models.CharField(max_length=5000)

    def __str__(self):
        return self.fileName
"""
