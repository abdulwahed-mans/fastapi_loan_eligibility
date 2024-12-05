import matplotlib.pyplot as plt
from app.services import get_customers, calculate_loan_eligibility

# توليد الرسم البياني
def generate_chart():
    customers = get_customers()
    names = [c["Name"] for c in customers]
    max_loans = [calculate_loan_eligibility(c) for c in customers]

    plt.figure(figsize=(10, 6))
    plt.bar(names, max_loans, color="skyblue")
    plt.title("Maximum Loan Eligibility per Customer", fontsize=16)
    plt.xlabel("Customer Name", fontsize=14)
    plt.ylabel("Max Loan Eligibility (SEK)", fontsize=14)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("loan_eligibility_chart.png")
    plt.close()
