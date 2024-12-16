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

    path('shop/', views.catalogue, name='catalogue'),
    path('shop/favourite', views.fav, name='fav'),
    path('shop/<int:merchid>', views.merchpage, name='merchpage'),
    path('buy/<int:merchid>', views.buy, name='buy'),
    path('swapfav/<int:merchid>_<int:direction>', views.swapfav, name='swapfav'),
    path('mercheditor/', views.mercheditorempty, name='mercheditorempty'),
    path('mercheditor/<int:merchid>', views.mercheditorfilled, name='mercheditorfilled'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:orderid>', views.order, name='order'),
    path('status/<int:orderid>', views.statusupdate, name='statusupdate'),
    path('deletion/<int:orderid>', views.deletion, name='deletion')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
