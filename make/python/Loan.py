
'''
Title: Loan.py
Created: 2022-10-11 21:18:55
Encoding: UTF-8
@author: samantix
'''

import math


class Loan(object):
    # + ------------------WORKING-------------------- +
    def __init__(self, principal, annualInterestRate, monthlyPaymentRate):
        self.principal = principal
        self.annual_int_rate = annualInterestRate
        self.monthly_pmt_rate = monthlyPaymentRate
        self.annual_months = 12
        self.monthly_int_rate = self.annual_int_rate / self.annual_months
        self.month_of_pmt = 0

    # @ ------------------UNTESTED------------------- @
    def get_balance(self):
        return self.calc_balance()

    # @ ------------------UNTESTED------------------- @
    def __str__(self):
        # return "Remaining balance: " + str(self.calc_balance)
        return str(self.calc_balance())

    # + ------------------WORKING-------------------- +
    def round_up(self, x, factor=1):
        res = math.ceil(x / factor) * factor
        return res

    # + ------------------WORKING-------------------- +
    def round_down(self, x, factor=1):
        res = math.floor(x / factor) * factor
        return res

    # @ ------------------UNTESTED------------------- @
    def update_balance(self, OLB, min_monthly_pmt):
        int_rate = self.monthly_int_rate
        TMP = min_monthly_pmt
        # outstanding loan balance
        OLB = (OLB - TMP) + (OLB - TMP) * int_rate
        return OLB

    # @ ------------------UNTESTED------------------- @
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

    # + ------------------WORKING-------------------- +
    def amortize(self, years_of_payment=1):
        '''
        # * assumes: payments are factors of 10, interest is compounded monthly
        # * returns: lowest estimated monthly payment (float); and total accrued interest (float)
        '''
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
        return EMI, total_accrued_interest

# ----------------------------------------------------------
    # ! -----------------ERRONEOUS------------------ !
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

    # + ------------------WORKING-------------------- +

    def amortize_10x(self, term=1):
        '''
        # * assumes: payments are factors of 10, interest is compounded monthly
        # * returns: lowest fixed monthly payment to clear loan balance
        '''
        total_installments = term * 12
        monthly_int_rate = self.annual_int_rate / 12
        # start at a reasonable estimated monthly installment (EMI)
        x = self.principal / total_installments
        # assume payments must be a factor of 10
        EMI = self.round_down(x, 10)
        if self.principal - EMI*10 > 0:
            updated_balance = self.principal - EMI
            while updated_balance > 0:
                EMI += 10
                updated_balance = self.principal
                for installment in range(total_installments):
                    updated_balance -= EMI
                    # add interest (monthly_int_rate * updated_balance)
                    updated_balance += monthly_int_rate * updated_balance
                updated_balance = round(updated_balance, 2)
        total_accrued_interest = round(12*EMI*term-self.principal, 2)
        return EMI, total_accrued_interest

# ----------------------------------------------------------
    # + ------------------WORKING-------------------- +
    def get_amortization(self, total_installments=12):
        EMI, total_interest = self.amortize()
        print("Amortization method: standard formula")
        print(f"Original principal: ${self.principal}")
        print(f"Min monthly payment: ${EMI}")
        print(f"Total accrued interest: ${total_interest}")
        print(f"Total to be paid: ${EMI * total_installments}")

# ----------------------------------------------------------
    # + ------------------WORKING-------------------- +
    def get_amortization_10x(self, total_installments=12):
        EMI, total_interest = self.amortize_10x()
        print("Amortization method: factor 10")
        print(f"Original principal: ${self.principal}")
        print(f"Min monthly payment: ${EMI}")
        print(f"Total accrued interest: ${total_interest}")
        print(f"Total to be paid: ${EMI * total_installments}")
# ----------------------------------------------------------
    # + ------------------WORKING-------------------- +

    def get_min_amortization(self):
        EMI_a, total_interest_a = self.amortize()
        EMI_b, total_interest_b = self.amortize_10x()
        if EMI_a <= EMI_b:
            print("Best amortization: amortize")
            return self.get_amortization()
        else:
            print("Best amortization: amortize_10x")
            return self.get_amortization_10x()
# ----------------------------------------------------------
# @ --------------------------------------------- @
# @                   TESTING                     @
# @ --------------------------------------------- @


principal = 619  # 4800
annualInterestRate = 0.18  # 0.15
monthlyPaymentRate = 0.04
term = 1
total_installments = 12
# ----------------------------------------------------------
print("\n***Testing 'get_amortization' & 'amortize'***\n")
Loan(principal, annualInterestRate,
     monthlyPaymentRate).get_amortization(total_installments)

print("\n***Testing 'get_amortization_10x' & 'amortize_10x'***\n")

Loan(principal, annualInterestRate,
     monthlyPaymentRate).get_amortization_10x(total_installments)

print("\n***Testing 'get_min_amortization'***\n")

Loan(principal, annualInterestRate,
     monthlyPaymentRate).get_min_amortization()

print("\n***Testing 'amortize_10'***\n")

print(Loan(principal, annualInterestRate, monthlyPaymentRate).amortize_10())
