from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def platform(request):
    title = "Главная страница"

    context = {
        'title': title,
    }

    return render(request, 'third_task/platform.html', context)


class Shop(TemplateView):
    template_name = 'third_task/shop.html'


def products(request):
    title = "Магазин"
    text_back = "Вернуться обратно"

    subject = "Выбирите продукт"

    list_products = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    len_list = len(list_products)

    context = {
        'title': title,
        'button_back': text_back,
        'subject': subject,
        'list_products': list_products,
        'len_list': len_list,
    }

    return render(request, 'third_task/games.html', context)


def shopping_cart(request):
    title = "Корзина"
    button_back = "Вернуться обратно"

    list_products = []

    if len(list_products) == 0:
        subject = "Ваша корзина пуста"
    else:
        subject = "Выбранные товары"

    context = {
        'title': title,
        'button_back': button_back,
        'subject': subject,
    }

    return render(request, 'third_task/cart.html', context)
