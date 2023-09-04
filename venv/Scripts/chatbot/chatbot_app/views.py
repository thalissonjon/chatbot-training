from django.http import JsonResponse
from django.shortcuts import render

def botAnswer(request):
    option = request.GET.get('option') # pega da pagina

    match option:
        case '1':
            resposta = 'A opçao escolhida foi a numero 1.'
        case '2':
            resposta = 'A opçao escolhida foi a numero 2.'
        case '3':
            resposta = 'A opçao escolhida foi a numero 1.'
        case _:
          resposta = 'Entrada invalida'

    return JsonResponse({'resposta': resposta})



