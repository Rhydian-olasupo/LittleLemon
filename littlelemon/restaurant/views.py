from django.shortcuts import render
from rest_framework import generics , viewsets
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def home(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = menuSerializer
    
    def get_queryset(self):
        queryset = Menu.objects.filter(id=self.kwargs['pk'])
        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer