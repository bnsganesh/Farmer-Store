from django import forms
from django.forms import ModelForm
from .models import Order, Product


class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'
        
class ProductForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Ice-Cream','id':'name', 'name':'name','class':'inputStyle'}), label="", required=True)
    price=forms.DecimalField(widget=forms.NumberInput(attrs={'type':'number','placeholder':'12.25','id':'price', 'name':'price','class':'inputStyle'}), label="", required=True)
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={'type':'file','accept':'image','id':'image','name':'image',}), label="", required=False)
    
    slot=forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number','placeholder':'1','id':'slot', 'name':'slot','class':'inputStyle'}), label="", required=True)
    stock=forms.IntegerField(widget=forms.NumberInput(attrs={'type':'number','placeholder':'25','id':'stock', 'name':'stock','class':'inputStyle'}), label="", required=True)
    desc=forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'Nutrients','id':'desc', 'name':'desc','class':'inputStyle'}), label="", required=False)
    netwt=forms.CharField(widget=forms.TextInput(attrs={'type':'text','placeholder':'1 Kg','id':'netwt', 'name':'netwt','class':'inputStyle'}), label="", required=True)
    
    class Meta:
        model = Product
        fields = ['name','price','image','slot','stock','desc','netwt']
    
    #Validation
    def clean_slot(self):
        input_slot = self.cleaned_data['slot']
        slots = Product.objects.all()
        for slot in slots:
            if slot.slot == input_slot:
                raise forms.ValidationError("Slot already Exist!")
        return input_slot