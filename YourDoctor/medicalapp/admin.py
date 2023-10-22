from django.contrib import admin

# Register your models here.
from .models import DepartmentPredict
# Register your models here.
class DepartmentPredictAdmin(admin.ModelAdmin):
    list_display = ('stomach_pain_and_acidity','vomiting','cough',
                    'fever','breathlessness','indigestion','headache',
                    'abdominal_pain','diarrhoea','runny_nose','chest_pain','fast_heart_rate',
                    'dizziness','stiff_neck','loss_of_balance','altered_sensorium',
                    'belly_pain','watering_from_eyes','DEPARTMENT')
    list_filter = ('DEPARTMENT',)

admin.site.register(DepartmentPredict,DepartmentPredictAdmin)