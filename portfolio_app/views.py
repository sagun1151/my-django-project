from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm
from .forms import PortfolioForm

# Create your views here.
def index(request):
   student_active_portfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
   # print('active portfolio query set', student_active_portfolios)
   # portfolios = Portfolio.objects.all()

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'portfolio_app/index.html', 
   {
  'student_active_portfolios': student_active_portfolios,
#   'portfolios': portfolios
   })


def portfolio_list(request):
    portfolios = Portfolio.objects.prefetch_related('project_set').all()

    return render(
        request,
        'portfolio_app/portfolio_list.html',
        {'portfolios': portfolios},
    )

def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'portfolio_app/student_list.html',
        {'students': students},
    )

def portfolio_detail(request, pk):
    portfolio_detail = Portfolio.objects.prefetch_related('project_set').get(pk=pk)
    return render(
        request,
        'portfolio_app/portfolio_detail.html',
        {'portfolio_detail': portfolio_detail},
    )

def project_detail(request, pk):
      project = Project.objects.get(pk=pk)
      return render(
         request,
         'portfolio_app/project_detail.html',
         {'project': project},
      )
def project_create(request, portfolio_pk):
    portfolio = Portfolio.objects.get(pk=portfolio_pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = ProjectForm()

    return render(
        request,
        'portfolio_app/project_form.html',
        {'form' : form, 
         'form_mode' : 'Create',
         'portfolio' : portfolio
        
        },
    )
    
def project_update(request, pk):
    project = Project.objects.get(pk=pk)
    portfolio = project.portfolio #to go back to portfolio detail after update don tknow why it wasent needed for create

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio_detail', pk=portfolio.pk)
    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        'portfolio_app/project_form.html',
        {'form': form, 
         'form_mode' : 'update',
         'portfolio' : portfolio,
         'project' : project
        },
    )
def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    portfolio = project.portfolio

    if request.method == 'POST':
        project.delete()
        return redirect('portfolio_detail', pk=portfolio.pk)

    return render(
        request,
        'portfolio_app/project_confirm_delete.html',
        {'project': project,
         'portfolio' : portfolio
        },
    )

def student_detail(request,pk):
    student = Student.objects.get(pk=pk)

    return render(
        request,
        'portfolio_app/student_detail.html',
        {'student': student},
    )

def portfolio_update(request, pk):
    portfolio = Portfolio.objects.get(pk=pk)
    student= portfolio.student

    if request.method == 'POST':
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = PortfolioForm(instance=portfolio)

    return render(
        request,
        'portfolio_app/portfolio_form.html',
        {'form': form, 
         'form_mode' : 'update',
         'portfolio' : portfolio,
         'student' : student
        },
    )