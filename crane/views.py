from django.shortcuts import render
import hashlib
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core.paginator import Paginator
# Create your views here.
from crane.models import *
from django.contrib import messages

def setpwd(password):
    md5=hashlib.md5()
    md5.update(password.encode())
    result=md5.hexdigest()
    return result

def loginDecorator(func):
    '''
    1.获取cookies中的username 和 email
    2.判断username 和email
    3.如果成功 跳转主页
    4.如果失败 跳转登录页
    :param func:
    :return:
    '''
    def inner(request,*args,**kwargs):
        email=request.COOKIES.get("username")
        session_email=request.session.get("username")

        if email and session_email and email==session_email:
            return func(request,*args,**kwargs)
        else:
            return HttpResponseRedirect('/crane/login/')
    return inner

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username:
            user=User.objects.filter(username=username).first()
            if user:
                if user.password==password and user.username==username:
                    response=HttpResponseRedirect('/crane/index/')
                    # response.set_cookie('email',user.email)
                    # request.session['email']=user.email
                    return response
                else:
                   messages.error(request,"密码错误")
            else:
                messages.error(request, "邮箱或密码错误")
        else:
            messages.error(request, "邮箱错误")
        return render(request,'crane/login.html')
    return render(request,'crane/login.html')

def base(request):
    return render(request,'crane/base.html',locals())

def index(request):
    return render(request,'crane/index.html',locals())

def addDoc(request):
    return render(request,'crane/add_doc.html',locals())

def alerts(request):
    return render(request,'crane/alerts.html',locals())

def buttons(request):
    return render(request,'crane/buttons.html',locals())

def cards(request):
    return render(request,'crane/cards.html',locals())

def chartjs(request):
    return render(request,'crane/chartjs.html',locals())

def checkbox(request):
    return render(request,'crane/checkbox.html',locals())

def colorpicker(request):
    return render(request,'crane/colorpicker.html',locals())

def config(request):
    return render(request,'crane/config.html',locals())

def configUpload(request):
    return render(request,'crane/config_upload.html',locals())

def dataTable(request):
    return render(request,'crane/data_table.html',locals())

def datepicker(request):
    return render(request,'crane/datepicker.html',locals())

def doc(request):
    return render(request,'crane/doc.html',locals())

def editpwd(request):
    return render(request,'crane/edit_pwd.html',locals())

def elements(request):
    return render(request,'crane/elements.html',locals())

def error(request):
    return render(request,'crane/error.html',locals())

def formSwitch(request):
    return render(request,'crane/forms_switch.html',locals())

def gallery(request):
    return render(request,'crane/gallery.html',locals())

def grid(request):
    return render(request,'crane/grid.html',locals())

def guide(request):
    return render(request,'crane/guide.html',locals())

def icons(request):
    return render(request,'crane/icons.html',locals())

def jconfirm(request):
    return render(request,'crane/jconfirm.html',locals())

def main(request):
    return render(request,'crane/main.html',locals())

def modals(request):
    return render(request,'crane/modals.html',locals())

def notify(request):
    return render(request,'crane/notify.html',locals())

def onfigSystem(request):
    return render(request,'crane/onfig_system.html',locals())

def other(request):
    return render(request,'crane/other.html',locals())

def pagination(request):
    return render(request,'crane/pagination.html',locals())

def profile(request):
    return render(request,'crane/profile.html',locals())

def progress(request):
    return render(request,'crane/progress.html',locals())

def rabc(request):
    return render(request,'crane/rabc.html',locals())

def radio(request):
    return render(request,'crane/radio.html',locals())

def sliders(request):
    return render(request,'crane/sliders.html',locals())

def step(request):
    return render(request,'crane/step.html',locals())

def tables(request):
    return render(request,'crane/tables.html',locals())

def tabs(request):
    return render(request,'crane/tabs.html',locals())

def tagInput(request):
    return render(request,'crane/tags_input.html',locals())

def tooltipsPopover(request):
    return render(request,'crane/tooltips_popover.html',locals())

def typography(request):
    return render(request,'crane/typography.html',locals())