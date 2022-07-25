from django.forms import ModelForm
from .models import View

class ViewForm(ModelForm):
  class Meta:
    model = View
    fields = ['date', 'time']