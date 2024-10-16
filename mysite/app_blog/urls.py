from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='home'),  # Головна сторінка з переліком статей
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.ArticleDetailView.as_view(), name='news-detail'),  # Детальний перегляд статті
]
