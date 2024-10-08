from core.models import BaseModel
from django.db import models


class Curriculum(BaseModel):
    """ curriculums table """
    name = models.CharField(max_length=32, default="arabic")

    def __str__(self):
        return f"{self.name}"

class Grade(BaseModel):
    """ grades table """
    title = models.CharField(max_length=64)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.curriculum}"


class Semester(BaseModel):
    """ semesters table """
    title = models.CharField( # models.TextChoices
        max_length=1,
        choices=[
            ("no_term", "No Term"),       # for grades with one term like third year of secondary school
            ("first_term", "First Term"),
            ("2", "Second Term"),
            ])
    starting_date = models.DateField()
    ending_date = models.DateField()

    def __str__(self):
        return f"{self.title}"
    @staticmethod
    def get_current_semester()-> Semester:
        return Semester.objects.filter(
        starting_date__lte=timezone.now(),
        ending_date__gte=timezone.now()
        ).first()
