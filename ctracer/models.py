from django.db import models

# Create your models here.
class Courses(models.Model):
	term_code = models.IntegerField(default = 0)
	term_Description = models.CharField(max_length = 200)
	crn = models.IntegerField(default = 0)
	subj = models.CharField(max_length = 200)