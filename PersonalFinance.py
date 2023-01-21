# Developer: Roger De Four
# Category: Personal Finance

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class PersonalFinance:
    """
        date: 2022-12-15 15:50
        description: a class that a user can use to manage their pesonal finances
    """

    def __init__(self):
        pass

    def ISP():
        """
        Date: 2022-12-15 15:21

        Description:  developed just for the practice - to calculate
        the cost of adopting an Internet Service Provider (ISP)


        """

        service_charge = 0.00  # installation charge (enter relevant value)
        rental = 0.00  # monthly charge - to be paid up front
        total_cost = service_charge + rental  # Expected total cost

        resp = "The expected cost of setting up {0} as my ISP is ${1}: "

        isp_possible_choice = "a.n isp_"
        print("\n")

        return resp.format(isp_possible_choice , total_cost)

    def expense_analysis ():

        df_all_expenses = pd.read_csv(r"DRIVE:Location\of\expense_file\personal_expense_analysis.csv") ## the 'r' command was just included as the script was developed on a WIdows machine; so adopt as per required by your OS

        # df_sample = df_all_expenses.head()
        # print(df_all_expenses.sort_values(by=['LogID'] , ascending=True))

        def_expense_report = df_all_expenses[['LogID', 'BudgetCategory', 'Description', 'AmountSpent']] ## These are a sample of heading in my expense file; therefore change to reflect your file

        print(def_expense_report.sort_values(['LogID'], ascending=False))   ## sorts output in ascending order
       


# creation of object
cost = PersonalFinance

# outputting results of computation
print(cost.ISP())

# print(cost)

print(cost.expense_analysis())
