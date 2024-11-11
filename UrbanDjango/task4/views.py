from django.shortcuts import render

# Create your views here.

TMP_FLDR = 'four_task/'

def main_page(request):
    title = 'Главнвя страница'
    text = 'В компании ParkerBrewery мы стремимся создавать уникальные сорта пива, которые радуют ценителей и новичков. Наша команда опытных пивоваров использует только лучшие ингредиенты: от отборного ячменя до свежих хмелей, чтобы обеспечить высокое качество и насыщенный вкус каждого напитка. Мы гордимся традициями пивоварения, сочетая их с инновационными методами, что позволяет нам разрабатывать оригинальные рецепты. В нашем ассортименте вы найдете как классические сорта, так и крафтовые новинки, каждая из которых рассказывает свою историю. ParkerBrewery — это не просто пиво, это искусство, созданное с любовью и страстью.'

    context = {
        'title': title,
        'text': text
    }
    return render(request, TMP_FLDR+'main_page.html', context)

def second_page(request):
    title = 'Купить BEER'
    context = {
        'title': title
    }
    return render(request, TMP_FLDR+'second_page.html', context)

def third_page(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, TMP_FLDR+'third_page.html', context)