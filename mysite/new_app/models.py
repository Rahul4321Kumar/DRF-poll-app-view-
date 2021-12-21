from django.db import models

class Question(models.Model):
    """
    This class represents Question fields
    """
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.question_text

    
class Choice(models.Model):
    """
    This class represents Choice fields
    """
    question = models.ForeignKey(Question, on_delete = models.CASCADE,
    related_name = 'choices', blank = True )
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text
