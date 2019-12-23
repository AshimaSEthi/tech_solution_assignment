from django.db import models

# Create your models here.


class team_structure(models.Model):
	name =  models.CharField(max_length=200,unique = True)
	logoUri = models.CharField(max_length=200,unique = True)
	club_state = models.CharField(max_length = 200)
	created_on = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ['-created_on']
	def __str__(self):
		return self.name


class player_structure(models.Model):
	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length = 200)
	imageUri  = models.CharField(max_length = 200)
	player_jersey_number = models.IntegerField()
	country = models.CharField(max_length=40,default="IN")
	playerHistory = models.TextField(default='')
	# fullName = str(firstName)+' '+str(lastName)
	def __str__(self):
		
		return "%s   %s" % (self.firstName,self.lastName)

class match_team(models.Model):
	first_team = models.CharField(max_length=20)
	second_team = models.CharField(max_length=20)
	match_winner = models.CharField(max_length=20)
	def __str__(self):
		return "%s vs  %s" % (self.first_team,self.second_team)

class points_table(models.Model):
	points = models.IntegerField()
	def __str__(self):
		return self.points