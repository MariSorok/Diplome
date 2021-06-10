from django.forms import ModelForm, Textarea
from project.models import Dish

# Create the form class.
class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['image', 'category', 'name', 'description', 'price']
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 4}),
        }