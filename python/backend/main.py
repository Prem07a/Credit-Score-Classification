import uvicorn
import pandas as pd
import joblib
from fastapi import FastAPI, Request, Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .schemas import Data

app = FastAPI()
templates = Jinja2Templates(directory="python/frontend/templates")
app.mount("/static", StaticFiles(directory="python/frontend/static"), name="static")

@app.get("/")
async def get_form(request: Request):
    """
    Render the main form page.

    Args:
        request (Request): FastAPI Request object.

    Returns:
        TemplateResponse: HTML template response.
    """
    return templates.TemplateResponse("credit.html", {"request": request})

@app.post('/credit')
async def predict(request: Request, 
                  Annual_Income:float=Form(...),
                  Monthly_Inhand_Salary:float=Form(...),
                  Num_Bank_Accounts:int=Form(...),
                  Num_Credit_Card:int=Form(...),
                  Interest_Rate:int=Form(...),
                  Num_of_Loan:float=Form(...),
                  Delay_from_due_date:int=Form(...),
                  Num_of_Delayed_Payment:float=Form(...),
                  Credit_Mix:int=Form(...),
                  Outstanding_Debt:float=Form(...),
                  Credit_History_Year:int=Form(...),
                  Monthly_Balance:float=Form(...)
                  ):
    """
    Predict credit score based on user input.

    Args:
        request (Request): FastAPI Request object.
        data (Data): Form data from the user.

    Returns:
        TemplateResponse: HTML template response with the predicted credit score.
    """
    df = {
    "Annual_Income": [Annual_Income],
    "Monthly_Inhand_Salary": [Monthly_Inhand_Salary],
    "Num_Bank_Accounts": [Num_Bank_Accounts],
    "Num_Credit_Card": [Num_Credit_Card],
    "Interest_Rate": [Interest_Rate],
    "Num_of_Loan": [Num_of_Loan],
    "Delay_from_due_date": [Delay_from_due_date],
    "Num_of_Delayed_Payment": [Num_of_Delayed_Payment],
    "Credit_Mix": [Credit_Mix],
    "Outstanding_Debt": [Outstanding_Debt],
    "Credit_History_Year": [Credit_History_Year],
    "Monthly_Balance": [Monthly_Balance]
}

    df = pd.DataFrame(df)
    model = joblib.load("./model/clf.joblib")
    credit_Score = int(model.predict(df)[0])
    score = {0: "Good", 1: "Standard", 2: "Poor"}
    Credit_Grade = score[credit_Score]
    return templates.TemplateResponse("score.html", {"request": request, "cs": Credit_Grade})

@app.get('/resume')
async def resume(request: Request):
    """
    Render the resume page.

    Args:
        request (Request): FastAPI Request object.

    Returns:
        TemplateResponse: HTML template response for the resume page.
    """
    return templates.TemplateResponse("resume.html", {"request": request})

@app.get('/hire')
async def hire_me(request: Request):
    """
    Render the hire me page.

    Args:
        request (Request): FastAPI Request object.

    Returns:
        TemplateResponse: HTML template response for the hire me page.
    """
    return templates.TemplateResponse("hire.html", {"request": request})

@app.post('/thankyou')
async def sendMail(request: Request, Name:str=Form(...), Email:str=Form(...), Message:str = Form(...)):
    with open(f"data/Mail/info.txt", "a") as f:
        f.write(f"\n\nName: {Name}\n")
        f.write(f"Email: {Email}\n")
        f.write(f"Message:\n{Message}\n")
    return templates.TemplateResponse("thankyou.html", {"request": request})    


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
