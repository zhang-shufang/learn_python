from pyexpat import model
from django.db import models

# Create your models here.

# Pizza 的模型
class Pizza(models.Model):
    """一个关于披萨的类，主要记录披萨的种类名"""
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name


# Pizza上的馅料的模型
class Topping(models.Model):
    """一个关于披萨上的馅料的模型，记录具体的馅料，并关联到对应的披萨上。"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name