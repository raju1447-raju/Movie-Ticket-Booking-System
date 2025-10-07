from rest_framework import generics,permissions,status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction, IntegrityError
from django.shortcuts import get_object_or_404
from .models import Movie,Show,Booking
from .serializers import SignupSerializer,MovieSerializer,ShowSerializer,BookingSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(generics.CreateAPIView):
    serializer_class=SignupSerializer
    permission_classes=[permissions.AllowAny]

class MovieListView(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class ShowListView(generics.ListAPIView):
    queryset=Show.objects.all()
    serializer_class=ShowSerializer

class BookSeatView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,pk):
        seat=request.data.get('seat_number')
        show=get_object_or_404(Show,pk=pk)
        with transaction.atomic():
            if Booking.objects.filter(show=show,seat_number=seat,status='booked').exists():
                return Response({'detail':'Seat already booked'},status=400)
            if Booking.objects.filter(show=show,status='booked').count()>=show.total_seats:
                return Response({'detail':'Show full'},status=400)
            b=Booking.objects.create(user=request.user,show=show,seat_number=seat)
            return Response(BookingSerializer(b).data,status=201)

class CancelBookingView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self,request,pk):
        b=get_object_or_404(Booking,pk=pk,user=request.user)
        b.status='cancelled';b.save()
        return Response({'detail':'Booking cancelled'},status=200)
