from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=15)
	content = models.CharField(max_length=500)
	author = models.CharField(max_length=25)
	def __str__(self):
		return self.title

class Voter(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    def __str__(self):
        return self.name


class PolledInfo(models.Model):
    datetimes = models.DateTimeField(auto_now_add=True)
    ratings = models.IntegerField()
    title_id = models.ForeignKey(Article,on_delete=models.CASCADE)
    name_id = models.ForeignKey(Voter,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.datetimes)








