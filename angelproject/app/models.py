from django.db import models

# Create your models here.

class company_name(models.Model):
    company_name=models.CharField(max_length=200)

    def __str__(self):
        return self.company_name
    
class options(models.Model):
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE)    
    ce=models.TextField()
    pe=models.TextField()

    def __str__(self):
        return self.company_name.company_name
    
class expirystrikeprice(models.Model):
    company_name=models.ForeignKey(company_name,on_delete=models.CASCADE)
    ce=models.TextField()
    pe=models.TextField()

    def __str__(self):
        return self.company_name.company_name    
    
    
