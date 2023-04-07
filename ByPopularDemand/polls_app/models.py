from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    """A class representing a poll question.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time the question was published.
    """


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    

    def was_published_recently(self):
        """Check if the question was published recently.

        Returns:
            bool: True if the question was published within the last day, False otherwise.
        """
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """A class representing a choice for a poll question.

    Attributes:
        question (Question): The question this choice belongs to.
        choice_text (str): The text of the choice.
        votes (int): The number of votes this choice has received.
    """

    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text