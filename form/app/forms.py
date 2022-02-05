from django import forms
from .models import Student

class insert_student1(forms.Form):
    studentname = forms.CharField(max_length=100)
    studentemail = forms.EmailField(max_length=100)
    studentage = forms.IntegerField()
    trackname = forms.CharField(max_length=100)


class insert_student2(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
