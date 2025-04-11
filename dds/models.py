from django.db import models
from django.core.exceptions import ValidationError

class Status(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name
    

class CashFlow(models.Model):

    date_created = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def clean(self):
        if self.category.type != self.type:
            raise ValidationError("Выбранная категория не принадлежит выбранному типу.")
        if self.subcategory.category != self.category:
            raise ValidationError("Выбранная подкатегория не принадлежит выбранной категории.")
        
    def __str__(self):
        return f"{self.date_created} - {self.type} - {self.amount} руб."
