from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder": "todo title",
            "class": "form-control"
        }
    ))
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            "placeholder": "todo description",
            "rows": 2,
            "cols":120,
            "class": "form-control"
        }
    ))
    class Meta:
        model = Todo
        fields = [
            "title",
            "text"
        ]