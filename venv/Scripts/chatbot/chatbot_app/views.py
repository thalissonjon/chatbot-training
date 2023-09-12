from django.http import JsonResponse
from django.shortcuts import render

from .models import userMsg, botMsg

def botAnswer(request):
    option = request.GET.get('option') # pega da pagina

    msg = userMsg(userText='oiii teste teste')
    print(msg)

    msg, resp = inputMsg(option)

    

    return JsonResponse({'resposta': msg})


def inputMsg(option):
    msg = userMsg.objects.get(option = option)
    resp = botMsg.objects.filter(msg = msg)
    return(msg.userText, resp.botResp)

    # resp = botMsg.objects.filter(resp = resp)


