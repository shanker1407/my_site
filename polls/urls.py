from django.urls import path
from.import views

urlpatterns = [
    path('home/', views.home, name='home.html'),
    path('<int:question_id>/vote/', views.vote, name="vote"),
    path('<int:question_id>/result/', views.results, name='result.html'),
    path('<int:question_id>/', views.details, name='details.html'),
]
