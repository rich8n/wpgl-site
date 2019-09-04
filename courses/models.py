from django.db import models
from django.utils import timezone

class Course(models.Model):

    course_name = models.CharField(max_length=50)
    course_short_name = models.CharField(max_length=10)
    legacy_id = models.CharField(blank=True,max_length=15)
    active = models.BooleanField()


    class Meta:
        ordering = ('active','legacy_id')

    def __str__(self):
        return self.course_name

class CourseHoleDetail(models.Model):
    course = models.ForeignKey('Course',on_delete=models.CASCADE)
    hole_num = models.PositiveSmallIntegerField()
    men_par = models.PositiveSmallIntegerField()
    men_hcp = models.PositiveSmallIntegerField()
    ladies_par = models.PositiveSmallIntegerField()
    ladies_hcp = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('course','hole_num')

    def __str__(self):
        return f'{self.course} Hole {self.hole_num}'
