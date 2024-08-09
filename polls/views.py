from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#
#     # 하드코딩 (나쁜 예)
#     # output = ", ".join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#
#     # 템플릿 분리
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     # return HttpResponse(template.render(context, request))
#
#     # 지름길 render(request, 템플릿 이름, context-> HttpResponse) 사용 - model을 안가져와도 됨.
#     return render(request, "polls/index.html", context)
#
#
#
# def detail(request, question_id):
#     # return HttpResponse("looking at questions %s." % question_id)
#     # 404 에러 발생
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return render(request, "polls/detail.html", {"question": question})
#
#     # 404에러 발생 shortcut 버전
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
#
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question" : question,
                "error_message": "You didn't select a choice",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
