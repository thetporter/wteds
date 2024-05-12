"""
Definition of urls for wteds.
"""

from datetime import datetime
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('pool/', views.pool, name='pool'),
    path('video/', views.video, name='video'),

    path('create/<str:type>', views.create, name='create'),
    path('singlepost/<int:postid>/', views.singlepost, name='singlepost'),
    path('thread/<int:threadid>/', views.thread, name='thread'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.registration, name='register'),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
