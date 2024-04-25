from django.shortcuts import render, redirect
from .forms import CreditCardForm
import pickle
import pandas as pd


def index(request):
    print("Pre Post")
    if request.method == 'POST':
        print("Post Post")
        form = CreditCardForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            acc_type = float(form.cleaned_data['acc_type'])
            print(acc_type)
            duration = float(form.cleaned_data['duration'])
            history = float(form.cleaned_data['history'])
            purpose = float(form.cleaned_data['purpose'])
            amount = float(form.cleaned_data['amount'])
            balance = float(form.cleaned_data['balance'])
            employment = float(form.cleaned_data['employment'])
            rate = float(form.cleaned_data['rate'])
            marital_status = form.cleaned_data['marital_status']
            gender = form.cleaned_data['gender']
            real_estate = form.cleaned_data['real_estate']
            age = float(form.cleaned_data['age'])
            other_installment = float(form.cleaned_data['other_installment'])
            job = float(form.cleaned_data['job'])
            num_credits = float(form.cleaned_data['num_credits'])
            phone = float(form.cleaned_data['phone'])
            foreign = float(form.cleaned_data['foreign'])

            genandmar = 0.0
            if gender == 'male' and marital_status == 'single':
                genandmar = 3.0
            elif gender == 'male' and marital_status == 'divorced':
                genandmar = 1.0
            elif gender == 'male' and marital_status == 'married':
                genandmar = 2.0
            elif gender == 'female' and marital_status == 'divorced':
                genandmar = 0.0

            data = {
                'CHK_ACCT': [acc_type],
                'Duration': [duration],
                'History': [history],
                'Purpose of credit': [purpose],
                'Credit Amount': [amount],
                'Balance in Savings A/C': [balance],
                'Employment': [employment],
                'Install_rate': [rate],
                'Marital status': [genandmar],
                'Real Estate': [real_estate],
                'Age': [age],
                'Other installment': [other_installment],
                'Num_Credits': [num_credits],
                'Job': [job],
                'Phone': [phone],
                'Foreign': [foreign]
            }
            df = pd.DataFrame(data)
            pred = make_prediction(df)[0]
            if pred == 0:
                prediction = 'Good'
            else:
                prediction = 'Bad'
            return render(request, 'predict/success.html', {'prediction': prediction})
    else:
        form = CreditCardForm()
    return render(request, 'predict/index.html', {'form': form})


def make_prediction(variables):
    prediction = 0
    with open('predict/model.pkl', 'rb') as file:
        model = pickle.load(file)
        print("Model loaded successfully")
        prediction = model.predict(variables)
        print("Prediction made:", prediction)
    return prediction
