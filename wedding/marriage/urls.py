from django import template
from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),

    path('',views.home,name='home'),
    path('about-us/',views.about,name='about'),
    path('Match-request/',views.request,name='request'),
    path('Matched/',views.matched,name='match'),
    path('profile/',views.profile,name='profile'),
    path('updateProfile/',views.updateProfile,name='updateProfile'),

    path('search/',views.search,name='search'),
    path('filter-data/',views.filter_data,name='filter_data'),
    path('search/detail/',views.searchDetail,name='searchDetail'),
    path('intress/',views.intress,name='intress'),
    path('notintrest/',views.notintrest,name='notintrest'),
    
    path('logout/',views.logout,name='logout'),
]
