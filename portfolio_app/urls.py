from django.urls import path
from . import views


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
path('', views.index, name='index'),

#path to portfolio list view
path('portfolios/', views.portfolio_list, name='portfolio_list'),

#path to student list view
path('students/', views.student_list, name='student_list'),

#path to portfolio detail view
path("portfolios/<int:pk>/", views.portfolio_detail, name="portfolio_detail"),

#path to project detail view
path("projects/<int:pk>/", views.project_detail, name="project_detail"),

#path to create project
path('projects/<int:portfolio_pk>/projects/create/', views.project_create, name='project_create'),

#path to update project
path('projects/<int:pk>/update/', views.project_update, name='project_update'),

#path to delete project
path('projects/<int:pk>/delete/', views.project_delete, name='project_delete'),

#path to student detail view
path("students/<int:pk>/", views.student_detail, name="student_detail"),

#path to update portfolio
path('portfolios/<int:pk>/update/', views.portfolio_update, name='portfolio_update'),

]
