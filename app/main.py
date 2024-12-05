from fastapi import FastAPI
from app.models import Customer
from app.services import calculate_loan_eligibility, get_customers
from app.chart import generate_chart

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Loan Eligibility API"}

@app.get("/customers/")
def list_customers():
    customers = get_customers()
    return {"customers": customers}

@app.get("/customers/{customer_id}/loan")
def customer_loan_eligibility(customer_id: int):
    customers = get_customers()
    customer = next((c for c in customers if c["CustomerID"] == customer_id), None)
    if not customer:
        return {"error": "Customer not found"}
    loan_eligibility = calculate_loan_eligibility(customer)
    return {"customer_id": customer_id, "max_loan": loan_eligibility}

@app.get("/chart/")
def get_chart():
    generate_chart()
    return {"message": "Chart generated and saved as loan_eligibility_chart.png"}
