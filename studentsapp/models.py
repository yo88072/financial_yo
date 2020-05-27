from django.db import models

class student(models.Model):
	companyid = models.CharField(max_length=20, null=False)
	num = models.CharField(max_length=20, null=False)
	jobname = models.CharField(max_length=20, null=False)
	name = models.CharField(max_length=20, null=False)
	company = models.CharField(max_length=20, null=False)
	cash = models.CharField(max_length=50, blank=True, default='')
	no = models.CharField(max_length=255,blank=True, default='')
    
	def __str__(self):
		return self.companyid
