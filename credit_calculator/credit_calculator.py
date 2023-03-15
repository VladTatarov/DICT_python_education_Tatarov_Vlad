"""A loan calculator program that helps calculate loan payments and other information based on user input.
The program supports two types of payment options: annuity and differentiated (diff).
The user can input the loan principal amount, number of payment periods, interest rate,
and payment amount (if known) to calculate the remaining values"""

# Libraries
import math
import argparse
import sys


def diff_payment(principal: float, periods: int, interest: float, payments: float) -> tuple[float, int, float, float]:
    """Determines which type of payment is chosen and returns the corresponding calculated values"""
    if args.type == 'diff' and principal > 0 and periods > 0 and interest > 0:
        return diff_payment_func(interest, principal, periods)

    if args.type == 'annuity' and payments is not None and principal is not None and interest is not None:
        return number_of_monthly_payments_func(interest, payments, principal)

    elif args.type == 'annuity' and periods is not None and payments is not None and interest is not None:
        return loan_principal_func(periods, payments, interest)

    elif args.type == 'annuity' and periods is not None and principal is not None \
            and args.interest is not None:
        return annuity_monthly_payment_amount_func(periods, principal, interest)

    # default return statement
    return 0.0, 0, 0.0, 0.0


def diff_payment_func(interest: float, principal: float, periods: int) -> tuple[float, int, float, float]:
    """Calculates and returns the values for a differentiated payment."""
    i = interest / (12 * 100)
    diff_whole = 0
    for x in range(1, args.periods + 1):
        diff_amount = math.ceil((principal / periods) + i * (
                principal - (principal * (x - 1) / periods)))
        diff_whole += diff_amount
        print(f'Month: {x} paid out {diff_amount}')
    overpayment = diff_whole - principal
    print(f'Overpayment: {overpayment}')
    return i, periods, diff_whole, overpayment


def number_of_monthly_payments_func(interest: float, payments: float, principal: float) \
        -> tuple[float, int, float, float]:
    """Calculates and returns the values for the number of monthly payments"""
    i = interest / (12 * 100)
    months = math.ceil(
        math.log(payments / (payments - i * principal), (1 + i)))
    overpayment = months * payments - principal
    years = months // 12
    months = months % 12

    if months == 0:
        print(f'You need {years}, years to repay this credit!')
    elif years == 0:
        print(f'You need {months}, months to repay this credit!')
    else:
        print(f'You need {years} years and {months} months to repay this credit!')
    print(f'Overpayment = {overpayment}')
    return months, years, i, overpayment


def annuity_monthly_payment_amount_func(periods: int, principal: float, interest: float) \
        -> tuple[float, int, float, float]:
    """Calculates and returns the values for the annuity monthly payment amount"""
    i = interest / (12 * 100)
    value = (i * math.pow(1 + i, periods)) / (
            math.pow(1 + i, periods) - 1)
    monthly_payment = principal * value
    overpayment = abs(periods * math.ceil(monthly_payment) - principal)
    monthly_payment = math.ceil(monthly_payment)
    print(f'Your annuity payment = {monthly_payment}!')
    print(f'Overpayment = {overpayment}')
    return monthly_payment, periods, i, overpayment


def loan_principal_func(periods: int, payments: float, interest: float) -> tuple[float, int, float, float]:
    """Calculates and returns the values for the loan principal amount"""
    i = interest / (12 * 100)
    value = (i * math.pow(1 + i, periods)) / (
            math.pow(1 + i, periods) - 1)
    credit_principal = int(payments / value)
    overpayment = periods * payments - credit_principal
    print(f'Your credit principal = {str(credit_principal)}!')
    print(f'Overpayment = {overpayment}')
    return credit_principal, periods, i, overpayment


if __name__ == '__main__':
    """
This is a command-line tool for calculating different types of loan payments: annuity or differentiated. 
The user must provide some input parameters depending on the type of payment. The available input parameters are:

--type: the type of payment. Allowed values are 'annuity' or 'diff' (differentiated).
--principal: the loan principal amount.
--periods: the number of payment periods (months).
--interest: the loan interest rate (as a percentage).
--payment: the monthly payment amount.

If the user specifies the --type parameter as 'diff', they must not provide the --payment parameter. 
If the user specifies the --type parameter as 'annuity', they must provide either the --payment parameter 
or both the --principal and --periods parameters.
If any of the input parameters is missing or invalid, the script will print an error message 
and exit with a non-zero status code.

Usage examples:

- Calculate the annuity payment for a loan of $10000 with an interest rate of 10% and a 24-month term:
    python credit_calculator.py --type=annuity --principal=10000 --periods=24 --interest=10

- Calculate the differentiated payments for a loan of $10000 with an interest rate of 10% and a 24-month term:
    python credit_calculator.py --type=diff --principal=10000 --periods=24 --interest=10
"""
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument('--type', choices=['annuity', 'diff'], help='type of payment (annuity or differentiated)')
    parser.add_argument('--principal', type=float, help='the loan principal amount')
    parser.add_argument('--periods', type=int, help='the number of payment periods')
    parser.add_argument('--interest', type=float, help='the loan interest rate')
    parser.add_argument('--payment', type=float, help='the monthly payment amount')

    args = parser.parse_args()

    if args.payment is None:
        payment = 'None'
    else:
        payment = args.payment
    if args.type is None or args.type not in ['annuity', 'diff']:
        print('Incorrect parameters')
        exit()
    elif args.type == 'annuity' and (args.principal is None or args.periods is None or args.interest is None):
        print('Incorrect parameters')
        parser.print_usage()
        sys.exit()
    elif args.type == 'diff' and not math.isnan(args.payment):
        print('Incorrect parameters')
        exit()
    elif args.type != 'annuity' and args.type != 'diff':
        print('Incorrect parameters')
    elif args.type == 'diff' and args.payment is not None:
        print('Incorrect parameters')
    elif not args.interest or any(val is None or val < 0 for val in (args.principal, args.periods)):
        print('Incorrect parameters')
    elif args.type == 'annuity' and args.payment is None:
        print('Incorrect parameters')
    elif args.principal is not None and args.periods is not None:
        if not isinstance(args.principal, (int, float)) or not isinstance(args.periods, (int, float)):
            raise ValueError('`principal` and `periods` must be numbers')
    elif args.type == 'annuity' and math.isnan(args.payment) and (args.principal is None or args.periods is None):
        raise ValueError('Both `principal` and `periods` are required for annuity calculation')
    elif (not math.isnan(payment) and payment < 0) or (args.principal and args.principal < 0) or \
            (args.periods and args.periods < 0) or (args.interest and args.interest < 0):
        print('Incorrect parameters')
        exit()
    else:
        diff_payment(args.principal, args.periods, args.interest, payment)
