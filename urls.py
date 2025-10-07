from django.urls import path
from .views import SignupView,MovieListView,ShowListView,BookSeatView,CancelBookingView

urlpatterns=[
 path('signup/',SignupView.as_view()),
 path('movies/',MovieListView.as_view()),
 path('shows/',ShowListView.as_view()),
 path('shows/<int:pk>/book/',BookSeatView.as_view()),
 path('bookings/<int:pk>/cancel/',CancelBookingView.as_view()),
]
