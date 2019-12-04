from django.db import models
class Sathya(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=20)
    salary=models.DecimalField(decimal_places=2,max_length=10)
    username=models.CharField(max_length=20)
    paasword=models.CharField(max_length=20)



