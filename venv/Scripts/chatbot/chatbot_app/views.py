from django.http import JsonResponse
from django.shortcuts import redirect, render

from .models import botMsg, userMsg

conversation_state = []

def conversation(user_text):
    bot_text = ""

    if not conversation_state: # inicio, sem state
        bot_text = "1 - Consultas\n2 - Exames\n3 - Informações\n"
        conversation_state.append('initial')

    else: 
        current_state = conversation_state[-1]
        
        if current_state == 'initial':
            if user_text == '1':
                bot_text = "1 - Verificar status de consultas\n2 - Reagendar consultas\n3 - Retornar ao menu anterior"
                conversation_state.append('consultas')
            if user_text == '2':
                bot_text = "1 - Verificar status de exames\n2 - Reagendar exames\n3 - Retornar ao menu anterior"
                conversation_state.append('exames')
            if user_text == '3': 
                bot_text = "Informações ETC ETC ETC ETC\n 1 - Retornar ao menu anterior "
                conversation_state.append('informacoes')

        # ----------| CONSULTAS |----------

        if current_state == 'consultas':
            if user_text == '1':
                # requisição para puxar as consultas com seus status
                bot_text = "STATUS DE CONSULTAS\n 1 - Retornar ao menu anterior"
                conversation_state.append('consultas_status')
            if user_text == '2':
                # requisição para puxar as consultas e tratar reagendamentos
                bot_text = "REAGENDAR CONSULTAS"
                conversation_state.append('consultas_reagendar')
            if user_text == '3': # retorno
                conversation_state.pop()

        if current_state == 'consultas_status':
            if user_text == '1': # retorno
                conversation_state.pop()

        if current_state == 'consultas_reagendar':
            if user_text == '1': # retorno
                conversation_state.pop()


        # ----------| EXAMES |----------

        if current_state == 'exames':
            if user_text == '1':
                # requisição para puxar os exames com seus status
                bot_text = "STATUS DE EXAMES\n 1 - Retornar ao menu anterior"
                conversation_state.append('exames_status')
            if user_text == '2':
                # requisição para puxar os exames e tratar reagendamentos
                bot_text = "REAGENDAR EXAMES"
                conversation_state.append('exames_reagendar')
            if user_text == '3': # retorno
                conversation_state.pop()

        if current_state == 'exames_status':
            if user_text == '1': # retorno
                conversation_state.pop()

        if current_state == 'exames_reagendar':
            if user_text == '1': # retorno
                conversation_state.pop()

        # ----------| INFORMAÇÕES |----------
        if current_state == 'informacoes':
            if user_text == '1': # retorno
                conversation_state.pop()

    bot_message = botMsg.objects.create(text=bot_text)

    return bot_text

def chat_view(request):
    if request.method == 'POST':
        user_text = request.POST['user_text']
        user_message = userMsg.objects.create(text=user_text)
        
        bot_text = conversation(user_text)
        user_message.save()

        return redirect('chatbot/chat')
    
    user_messages = userMsg.objects.all()
    bot_messages = botMsg.objects.all()
    return #voltar para o front


def conversation_test(request):

    user_text = request.GET.get('user_text')
    bot_text = ""

    if not conversation_state: # inicio, sem state
        bot_text = "1 - Consultas\n2 - Exames\n3 - Informacoes\n"
        conversation_state.append('initial')

    else: 
        current_state = conversation_state[-1]
        print(current_state)
        if current_state == 'initial':
            if user_text == '1':
                bot_text = "1 - Verificar status de consultas\n2 - Reagendar consultas\n3 - Retornar ao menu anterior"
                conversation_state.append('consultas')
            if user_text == '2':
                bot_text = "1 - Verificar status de exames\n2 - Reagendar exames\n3 - Retornar ao menu anterior"
                conversation_state.append('exames')
            if user_text == '3': 
                bot_text = "INFO ETC ETC ETC ETC\n 1 - Retornar ao menu anterior "
                conversation_state.append('informacoes')

        # ----------| CONSULTAS |----------

        if current_state == 'consultas':
            if user_text == '1':
                # requisição para puxar as consultas com seus status
                bot_text = "STATUS DE CONSULTAS\n 1 - Retornar ao menu anterior"
                conversation_state.append('consultas_status')
            if user_text == '2':
                # requisição para puxar as consultas e tratar reagendamentos
                bot_text = "REAGENDAR CONSULTAS"
                conversation_state.append('consultas_reagendar')
            if user_text == '3': # retorno
                conversation_state.pop()

        if current_state == 'consultas_status':
            if user_text == '1': # retorno
                conversation_state.pop()

        if current_state == 'consultas_reagendar':
            if user_text == '1': # retorno
                conversation_state.pop()


        # ----------| EXAMES |----------

        if current_state == 'exames':
            if user_text == '1':
                # requisição para puxar os exames com seus status
                bot_text = "STATUS DE EXAMES\n 1 - Retornar ao menu anterior"
                conversation_state.append('exames_status')
            if user_text == '2':
                # requisição para puxar os exames e tratar reagendamentos
                bot_text = "REAGENDAR EXAMES"
                conversation_state.append('exames_reagendar')
            if user_text == '3': # retorno
                conversation_state.pop()

        if current_state == 'exames_status':
            if user_text == '1': # retorno
                conversation_state.pop()

        if current_state == 'exames_reagendar':
            if user_text == '1': # retorno
                conversation_state.pop()

        # ----------| INFORMAÇÕES |----------
        if current_state == 'informacoes':
            if user_text == '1': # retorno
                conversation_state.pop()

    bot_message = botMsg.objects.create(text=bot_text)
    print('pilha inteira', conversation_state)

    return JsonResponse({'resposta': bot_text})




