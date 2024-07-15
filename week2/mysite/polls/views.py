from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-id")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#get คือการ select ข้อมูลจาก db โดยจะยอม return เเค่1เเถว   q = Question.objects.get(pk=question_id) #get คือการ select ข้อมูลจาก db โดยจะยอม return เเค่1เเถว
#filter คือการ select ข้อมูลจาก db โดยจะยอม return >1เเถว  qs = Question.objects.filter(pk=question_id) #filter คือการ select ข้อมูลจาก db โดยจะยอม return >1เเถว

# def detail(request, question_id):
#     q = Question.objects.get(pk=question_id) #get คือการ select ข้อมูลจาก db โดยจะยอม return เเค่1เเถว
#     print("get ->", q)
#     qs = Question.objects.filter(pk=question_id) #filter คือการ select ข้อมูลจาก db โดยจะยอม return >1เเถว
#     print("get ->", qs)
#     return HttpResponse("You're looking at question %s." % q.question_text)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, "detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)