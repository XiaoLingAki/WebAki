from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_text
    
class Personality(models.Model):
    personality_type = models.CharField(max_length=200)
    personality_id = models.IntegerField(default=0)
