from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from vidseries.models import Video, Series
# Create your views here.


def viddisplay_ext(request, series_num, lesson_num):

	current_vid = Video.objects.get(series_id=int(series_num), lesson_num=int(lesson_num))
	video_list = Video.objects.filter(series_id=int(series_num))

	context = {
		#'prev_vid' : prev_vid,
		'video':current_vid,
	    #'next_vid':next_vid,
		'video_list': video_list,
	}
	return render(request, 'video_display.html', context)



