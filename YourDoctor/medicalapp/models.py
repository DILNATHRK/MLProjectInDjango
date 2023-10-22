from django.db import models

# Create your models here.
class DepartmentPredict(models.Model):
    stomach_pain_and_acidity = models.CharField(max_length=50)
    vomiting = models.CharField(max_length=50)
    cough = models.CharField(max_length=50)
    fever = models.CharField(max_length=50)
    breathlessness = models.CharField(max_length=50)
    indigestion = models.CharField(max_length=50)
    headache = models.CharField(max_length=50)
    abdominal_pain = models.CharField(max_length=50)
    diarrhoea = models.CharField(max_length=50)
    runny_nose = models.CharField(max_length=50)
    chest_pain = models.CharField(max_length=50)
    fast_heart_rate = models.CharField(max_length=50)
    dizziness = models.CharField(max_length=50)
    stiff_neck = models.CharField(max_length=50)
    loss_of_balance = models.CharField(max_length=50)
    altered_sensorium = models.CharField(max_length=50)
    belly_pain = models.CharField(max_length=50)
    watering_from_eyes = models.CharField(max_length=50)
    DEPARTMENT = models.CharField(max_length=50)