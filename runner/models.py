from django.db import models
"""""
"dataSet":{
      "name":"chazuo",
      "XXxx":"82",
      "osType":"mac",
      "currSpeed":"86",
      "currSlope":"86",
      "sumTime":"86",
      "sumDistance":"86",
      "sumCalories":"86",
      "currRate":"86"
  
"""
 # Create your models here.
 
class runEvent(models.Model):
    name = models.CharField(max_length=50)
    mac=models.IPAddressField()#IPAddressField()
    osType = models.CharField(max_length=5)
    currSpeed = models.CharField(max_length=5)
    currSlope = models.CharField(max_length=6) 
    sumTime=models.CharField(max_length=10) 
    sumDistance = models.CharField(max_length=10) 
    currRate = models.CharField(max_length=10)
    sportTime=models.TimeField() 
"""
 class runerInfo(models.Model):
    name = models.CharField(max_length=50)
    mac=models.IPAddressField()#IPAddressField()
    osType = models.CharField(max_length=5)
    currSpeed = models.CharField(max_length=5)
    currSlope = models.CharField(max_length=6) 
    sumTime=models.CharField(max_length=10) 
    sumDistance = models.CharField(max_length=10) 
    currRate = models.CharField(max_length=10)
    sportTime=models.TimeField()   
    
"""
