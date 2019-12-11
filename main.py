import pandas as pd
from preference_cost import calculate_preference_cost
from accounting_cost import calculate_accounting_cost

def print_result_csv(resultlist):
    with open("output.csv","w") as file:
        file.write("family_id,assigned_day\n")
        for family,day in enumerate(resultlist):
            file.write(str(family))
            file.write(",")
            file.write(str(day))
            file.write("\n")


if __name__ == "__main__":
    data = pd.read_csv("family_data.csv")
    print(data.head())

    accounting_cost = 0
    preference_cost = calculate_preference_cost()
    total_cost = accounting_cost + preference_cost
    print(total_cost)

    print_result_csv([1,2])