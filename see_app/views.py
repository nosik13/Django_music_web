from django.shortcuts import render

from .models import Topic


# Create your views here.
def index(request):
    """Домашняя страница приложения see_app"""
    return render(request, r'see_app\index.html')


def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('-date_added')
    context = {'topics': topics}
    return render(request, r'see_app\topics.html', context)


def timetable(request):
    """Расписание"""
    return render(request, r'see_app\timetable.html')
