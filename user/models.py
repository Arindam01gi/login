from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False,blank=False)
    email = models.CharField(max_length=255,null=False,blank = False)
    phone = models.CharField(max_length=15,null= False,blank =False)
    password = models.CharField(max_length=50)
    created_on  = models.DateTimeField(null=False,blank =True)
    updated_on =models.DateTimeField(null=False,blank =True)

    class Meta:
        managed = True
        db_table= 'User'
    
