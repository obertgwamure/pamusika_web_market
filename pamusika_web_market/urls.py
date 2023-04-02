from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . forms import LoginForm


# URL Patterns
app_name = 'pamusika_web_market'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name ='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='pamusika_web_market/login.html', authentication_form=LoginForm), name='login'),
]

