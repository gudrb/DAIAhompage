from django.shortcuts import get_object_or_404,render
from polls.models import Question,Choice,Newmember
from polls.forms import ModelNameForm

def index(request):
    latest_question_list0 = Question.objects.all()[0]
    latest_question_list1 = Question.objects.all()[1]
    latest_choice_list = Choice.objects.all()
    latest_memeber_list = Newmember.objects.all()
    context={
        'latest_question_list0': latest_question_list0,
        'latest_question_list1':latest_question_list1,
        'latest_choice_list':latest_choice_list,
        'latest_member_list': latest_memeber_list
    }
    return render(request,'polls/index.html',context)

def okay(request,choice_id):

    if request.method == 'POST' and 'btn1' in request.POST:

        latest_question_list0 = Question.objects.all()[0]
        latest_question_list1 = Question.objects.all()[1]
        latest_choice_list = Choice.objects.all()
        member = Choice.objects.get(id=choice_id)
        newmember = Newmember()
        newmember.name = member.name
        newmember.email = member.email
        newmember.password = member.password
        newmember.git = member.git
        newmember.sns = member.sns
        newmember.student_id = member.student_id
        newmember.phone_num = member.phone_num
        # newmember.image = member.image
        newmember.save()
        latest_member_list = Newmember.objects.all()
        member.delete()
        context = {
            'latest_question_list0': latest_question_list0,
            'latest_question_list1': latest_question_list1,
            'latest_choice_list': latest_choice_list,
            'latest_member_list': latest_member_list
        }
        return render(request, 'polls/index.html', context)

    elif request.method == 'POST' and 'btn2' in request.POST:
        deny = Choice.objects.get(id=choice_id)
        deny.delete()

        latest_question_list0 = Question.objects.all()[0]
        latest_question_list1 = Question.objects.all()[1]
        latest_choice_list = Choice.objects.all()
        latest_member_list = Newmember.objects.all()
        context = {
            'latest_question_list0': latest_question_list0,
            'latest_question_list1': latest_question_list1,
            'latest_choice_list': latest_choice_list,
            'latest_member_list': latest_member_list
        }
        return render(request, 'polls/index.html', context)


def detail(request,member_id):
    member = Newmember.objects.get(id=member_id)
    form_class = ModelNameForm(initial=
                               {'name':member.name,
                                'email':member.email,
                                'password': member.password,
                                'git': member.git,
                                'sns': member.sns,
                                'student_id': member.student_id,
                                'phone_num': member.phone_num
                                })
    context = {
        'member': member,
        'form': form_class
    }

    return render(request,'polls/detail.html',context)

def modify(request,member_id):
    if request.method == 'POST' and 'btn1' in request.POST:
        member = Newmember.objects.filter(id=member_id)
        form = ModelNameForm(request.POST)

        form.save()
        member.delete()

        latest_question_list0 = Question.objects.all()[0]
        latest_question_list1 = Question.objects.all()[1]
        latest_choice_list = Choice.objects.all()
        latest_member_list = Newmember.objects.all()
        context = {

            'latest_question_list0': latest_question_list0,
            'latest_question_list1': latest_question_list1,
            'latest_choice_list': latest_choice_list,
            'latest_member_list': latest_member_list
        }
        return render(request, 'polls/index.html', context)
    elif request.method == 'POST' and 'btn2' in request.POST:
        member = Newmember.objects.get(id=member_id)
        member.delete()

        latest_question_list0 = Question.objects.all()[0]
        latest_question_list1 = Question.objects.all()[1]
        latest_choice_list = Choice.objects.all()
        latest_member_list = Newmember.objects.all()
        context = {
            'latest_question_list0': latest_question_list0,
            'latest_question_list1': latest_question_list1,
            'latest_choice_list': latest_choice_list,
            'latest_member_list': latest_member_list
        }

        return render(request, 'polls/index.html',context)
