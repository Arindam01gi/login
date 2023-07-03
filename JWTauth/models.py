from django.db import models

# Create your models here.

class UserToken(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(null=False,blank=False)
    token = models.CharField(max_length=255)
    updated_on = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = 'user_token'
