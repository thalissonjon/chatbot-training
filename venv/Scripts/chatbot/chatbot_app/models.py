from django.db import models



# Create your models here.
class userMsg(models.Model):
    userText = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.userText
    
class botMsg(models.Model):
    INICIO = (
        ('1', 'Consultas'),
        ('2', 'Exames'),
        ('3', 'Informações')
    )

    CONSULTAS = (
        
    )

    EXAMES = (
        ('')
    )

    choiceInt = models.PositiveSmallIntegerField(
        choices = CONSULTAS,
        default=3
    )

    
    botResp = models.ForeignKey(userMsg, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=100)
    # pos = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


