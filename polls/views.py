from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]

    # 하드코딩 (나쁜 예)
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

    # 템플릿 분리
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list
    }
    # return HttpResponse(template.render(context, request))

    # 지름길 render(request, 템플릿 이름, context-> HttpResponse) 사용 - model을 안가져와도 됨.
    return render(request, "polls/index.html", context)
    
    

def detail(request, question_id):
    # return HttpResponse("looking at questions %s." % question_id)
    # 404 에러 발생
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, "polls/detail.html", {"question": question})

    # 404에러 발생 shortcut 버전
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
def results(request, question_id):
    response = "looking at result %s." 
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("voting on question %s." % question_id)