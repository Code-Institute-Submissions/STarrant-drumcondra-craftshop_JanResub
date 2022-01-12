from django import forms
from .models import Item, Product, Creator, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0' # testhigh adjust style


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        categories = Category.objects.all()
        category_names = [(c.id, c.get_category_name()) for c in categories]
        self.fields['category_id'].choices = category_names

        creators = Creator.objects.all()
        creator_names = [(c.id, c.get_creator_name()) for c in creators]
        self.fields['creator_id'].choices = creator_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

