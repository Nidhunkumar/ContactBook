from django import forms
from .models import Contact_details

# Create your forms here.

class ContactsCrationForm(forms.ModelForm):
	class Meta:
		model=Contact_details
		fields=("name","number")
