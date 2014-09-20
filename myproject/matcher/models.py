from django.db import models

# Create your models here.

class Hacker(models.Model):
    DESIGNER = 'DS'
    DEVELOPER = 'DV'
    OTHER = 'OT'
    SKILL_CHOICES = (
        (DESIGNER, 'Designer'),
        (DEVELOPER, 'Developer'),
        (OTHER, 'Other'),
    )
    MALE = 'M'
    FEMALE = 'F'
    OTH = 'O'
    GENDERS = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTH, 'Other')
    )
    full_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=2,
                             choices=GENDERS)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    details = models.TextField()

    skill = models.CharField(max_length=2,
                             choices=SKILL_CHOICES,
                             default=DESIGNER)
    looking_for = models.CharField(max_length=2,
                             choices=SKILL_CHOICES,
                             default=DEVELOPER)

    def __str__(self):
      return self.full_name
