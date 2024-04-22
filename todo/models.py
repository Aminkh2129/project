from django.db import models
from django.contrib.auth.models import User




class Todo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    F_name = models.CharField(blank=True , null=True)
    L_name = models.CharField(blank=True , null=True)
    father_name=models.CharField(blank=True , null=True)
    age=models.IntegerField( null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='qwe')
    class Meta:
        #managed = False
        db_table = 'Amir'

class Amin(models.Model):
    # id = models.BigIntegerField(blank=True, null=True)
    first_name = models.CharField(blank=True, null=True)
    last_name = models.CharField(blank=True, null=True)
    ewq = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amin'    

#class TEST_VIEW(models.Model):
#    id = models.BigAutoField(primary_key=True)
#    fname=models.CharField(blank=True, null=True)
#    lname=models.CharField(blank=True, null=True)
#
#    class Meta:
#        managed=False
#        db_table='ama'


class a(models.Model):
    #id = models.BigAutoField(primary_key=True)
    fname=models.CharField(blank=True, null=True)
    lname=models.CharField(blank=True, null=True)

    class Meta:
        #managed=False
        db_table='a'


class b(models.Model):
    #id = models.BigAutoField(primary_key=True)
    fname=models.CharField(blank=True, null=True)
    lname=models.CharField(blank=True, null=True)

    class Meta:
        #managed=False
        db_table='b'


class d(models.Model):
    #id = models.BigAutoField(primary_key=True)
    fname=models.CharField(blank=True, null=True)
    lname=models.CharField(blank=True, null=True)

    class Meta:
        #managed=False
        db_table='d'
        #app_label='tmp'


class E(models.Model):
    #id = models.BigAutoField(primary_key=True)
    fname=models.CharField(blank=True, null=True)
    lname=models.CharField(blank=True, null=True)

    class Meta:
        #managed=False
        #db_table='E'
        app_label='tmp'

