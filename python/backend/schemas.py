from pydantic import BaseModel
from enum import Enum
from fastapi import Form


class Data(BaseModel):
    Annual_Income: float
    Monthly_Inhand_Salary: float
    Num_Bank_Accounts: int
    Num_Credit_Card: int
    Interest_Rate: int
    Num_of_Loan: float
    Delay_from_due_date: int
    Num_of_Delayed_Payment: float
    Credit_Mix: int
    Outstanding_Debt: float
    Credit_History_Year: int
    Monthly_Balance: str

    @classmethod
    def as_form(
        cls,
        annual_income: float = Form(...),
        monthly_inhand_salary: float = Form(...),
        num_bank_accounts: int = Form(...),
        num_credit_card: int = Form(...),
        interest_rate: int = Form(...),
        num_of_loan: float = Form(...),
        delay_from_due_date: int = Form(...),
        num_of_delayed_payment: float = Form(...),
        credit_mix: int = Form(...),
        outstanding_debt: float = Form(...),
        credit_history_year: int = Form(...),
        monthly_balance: str = Form(...)
    ):
        
        return cls(
            Annual_Income=annual_income,
            Monthly_Inhand_Salary=monthly_inhand_salary,
            Num_Bank_Accounts=num_bank_accounts,
            Num_Credit_Card=num_credit_card,
            Interest_Rate=interest_rate,
            Num_of_Loan=num_of_loan,
            Delay_from_due_date=delay_from_due_date,
            Num_of_Delayed_Payment=num_of_delayed_payment,
            Credit_Mix=credit_mix,
            Outstanding_Debt=outstanding_debt,
            Credit_History_Year=credit_history_year,
            Monthly_Balance=monthly_balance
        )