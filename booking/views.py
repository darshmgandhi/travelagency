from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookingForm
from django.views import View
from .models import Booking

# Create your views here.
class BookingView(View):

    def get(self, request):
        return render(request, 'booking.html', {'form': BookingForm()})

    def post(self, request):
        form = BookingForm(request.POST, request.FILES)
        if form.is_valid():
            final_form = form.save(commit = False)
            final_form.additional = ','.join(request.POST.getlist('additional'))
            final_form.save()
            return render(request, 'success.html', {'message': 'Record Successfully Added'})
        return render(request, 'booking.html', {'form': BookingForm()})

class BookingList(ListView):
    template_name = 'records.html'
    model = Booking

class UpdateBooking(View):
    
    def get(self, request, id):
        booking = Booking.objects.get(id = id)
        return render(request, 'update.html', {'form': BookingForm(instance = booking), 'additional_selected': booking.additional})

    def post(self, request, id):
        booking = Booking.objects.get(id = id)
        form = BookingForm(request.POST, request.FILES, instance = booking)
        if form.is_valid():
            final_form = form.save(commit = False)
            final_form.additional = ','.join(request.POST.getlist('additional'))
            final_form.save()
            return render(request, 'success.html', {'message': 'Record Successfully Updated'})
        return render(request, 'booking.html', {'form': BookingForm()})

class DeleteBooking(View):
    
    def get(self, request, id):
        Booking.objects.get(id = id).delete()
        return render(request, 'success.html', {'message': 'Record Successfully Deleted'})

class HomePage(TemplateView):

    template_name = 'home.html'