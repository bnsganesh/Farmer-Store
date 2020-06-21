import django_filters
from django import forms
from django_filters import DateFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_ordered", lookup_expr='gte', widget=forms.widgets.DateInput(attrs={'type':'date','id':'start_date', 'name':'start_date'}), label="")
	end_date = DateFilter(field_name="date_ordered", lookup_expr='lte', widget=forms.widgets.DateInput(attrs={'type':'date','id':'end_date', 'name':'end_date'}), label="")


	class Meta:
		model = Order
		fields = ''