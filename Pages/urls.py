from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="index"),
    path('search', views.search, name="search"),
    path('post/<int:id>/', views.post, name='post'),
    path('<str:languageName>', views.language, name='language'),
]