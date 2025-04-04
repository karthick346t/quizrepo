from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_option = models.IntegerField()  # Stores the correct answer (1, 2, 3, or 4)

    def __str__(self):
        return self.text
