from django.conf.urls import url
from vidseries.views import viddisplay_ext

urlpatterns = [
	url(r'^(?P<series_num>[0-9]{2})/(?P<lesson_num>[0-9]{2})/$', viddisplay_ext)
]

