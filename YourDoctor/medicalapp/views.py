from pydoc import text
from django.shortcuts import render
import pandas as pd 
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import accuracy_score
from .models import DepartmentPredict
from django.core.paginator import Paginator
import os
import sklearn
import joblib


def home(request):
    return render(request, "home.html")

def predict(request):
    return render(request, "predict.html")

def result(request):
    model = joblib.load('medical_app_model.joblib')    
    if request.method == "POST":
        n1 = str(request.POST['n1'])
        n2 = str(request.POST['n2'])
        n3 = str(request.POST['n3'])
        n4 = str(request.POST['n4'])
        n5 = str(request.POST['n5'])
        n6 = str(request.POST['n6'])
        n7 = str(request.POST['n7'])
        n8 = str(request.POST['n8'])
        n9 = str(request.POST['n9'])
        n10 = str(request.POST['n10'])
        n11 = str(request.POST['n11'])
        n12 = str(request.POST['n12'])
        n13 = str(request.POST['n13'])
        n14 = str(request.POST['n14'])
        n15 = str(request.POST['n15'])
        n16 = str(request.POST['n16'])
        n17 = str(request.POST['n17'])
        n18 = str(request.POST['n18'])
        for i in n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18:
            if n1==n2==n3==n4==n5==n6==n7==n8==n9==n10==n11==n12==n13==n14==n15==n16==n17==n18:
                result="invalid input"
            else:
                pred = model.predict(np.array([n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,
                    n12,n13,n14,n15,n16,n17,n18]).reshape(1,-1))
                result = ""
                for i in pred:
                    result=i
        data = DepartmentPredict(stomach_pain_and_acidity=n1,
                                vomiting=n2,cough=n3,fever=n4,breathlessness=n5,indigestion=n6,
                                headache=n7,abdominal_pain=n8,diarrhoea=n9,runny_nose=n10,
                                chest_pain=n11,fast_heart_rate=n12,dizziness=n13,stiff_neck=n14,
                                loss_of_balance=n15,altered_sensorium=n16,
                                belly_pain=n17,watering_from_eyes=n18,DEPARTMENT=result)
        data.save()
    return render(request, "predict.html",{"result":result,})

def recordData(request):
    data = DepartmentPredict.objects.all()
    paginator = Paginator(data, 10) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "recordData.html",{"page_obj":page_obj, })