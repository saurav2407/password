"""
URL configuration for JNCT project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.index,name = 'index'),
    path('login', views.login,name = 'login'),
    path('Apply_now', views.Apply_now,name = 'Apply_now'),
    path('submit', views.submit,name = 'submit'),
    path('pictures', views.pictures,name = 'pictures'),
    path('error', views.error, name='error'),
    path('coaching', views.coaching,name = 'coaching '),
    path('notes', views.notes,name = 'notes '),
    path('download_link', views.download_link,name = 'download_link '),
    path('report', views.report,name = 'report '),
    path('contact', views.contact,name = 'contact '),
    path('fee_cource', views.fee_cource,name = 'fee_cource '),
    path('student_login', views.student_login,name = 'student_login '),
    path('student_information', views.student_information,name = 'student_information '),
    ]
