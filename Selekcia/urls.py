from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'[Cc]eny/(?P<uk>[0-9]+)', views.cenyDetail, name="cenyDetail"),      
    url(r'[Cc]eny', views.ceny, name='ceny'),   
    url(r'', views.main, name='main'),
]
                                                       