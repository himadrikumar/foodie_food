from django.db import models


class Food(models.Model):
    """A food the user has selected"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model"""
        return self.text


class FoodRequest(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ratings'

    def __str__(self):
        """return a string representation of the model"""
        return f'{self.text[:50]}...'
