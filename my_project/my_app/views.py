from django.shortcuts import render
from my_app.forms import UserForm
# Create your views here.
from .models import UserInfo
import requests

def index(request):
    """Home Page for UserInfo"""
    return render(request, "my_app/index.html")


def userinfo(request):
    "Shows every infor for user"
    userinfo = UserInfo.objects.order_by('date_recorded')
    context = {"userinfo": userinfo}
    return render(request, "my_app/userinfo.html", context)
"""    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request,"my_app/form.html",{'form':form})
        #No data submitted; creating a blank form
"""




def thankingyou(request):
    #"Thanking the attender"
    return render(request, "my_app/thankingyou.html")

'''def form(request):
    form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST)

        if form.is_valid():
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email_address'])
            print("Roll NO"+form.cleaned_data['roll_no'])
            print("Feedback"+form.cleaned_data['feedback'])

    return render(request,"my_app/form.html",{'form':form}) '''


def users(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thankingyou(request)
        else:
            print("Error Form Invalid")

    return render(request,'my_app/form.html',{'form':form})
