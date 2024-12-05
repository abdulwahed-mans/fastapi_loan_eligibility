# FastAPI Loan Eligibility API

A FastAPI-based project for managing customer loan eligibility data, calculating maximum loan eligibility, and generating loan eligibility charts.

## Features

- **Customer Data Management**: Retrieve customer financial data.
- **Loan Eligibility Calculation**: Determine the maximum loan a customer is eligible for.
- **Chart Generation**: Generate a bar chart visualizing loan eligibility for all customers.

## Project Structure

```
fastapi_loan_eligibility/
├── app/
│   ├── main.py          # Main FastAPI application
│   ├── models.py        # Data models and schemas
│   ├── services.py      # Business logic for loan calculation
│   ├── chart.py         # Chart generation logic
│   └── data/            # Folder for data files
│       └── customers.json # Customer financial data
└── requirements.txt     # Project dependencies
```

## Prerequisites

- Python 3.10 or higher
- pip

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/abdulwahed-mans/fastapi_loan_eligibility.git
   cd fastapi_loan_eligibility
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   ```

   - **Activate the virtual environment**:
     - **Windows**:
       ```bash
       env\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source env/bin/activate
       ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the API**: Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Endpoints

| Endpoint                      | Method | Description                                  |
| ----------------------------- | ------ | -------------------------------------------- |
| /                             | GET    | Welcome message                              |
| /customers/                   | GET    | List all customers and their financial data  |
| /customers/{customer_id}/loan | GET    | Get maximum loan eligibility for a customer  |
| /chart/                       | GET    | Generate and save the loan eligibility chart |

## Data Example

Sample customer data in `app/data/customers.json`:

```json
[
  {
    "CustomerID": 1,
    "Name": "Customer 1",
    "Age": 48,
    "AnnualIncome": 872315,
    "CreditScore": 402,
    "ExistingLoans": 469580
  },
  {
    "CustomerID": 2,
    "Name": "Customer 2",
    "Age": 30,
    "AnnualIncome": 635410,
    "CreditScore": 638,
    "ExistingLoans": 387857
  },
  {
    "CustomerID": 3,
    "Name": "Customer 3",
    "Age": 57,
    "AnnualIncome": 572127,
    "CreditScore": 600,
    "ExistingLoans": 153948
  }
]
```

## Chart Generation

The `/chart/` endpoint generates a bar chart of loan eligibility for all customers and saves it as `loan_eligibility_chart.png` in the project root.

## Dependencies

- **FastAPI**: For building the API
- **Uvicorn**: ASGI server for running the FastAPI app
- **Matplotlib**: For generating charts

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running Tests

To ensure everything is working as expected, you can write and run tests using `pytest` (optional).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Repository

You can find the project repository at: [https://github.com/abdulwahed-mans/fastapi_loan_eligibility.git](https://github.com/abdulwahed-mans/fastapi_loan_eligibility.git)
