from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from vidseries.models import Video, Series
# Create your views here.
#class views(View):


'''def  sidenav(request, series_num, lesson_num):
	vids = Video.objects.get(series_num=series_num)
	context = {
		'videos':vids
	}
	return render(request, 'video_detail.html', context)

def header(request):
	series = Video.objects.all()
	context = {
		'topics': series
	}
	return render(request, 'header.html', context)


def viddisplay(request, series_num, lesson_num):
	vid = Video.objects.get(series_id=int(series_num), lesson_num=int(lesson_num))
	context = {
		'video':vid
	}
	return render(request, 'video_display.html', context)'''

def viddisplay_ext(request, series_num, lesson_num):

	# Need more generic logic here to catch any instance that is not found... maybe an error catch?
	current_vid = Video.objects.get(series_id=int(series_num), lesson_num=int(lesson_num))
	video_list = Video.objects.filter(series_id=int(series_num))
	'''if (int(lesson_num) == 1):
		prev_vid = video_list[0]
	if (int(lesson_num) == len(video_list)):
		next_vid = video_list[len(video_list)]
	else:
		prev_vid = video_list[int(lesson_num)-2]
		next_vid = video_list[int(lesson_num)]
						'''
	context = {
		#'prev_vid' : prev_vid,
		'video':current_vid,
	    #'next_vid':next_vid,
		'video_list': video_list,
	}
	return render(request, 'video_display.html', context)



