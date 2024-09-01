"""
This file is for the models of the polls app.

The models are the classes that represent the data in the database.

- The Question class represents the question and the date it was published.
- The Choice class represents the choices and the votes for each choice.

The models are defined in a class that inherits from django.db.models.Model.

Each attribute of the class represents a field in the database.
- The models are defined in a separate file so that they can be imported in other files.
- The models are used in the views to interact with the database.

"""
from django.db import models


class Question(models.Model):
    """
    Represents a question and its publication date.
    
    Arguments:
        models (type): _description
    
    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time when the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model): # Choice is for the choices and the votes
    """
    Represents a choice for a question and the number of votes for that choice.
    Args:
        models (_type_): _description_
    
    Attributes:
        question (Question): The question that the choice is associated with.
        choice_text (str): The text of the choice.
        votes (int): The number of votes for the choice.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
