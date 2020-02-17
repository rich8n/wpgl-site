from django.db import models
from django.utils import timezone

class Golfer(models.Model):
    TEES_CHOICES = (('M', 'Male'),('F','Female'))
    ROLE_CHOICES = (
        ('M', 'Team Member')
        ,('C','Team Captain')
        ,('S','Substitute')
        )

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    suffix = models.CharField(blank=True,max_length=15)
    identifier = models.CharField(max_length=3, unique=True)
    tees = models.CharField(max_length=8,choices=TEES_CHOICES,default='M')
    email = models.EmailField(blank=True,max_length=254)
    phone = models.CharField(blank=True, max_length=15)
    active = models.BooleanField()
    role = models.CharField(max_length=15,choices=ROLE_CHOICES,default='M')
    team = models.ForeignKey('Team',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    legacy_id = models.SmallIntegerField(null=True)

    class Meta:
        ordering = ('lastname','firstname','identifier')

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.suffix} ({self.identifier})'

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    active = models.BooleanField()
    bye_team = models.BooleanField()
    comment = models.CharField(blank=True,max_length=250)

    class Meta:
        ordering = ('bye_team','team_name')

    def __str__(self):
        return self.team_name

# Comment
