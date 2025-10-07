import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','movietix.settings')
django.setup()
from django.contrib.auth import get_user_model
from booking.models import Movie,Show
from django.utils import timezone
from datetime import timedelta
User=get_user_model()
u,_=User.objects.get_or_create(username='demo_user',defaults={'email':'demo@example.com'})
u.set_password('demo1234');u.save()
m,_=Movie.objects.get_or_create(title='Demo Movie',duration_minutes=120)
Show.objects.get_or_create(movie=m,screen_name='Main',date_time=timezone.now()+timedelta(days=1),total_seats=30)
print('Seed data created. demo_user/demo1234')
