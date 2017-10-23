from unittest import loader

from django.http import HttpResponse
from django.shortcuts import render
from .models import Question
# Create your views here.
def index(request):
    return HttpResponse("Hello")

def detail(request, question_id):
    return HttpResponse("hjgfl %s" % question_id)

def results(request, question_id):
    response = "Hello %st"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("hi %s" % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))