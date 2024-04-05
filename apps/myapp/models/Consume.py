from django.db import models
from utils.model import Model
from django_extensions.db.models import ActivatorModel, TimeStampedModel
from django.conf import settings
from apps.myapp.models import Food


class Consume(ActivatorModel, TimeStampedModel, Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        db_column='user'
    )
    foodConsumed = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        db_column='food'
    )

    class Meta:
        db_table = 'MAE_CONSUME'
