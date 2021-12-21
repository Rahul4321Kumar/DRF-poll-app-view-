from django.urls import path

from new_app import views

urlpatterns = [
    path('questions/', views.QuestionsView.as_view(), name='questions_view'),
]