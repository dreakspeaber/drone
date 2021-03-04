from django.urls import path, include, re_path
from web import views

urlpatterns = [
    
    path('', views.signin.as_view(),name='signin'),
    path('logout', views.logoutpg.as_view()),
    path('dash',views.dash.as_view(),name='dash'),
    

]