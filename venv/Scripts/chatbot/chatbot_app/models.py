from django.db import models



# Create your models here.
class userMsg(models.Model):
    userText = models.TextField()

    def __str__(self):
        return self.userText
    
class botMsg(models.Model):
    CONSULTAS = (
        ('1', 'Verificar consultas'),
        ('2,', 'Agendar consultas'),
        ('3', 'Retornar')
    )

    choiceInt = models.PositiveSmallIntegerField(
        choices = CONSULTAS,
        default=3
    )

    botResp = models.ForeignKey(userMsg, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    pos = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


    

    # choice = models.PositiveSmallIntegerField(
    #     choices = Consultas.choices
    # )
