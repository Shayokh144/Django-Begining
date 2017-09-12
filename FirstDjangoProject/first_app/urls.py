from django.conf.urls import url
from first_app import views


urlpatterns = [
	url(r'^$',views.index,name='index'),   # http://127.0.0.1:8000/first_app/
	url(r'^abc',views.index,name='index'), # http://127.0.0.1:8000/first_app/abc
]
