from django.db import models



# Create your models here.
class userMsg(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
    
class botMsg(models.Model):
    user_msg = models.ForeignKey(userMsg, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

