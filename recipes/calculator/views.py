from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'картофель, гр.': 100,
        'морковь, гр.': 50,
        'огурцы, гр.': 50,
        'горошек, гр.': 30,
        'майонез, мл.': 70,
    },
  'pizza':  {
        'сыр, гр.': 50,
        'томаты, гр.': 50,
        'тесто, гр.': 100,
        'бекон, гр.': 30,
        'колбаса, гр.': 30,
        'грибы, гр.': 20,
  },
    'dessert': {
        'хурма, гр.': 60,
        'киви, гр.': 60,
        'творог, гр.': 60,
        'сахар, гр.': 10,
        'мед, мл.': 50,  
  }
    # можете добавить свои рецепты ;)
}


def recipes_list(request, dish):
    if dish in DATA:
        choice_dish = DATA[dish]
        servings = request.GET.get('servings', '1')
        if servings.isdigit():
            servings = int(servings)
            choice_dish1 = {}
            for key in choice_dish:
                
                choice_dish1[key] = choice_dish[key] * servings
            context = {"choice_dish": choice_dish1, "dish": dish, 'data': DATA}
        else:
            context = {"choice_dish": choice_dish, "dish": dish, 'data': DATA}
    else:
        context = {"dish": dish, 'data': DATA}

    return render(request, 'calculator/index.html', context=context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }