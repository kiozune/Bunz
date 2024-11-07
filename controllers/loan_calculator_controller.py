from flask import Blueprint, render_template, flash, request
from models import Calculator

loan_calculator_bp = Blueprint('loan_calculator', __name__)

class LoanCalculatorController:
    @staticmethod
    @loan_calculator_bp.route('/loan_calculator', methods=['GET', 'POST'])
    def loan_calculator():
        if request.method == 'POST':
            principal = int(request.form.get('principal').strip())
            interest_rate = int(request.form.get('interest_rate').strip())
            years = int(request.form.get('years').strip())

            try:
                cal = Calculator(principal, interest_rate, years)
                result = cal.calculate_loan(principal, interest_rate, years)
                return render_template('loan_calculator.html', result=result)
            except ValueError as e:
                # Flash the error message to notify the users
                flash(str(e), 'danger')
                return render_template('loan_calculator.html', principal=principal,
                                       interest_rate=interest_rate, years=years)
        return render_template('loan_calculator.html')
