from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
# TASK_5
users = ['ira', 'nikita', 'Kolya', 'Masha']
def sign_up_by_html(request):
    
    info = {}
    
    # If method = POST
    if request.method == 'POST':
        # Get data
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get('age')

        print(f'Username: {username}')
        print(f'Passsword: {password}')
        print(f'Repeat_password: {repeat_password}')
        print(f'Age: {age}')

        if password == repeat_password and username not in users and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if username in users:
                info['error'] = f'Пользователь {username} уже существует'
            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # Get data
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            repeat_password = form.cleaned_data('repeat_password')
            age = form.cleaned_data('age')

            #Logic
            if password == repeat_password and username not in users and int(age) >= 18:
                users.append(username)
                info['error'] = f'Приветствуем, {username}!'
                info['form'] = form
                
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context=info)       