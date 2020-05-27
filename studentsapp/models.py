from django.db import models

class student(models.Model):
	companyid = models.CharField(max_length=50, null=False)
    
	num = models.PositivelntegerField
    
	jobname =  models.CharField(max_length=50, null=False)
    
	name =  models.CharField(max_length=50, null=False)
    
	company =  models.CharField(max_length=50,blank=True)

	cash =  models.PositivelntegerField
                             

    
	def __str__(self):
		return self.companyid
