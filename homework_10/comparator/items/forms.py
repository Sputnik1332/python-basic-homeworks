from django.forms import ModelForm, CharField
from django.forms.widgets import Widget
from .models import Item


class ItemCreateForm(ModelForm):
    class Meta:
        model = Item
        fields = "name", "url", "description", "price"

    name = CharField(max_length=20, label="Item name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"