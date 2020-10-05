import pandas as pd

def treat_missingval(data:pd.DataFrame) -> pd.DataFrame:
    data['Gender'] = data['Gender'].fillna( data['Gender'].dropna().mode().values[0] )
    data['Married'] = data['Married'].fillna( data['Married'].dropna().mode().values[0] )
    data['Dependents'] = data['Dependents'].fillna( data['Dependents'].dropna().mode().values[0] )
    data['Self_Employed'] = data['Self_Employed'].fillna( data['Self_Employed'].dropna().mode().values[0] )
    data['LoanAmount'] = data['LoanAmount'].fillna( data['LoanAmount'].dropna().mean() )
    data['Loan_Amount_Term'] = data['Loan_Amount_Term'].fillna( data['Loan_Amount_Term'].dropna().mode().values[0] )
    data['Credit_History'] = data['Credit_History'].fillna( data['Credit_History'].dropna().mode().values[0] )
    data['Dependents'] = data['Dependents'].str.rstrip('+')

    return data
