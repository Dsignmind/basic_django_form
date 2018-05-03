from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    # return HttpResponse('<h1 style="text-align:center;"><em>My Second App</em></h1>')
    return render(request, 'appTwo/index.html')


def help(request):
    index_dict = {'help_tag': 'Help Page'}
    return render(request, 'appTwo/help.html', context=index_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    users_dict = {'users_list': user_list}
    return render(request, 'appTwo/users.html', context=users_dict)


def signup(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Form invalid!')
    return render(request, 'appTwo/signup.html', {'form': form})
