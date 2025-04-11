from django import forms
from .models import CashFlow, Status, Type, Category, Subcategory

class CashFlowForm(forms.ModelForm):
    date_created = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = CashFlow
        fields = ['date_created', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'type']

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name', 'category']
