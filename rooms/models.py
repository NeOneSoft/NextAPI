# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


# Define choices for status field
STATUS = (
    ('OPEN', 'OPEN'),
    ('RESERVED', 'RESERVED'),
)


class Room(models.Model):
    room_name = models.CharField(max_length=200)
    reserved_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=8, choices=STATUS)
    minutes_estimated = models.IntegerField(validators=[MaxValueValidator(180), MinValueValidator(1)])
    current_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.room_name


