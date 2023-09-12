from django.db import models

# https://samiddha99.medium.com/implement-dynamic-select-options-with-django-d04e791f0483 IMPORTANTE

# Create your models here.
class userMsg(models.Model):
    userText = models.PositiveSmallIntegerField()
    def __str__(self):
        return self.userText
    
class botMsg(models.Model):

    CONSULTAS = 1
    EXAMES = 2
    INFORMACOES = 3

    INICIO = (
        (CONSULTAS, 'Consultas'),
        (EXAMES, 'Exames'),
        (INFORMACOES, 'Informações')
        )



    CONSULTAS = (
        ('')
    )

    EXAMES = (
        ('')
    )

    

    
    botResp = models.ForeignKey(userMsg, on_delete=models.CASCADE)
    
    # choice_text = models.CharField(max_length=100)
    # pos = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


