from django.conf.urls import url
from blog.views import blog_display

urlpatterns = [
	url(r'^(?P<cat_num>[0-9]{2})/(?P<post_num>[0-9]{2})/$', blog_display)
]

