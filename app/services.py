import json
from typing import List

# تحميل بيانات الزبائن من JSON
def get_customers() -> List[dict]:
    with open("app/data/customers.json", "r") as f:
        return json.load(f)

# حساب أهلية القرض
def calculate_loan_eligibility(customer: dict) -> float:
    if 25 <= customer["Age"] <= 60 and customer["CreditScore"] > 600:
        max_loan = (customer["AnnualIncome"] * 0.5) - (customer["ExistingLoans"] * 0.7)
        return max(0, max_loan)
    else:
        return 0
