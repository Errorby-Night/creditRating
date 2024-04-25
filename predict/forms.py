from django import forms


class CreditCardForm(forms.Form):
    acc_choices = (
        (0, '0'),
        (1, 'Less than 200'),
        (3, 'Over 200'),
        (2, 'No Account')
    )

    history_choices = (
        (4, 'Critical'),
        (2, 'Duly Paid Till Now'),
        (3, "Delayed"),
        (1, 'Bank Paid Duly Paid Till Now'),
    )

    purpose_choices = (
        (6, 'Radio / TV'),
        (2, 'Education'),
        (3, 'Furniture'),
        (4, 'New Car'),
        (9, 'Used Car'),
        (0, 'Business'),
        (1, 'Domestic Appliances'),
        (7, 'Repairs'),
        (5, 'Others'),
        (8, 'Retraining')
    )

    balance_choices = (
        (1, 'Less than 100'),
        (2, 'Less than 500'),
        (0, 'Less than 1000'),
        (3, 'Over 1000'),
        (4, 'Unknown'),
    )

    employment_choices = (
        (2, 'Over seven years'),
        (3, 'Seven years'),
        (0, 'Four years'),
        (1, 'One year'),
        (4, 'Unemployed'),
    )

    MARITAL_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    real_estate_choices = (
        (3, 'Real Estate'),
        (0, 'Building Society'),
        (2, 'None'),
        (1, 'Car')
    )
    other_installment_choices = (
        (0, 'Bank'),
        (2, 'Stores'),
        (1, 'None')
    )
    job_choices = (
        (1, 'Skilled'),
        (3, 'Unskilled - Resident'),
        (0, 'Management'),
        (2, 'Unemployed Non Resident')
    )
    phone_choices = (
        (0, 'No'),
        (1, 'Yes')
    )

    foreign_choices = (
        (0, 'No'),
        (1, 'Yes')
    )

    acc_type = forms.ChoiceField(choices=acc_choices, widget=forms.Select(attrs={'class': 'acc_type'}), required=True, label='Account Type')
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'duration'}), min_value=0, max_value=72, required=True, label='Duration')
    history = forms.ChoiceField(choices=history_choices, widget=forms.Select(attrs={'class': 'history'}), required=True, label='History')
    purpose = forms.ChoiceField(choices=purpose_choices, widget=forms.Select(attrs={'class': 'purpose'}), required=True, label='Purpose')
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'amount'}), required=True, label='Amount')
    balance = forms.ChoiceField(choices=balance_choices, widget=forms.Select(attrs={'class': 'balace'}), required=True, label='Balance')
    employment = forms.ChoiceField(choices=employment_choices, widget=forms.Select(attrs={'class': 'emp'}), required=True, label='Employment')
    rate = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'rate'}), required=True, label='Rate')
    marital_status = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'marital_status'}),
        choices=MARITAL_CHOICES,
        required=True,
        label='Marital Status'
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={'class': 'gender'}),
        choices=GENDER_CHOICES,
        required=True, label='Gender'
    )
    real_estate = forms.ChoiceField(choices=real_estate_choices, widget=forms.Select(attrs={'class': 'real-estate'}), required=True, label='Real Estate')
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'age'}), required=True, label='Age')
    other_installment = forms.ChoiceField(choices=other_installment_choices, widget=forms.Select(attrs={'class': 'other-installment'}), required=True, label='Other Installments')
    job = forms.ChoiceField(choices=job_choices, widget=forms.RadioSelect(attrs={'class': 'job'}), required=False, label='Job')
    num_credits = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'num-credits'}), required=True, label='Credits')
    phone = forms.ChoiceField(choices=phone_choices, widget=forms.Select(attrs={'class': 'phone'}), required=True, label='Phone')
    foreign = forms.ChoiceField(choices=foreign_choices, widget=forms.Select(attrs={'class': 'foreign'}), required=True, label='Foreign Assets')



