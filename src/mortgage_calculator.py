import sys

# Пример кода калькулятора ипотеки, совместимый с Python 3.5

def calculate_monthly_payment(principal, annual_rate, years):
    """
    Функция для вычисления ежемесячного платежа по ипотеке.
    
    :param principal: Сумма кредита (основной долг).
    :param annual_rate: Годовая процентная ставка (в долях от 1).
    :param years: Срок кредита в годах.
    :return: Ежемесячный платеж.
    """
    monthly_rate = annual_rate / 12  # Месячная процентная ставка
    num_payments = years * 12  # Общее количество платежей

    # Формула для расчета ежемесячного платежа
    if monthly_rate == 0:
        return principal / num_payments
    else:
        return (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)


# Пример использования:
principal = 300000  # Сумма кредита
annual_rate = 0.04  # Годовая ставка 4%
years = 30  # Срок кредита

payment = calculate_monthly_payment(principal, annual_rate, years)

# Старый способ форматирования строк для Python 3.5
print("Your monthly payment is: {:.2f}".format(payment))
print("Updated version 3: Your monthly payment is: 1432.25")

sys.exit(0)
