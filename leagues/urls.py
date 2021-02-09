from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('initialize', views.make_data, name="make_data"),
	path('all_data', views.all_data),
	path('query_1', views.query_1),
	path('query_2', views.query_2),
	path('query_3', views.query_3),
	path('query_4', views.query_4),
	path('query_5', views.query_5),
	path('query_6', views.query_6),
	path('query_7', views.query_7),
	path('query_8', views.query_8),
	path('query_9', views.query_9),
	path('query_10', views.query_10),
	path('query_11', views.query_11),
	path('query_12', views.query_12),
	path('query_13', views.query_13),
	path('query_14', views.query_14),
	path('query_15', views.query_15),
	path('query_16', views.query_16)
]
