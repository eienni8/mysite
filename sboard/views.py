#from django.shortcuts import render
#from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone


def index(request):
    """
    sboard 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}
    return HttpResonse("안녕하세요 sboard에 오신 것을 환영합니다.")



def detail(request, question_id): 
    """
    sboard 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'sboard/question_detail.html' , context)

def answer_create(request, question_id):
    """
    sboard 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('sboard:detail', question_id=question.id)




# Create your views here.
