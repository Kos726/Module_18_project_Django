from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister

users = ['tor', 'gor', 'frog', 'rog', 'smog']

info_ = {}

# Create your views here.
def sign_up_by_html(request):
    if request.method == "POST":
        # Получение данных
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        # HTTP ответ пользователя

        # Валидация данных
        is_valid_age = int(age) >= 18
        is_valid_user = username.lower() not in users
        is_valid_password = password == repeat_password

        if is_valid_age is False:
            info_.update({'error': 'Вы должны быть старше 18'})

        elif is_valid_user is False:
            info_.update({'error': 'Пользователь уже существует'})

        elif is_valid_password is False:
            info_.update({'error': 'Пароли не совпадают'})

        # если все проверки пройдены
        elif is_valid_age and is_valid_user and is_valid_password is True:
            return HttpResponse(f'Приветствуем, {username}!')

        # Если GET
    context = info_

    return render(request, 'fifth_task/registration_page.html', context)


def sign_up_by_django(request):
    if request.method == "POST":
        # Получение данных
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обработка данных формы
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

        # Валидация данных
        is_valid_age = int(age) >= 18
        is_valid_user = username.lower() not in users
        is_valid_password = password == repeat_password

        if is_valid_age is False:
            info_.update({'error': 'Вы должны быть старше 18'})

        elif is_valid_user is False:
            info_.update({'error': 'Пользователь уже существует'})

        elif is_valid_password is False:
            info_.update({'error': 'Пароли не совпадают'})

        # если все проверки пройдены
        elif is_valid_age and is_valid_user and is_valid_password is True:

            return HttpResponse(f'Приветствуем, {username}!')

        # HTTP ответ пользователя
    else:
        form = UserRegister()

        # Если GET
    form_ = {'form': form}
    context = {**form_, **info_}
    return render(request, 'fifth_task/registration_page.html', context)
