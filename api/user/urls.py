from django.urls import path, include
from django.views.generic.base import TemplateView

from . import views

#app_name = 'user'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),

    #path('accounts/', include('django.contrib.auth.urls')),    
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]