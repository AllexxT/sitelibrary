from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Введите дату в диапазоне 4х недель(default 3), начиная от текущего дня.")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Проверка того, что дата не выходит за "нижнюю" границу (не в прошлом). 
        if data < datetime.date.today():
            raise ValidationError(_('Неверная дата - значение в прошедшем времени'))

        #Проверка того, то дата не выходит за "верхнюю" границу (+4 недели).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Неверная дата - значение выходит за границу диапазона в 4 недели'))

        # Помните, что всегда надо возвращать "очищенные" данные.
        return data