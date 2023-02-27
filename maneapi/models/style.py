"""Hair styles class module"""
from django.db import models


class HairStyle(models.Model):
    """Hair style model class"""
    label = models.CharField(max_length=50)

    @property
    def total_clients(self):
        return self.__client

    @total_clients.setter
    def total_clients(self, value):
        self.__client = value
