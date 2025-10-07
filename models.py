from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Movie(models.Model):
    title=models.CharField(max_length=255)
    duration_minutes=models.PositiveIntegerField()
    def __str__(self): return self.title

class Show(models.Model):
    movie=models.ForeignKey(Movie,related_name='shows',on_delete=models.CASCADE)
    screen_name=models.CharField(max_length=100)
    date_time=models.DateTimeField()
    total_seats=models.PositiveIntegerField()

class Booking(models.Model):
    STATUS_BOOKED='booked'
    STATUS_CANCELLED='cancelled'
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    show=models.ForeignKey(Show,on_delete=models.CASCADE)
    seat_number=models.PositiveIntegerField()
    status=models.CharField(max_length=10,default=STATUS_BOOKED)
    class Meta: unique_together=('show','seat_number')
