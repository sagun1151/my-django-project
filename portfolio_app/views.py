from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
   student_active_portfolios = Student.objects.select_related('portfolio').all().filter(Portfolio__is_active=True)
   print('active portfolio query set', student_active_portfolios)

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'portfolio_app/index.html', {'student_active_portfolios': student_active_portfolios})