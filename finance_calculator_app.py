def compound_interest():
    try:
        principal = float(input("Enter principal amount: "))
        interest_rate = float(input('Enter annual interest rate (as a decimal): '))
        if interest_rate >= 1:
            interest_rate = interest_rate/100
        times_compounded = float(input('Enter the number of times interest is compounded per year: '))
        time = float(input('Enter time (in years): '))
    except ValueError:
        return 'Incorrect value given!'
    result = principal * (1 + interest_rate/times_compounded)**(times_compounded*time)
    return f'Total interest earned: {(result-principal):.2f}\nFuture investment value: {result}'


def simple_interest():
    try:
        principal = float(input("Enter principal amount: "))
        interest_rate = float(input('Enter annual interest rate (as a decimal): '))
        if interest_rate >= 1:
            interest_rate = interest_rate/100
        time = float(input('Enter time (in years): '))
    except ValueError:
        return 'Incorrect value given!'
    result = principal * (1 + interest_rate * time)
    return f'Total interest earned: {(result-principal):.2f}\nFuture investment value: {result}'


def loan_payment():
    try:
        present_value = float(input("Enter present value: "))
        rate_per_period = float(input("Enter the rate per period (as a decimal): "))
        if rate_per_period >= 1:
            rate_per_period = rate_per_period/100
        number_of_periods = float(input("Enter the number of periods: "))
    except ValueError:
        return 'Incorrect value given!'
    result = (rate_per_period * present_value) / (1 - ((1 + rate_per_period)**(-number_of_periods)))
    return f"Total loan payment is {result:.2f}"


def future_value_of_savings():
    try:
        present_value = float(input("Enter present value: "))
        interest_rate_annual = float(input("Enter the annual interest rate (as a decimal): "))
        if interest_rate_annual>= 1:
            interest_rate_annual = interest_rate_annual / 100
        years = float(input("Enter the number of yeats: "))
    except ValueError:
        return 'Incorrect value given!'
    result = present_value * (1 + (interest_rate_annual * years))
    return  f"Future value of savings is {result:.2f}"


def main_menu():
    print('''Main Menu:
    Calculate Simple Interest - 1
    Calculate Compound Interest - 2
    Calculate Loan Payment - 3
    Calculate Future Value of Savings - 4
    Quit - 5''')
    while True:
        choice = input('Enter your choice (1/2/3/4/5): ')
        if choice == "1":
            print(simple_interest())
        elif choice == "2":
            print(compound_interest())
        elif choice == "3":
            print(loan_payment())
        elif choice == "4":
            print(future_value_of_savings())
        elif choice == "5":
            print('Goodbye!')
            break
        else:
            print('Invalid input!')


main_menu()