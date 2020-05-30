from django.urls import path
from . import views

urlpatterns = [

	path('', views.IndexView.as_view(), name = 'polls-index'),
	path('<int:pk>/', views.DetailView.as_view(), name = 'polls-detail'),
	path('<int:pk>/results', views.ResultsView.as_view(), name = 'polls-results'),
	path('<int:question_id>/vote', views.vote, name = 'polls-vote'),

	]