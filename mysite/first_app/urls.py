from django.urls import include, re_path
from first_app import views

urlpatterns=[
re_path(r'^$',views.heading,name='heading'),
]
