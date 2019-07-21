from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Exam(models.Model):
    name = models.CharField('Name', max_length=100)
    begins = models.DateTimeField('Start of exam')
    ends = models.DateTimeField('End of exam')
    has_expired = models.BooleanField('Expired?')

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name

class ExamVenue(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    req_inv = models.IntegerField('Required invigilators', default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.exam.name + "@" + self.room.name

class InvigilatorResponse(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    can_make = models.BooleanField('I can make that!')
    whoami = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_venue = models.ForeignKey(ExamVenue, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.whoami.first_name + " " + self.whoami.last_name + "/" + self.exam.name
