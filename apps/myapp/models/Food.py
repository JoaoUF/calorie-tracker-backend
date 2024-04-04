from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel


class Food(ActivatorModel, TimeStampedModel, Model):
    name = models.CharField(
        db_column='name',
        max_length=100
    )
    carbs = models.FloatField(
        db_column='carbs',
    )
    protein = models.FloatField(
        db_column='protein',
    )
    fats = models.FloatField(
        db_column='fats',
    )
    calories = models.IntegerField(
        db_column='calories',
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'MAE_FOOD'
