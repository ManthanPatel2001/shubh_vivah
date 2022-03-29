from email.policy import default
from tokenize import blank_re
from django.db import models
import os
# Create your models here.
class Customer(models.Model):
    email = models.EmailField(max_length=50,unique=True)
    password = models.CharField(max_length=30)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField()
    qualification = models.CharField(max_length=30)
    mother_tounge = models.CharField(max_length=30)
    cast = models.CharField(max_length=30)
    Religene = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    sunshine = models.CharField(default=None,blank=True,max_length=30)
    about = models.TextField(default=None,blank=True,max_length=300)
    height_feet = models.IntegerField(default=None,blank=True,null = True)
    height_inch = models.IntegerField(default=None,blank=True,null = True)
    income = models.IntegerField(default=None,blank=True,null = True)
    
    def imagePath(instance,filename):
        upload_to = 'profileImg/'
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}.{}'.format(instance.pk, ext)
        # return the whole path to the file
        return os.path.join(upload_to, filename)
    image = models.ImageField(blank=True, upload_to=imagePath,default = 'default_profile.png')


    def __str__(self):
        return self.f_name+' '+self.l_name

class Intrest(models.Model):
    person = models.ForeignKey(Customer, related_name='current_user',on_delete= models.CASCADE )
    interested = models.ForeignKey(Customer, related_name='intrested_in',on_delete= models.CASCADE )

class Reject(models.Model):
    person = models.ForeignKey(Customer, related_name="this_user",on_delete= models.CASCADE )
    notinterested = models.ForeignKey(Customer, related_name='not_intrested_in',on_delete= models.CASCADE )

class Matched(models.Model):
    person = models.ForeignKey(Customer, related_name="first_user_mathed",on_delete= models.CASCADE )
    matched_person = models.ForeignKey(Customer, related_name='secound_user_matched',on_delete= models.CASCADE)