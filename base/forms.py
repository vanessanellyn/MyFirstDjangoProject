from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room  # The model that we want to create a form for
        fields = '__all__'  # Include all editable fields of the Django admin
      # fields = ['name', 'body']
