# ***************************************************************************
from django.shortcuts import render
from .forms import ApprovalForm
from .models import Approval
from .serializers import ApprovalSerializers
# ***************************************************************************
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib import messages

# ***************************************************************************
from sklearn import preprocessing
import pandas as pd
from keras.models import model_from_json
from rest_framework.decorators import action

# ***************************************************************************
class ApprovalsViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializers

    @action(methods=['get'], detail=False)
    def newest(self, request):
        new = self.get_queryset().order_by('id').last()
        serial = self.get_serializer_class()(new)
        return Response(serial.data)


# @ api_view(["POST"])
def approvereject(request, arr):
    try:
        json_file = open(r'E:\Django\simple_projects\new_ml_django\djangoAPI\myAPI\model.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        mdl = model_from_json(loaded_model_json)
        # load weights into new model
        mdl.load_weights(r"E:\Django\simple_projects\new_ml_django\djangoAPI\myAPI\model.h5")
        # *******************************************************************************

        scaling = pd.read_pickle(r'E:\Django\simple_projects\new_ml_django\djangoAPI\myAPI\scaler.pkl')
        scl = scaling.transform([arr])
        print(scl)
        prediction = mdl.predict(scl)
        prediction = (prediction > 0.5)
        return prediction

    except ValueError as e:
        return e.args[0]


def cxcontact(request):
    if request.method == 'POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            Firstname = form.cleaned_data['firstname']
            Lastname = form.cleaned_data['lastname']
            Dependents = form.cleaned_data['Dependents']
            ApplicantIncome = form.cleaned_data['ApplicantIncome']
            CoapplicantIncome = form.cleaned_data['CoapplicantIncome']
            LoanAmount = form.cleaned_data['LoanAmount']
            Loan_Amount_Term = form.cleaned_data['Loan_Amount_Term']
            Credit_History = form.cleaned_data['Credit_History']
            Gender = form.cleaned_data['Gender']
            Married = form.cleaned_data['Married']
            Education = form.cleaned_data['Education']
            Self_Employed = form.cleaned_data['Self_Employed']
            Property_Area = form.cleaned_data['Property_Area']

            if Gender == 'Female':    # GENDER
                Gender = 0
            else:
                Gender = 1

            if Married == 'Yes':    # MARRIED
                Married = 1
            else:
                Married = 0

            if Education == 'Yes':    # EDUCATION
                Education = 1
            else:
                Education = 0

            if Self_Employed == 'No':    # SELF EMPLOYED
                Self_Employed = 0
            else:
                Self_Employed = 1

            if Property_Area == 'Rural':   # AREA
                Property_Area = 0
            elif Property_Area == 'Semiurban':
                Property_Area = 1
            else:
                Property_Area = 2

            print(Gender, ' ', Married, ' ', Dependents, ' ', Education, ' ', Self_Employed, ' ', ApplicantIncome, ' ',
                  CoapplicantIncome, ' ',
                  LoanAmount, ' ', Loan_Amount_Term, ' ', Credit_History, ' ', Property_Area)

            arr = [Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome,
                   LoanAmount, Loan_Amount_Term, int(Credit_History), Property_Area]

            print(arr)
            ans = approvereject(request, arr)[0][0]
            if ans:
                ans = 'Approved'
            else:
                ans = 'Not Approved'

            # messages.success(request._request, 'Success')
            return render(request, 'apporval.html', {'form': form, 'ans': ans})

    form = ApprovalForm()
    return render(request, 'apporval.html', {'form': form, 'ans': None})

