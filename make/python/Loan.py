
'''
Title: Loan.py
Created: 2022-10-11 21:18:55
Encoding: UTF-8
@author: samantix
'''

import math


class Loan(object):
    def __init__(self, principal, annualInterestRate, monthlyPaymentRate):
        self.principal = principal
        self.annual_int_rate = annualInterestRate
        self.monthly_pmt_rate = monthlyPaymentRate
        self.annual_months = 12
        self.monthly_int_rate = self.annual_int_rate / self.annual_months
        self.month_of_pmt = 0

    def get_balance(self):
        return self.calc_balance()

    def __str__(self):
        # return "Remaining balance: " + str(self.calc_balance)
        return str(self.calc_balance())

    def update_balance(self, OLB, min_monthly_pmt):
        int_rate = self.monthly_int_rate
        TMP = min_monthly_pmt
        # outstanding loan balance
        OLB = (OLB - TMP) + (OLB - TMP) * int_rate
        return OLB

    def calc_balance(self):
        OLB = self.principal  # outstanding loan balance
        TMP_rate = self.monthly_pmt_rate
        year = range(self.annual_months)
        min_monthly_pmt = 0
        # ---------------------------------------------------
        for month in year:
            min_monthly_pmt = OLB * TMP_rate
            OLB = self.update_balance(OLB, min_monthly_pmt)
            #month += 1
        return round(OLB, 2)

    def amortize_10(self, required_months_of_payment=12):
        # compounded
        P = self.principal
        i = self.monthly_int_rate
        required_payments = required_months_of_payment
        # Estimated monthly installments (payment)
        EMI = 10
        dP = P - 10

        while dP > 0:
            EMI += 10
            dP = P
            months_paid = 0   # month

            while months_paid < required_payments and dP > 0:
                dP -= EMI
                I = self.monthly_int_rate * dP   # interest
                dP += I
                months_paid += 1
            dP = round(dP, 2)
        return EMI

        #print("Lowest Payment: " + str(EMI))
# ----------------------------------------------------------
    def amortize(self, years_of_payment):
        annualInterestRate = 0.2
        P = self.principal
        r = self.annual_int_rate
        t = years_of_payment
        n = 12                         # payments/month/year
        # ----------------------------------------------------------
        rP = r*P
        nt = n*t
        rn1 = 1+(r/n)
        # Estimated monthly installment (EMI)
        EMI = round(rP / (n*(1-(rn1)**(-nt))), 2)
        total_accrued_interest = round(n*EMI*t-P, 2)
        # ----------------------------------------------------------
        print(f"Original principal: ${P}")
        print(f"Min monthly payment: ${EMI}")
        print(f"Total accrued interest: ${total_accrued_interest}")
        print(f"Total to be paid: ${EMI * n}")
# ----------------------------------------------------------

# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @


principal = 3329
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
term = 1

print("\n***Testing 'amortize'***\n")
Loan(principal, annualInterestRate, monthlyPaymentRate).amortize(term)
print("\n***Testing 'amortize_10'***\n")
print(Loan(principal, annualInterestRate, monthlyPaymentRate).amortize_10())
