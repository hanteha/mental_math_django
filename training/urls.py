from django.urls import path

from . import views

app_name = 'training'
urlpatterns = [
    path('<int:id_question>', views.question_training),
    path('', views.home_user_training)
]