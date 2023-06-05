from django import forms
from django import forms

from . models import Item

# creating a form classes
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        # adding styling and attributes to fields
        widgets = {
                'category': forms.Select(attrs={
                        'class': 'form-control'
                    }),
                'name': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                'description': forms.Textarea(attrs={
                        'class': 'form-control'
                    }),
                'price': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                'image': forms.FileInput(attrs={
                        'class': 'form-control'
                    }),
            }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        # adding styling and attributes to fields
        widgets = {
                'name': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                'description': forms.Textarea(attrs={
                        'class': 'form-control'
                    }),
                'price': forms.TextInput(attrs={
                        'class': 'form-control'
                    }),
                'image': forms.FileInput(attrs={
                        'class': 'form-control'
                    }),
              
            }


