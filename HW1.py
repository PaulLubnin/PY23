salary = int(input('Введите заработанную плату за месяц: '))
mortgage_interest = int(input('Введите сколько процентов от зп уходит на ипотеку: '))
mortgage_payment = salary * mortgage_interest // 100
after_paying_the_mortgage = salary - mortgage_payment
percentage_of_expenses = int(input('Введите сколько процентов от зп уходит на жизнь: '))
after_household_expenses = after_paying_the_mortgage - ((salary * percentage_of_expenses) // 100)
bonus = int(input('Введите количество премий за год: '))
if bonus == 1:
  annual_bonus = salary // 2
else:
  annual_bonus = salary * bonus - salary // 2
conclusion = (
  f'Вывод:\n'
  f'Сумма платежа по ипотеке: {mortgage_payment}\n'
  f'Ежемесячный остаток после оплаты ипотеки: {after_paying_the_mortgage}\n'
  f'Ежемесячный остаток после бытовых расходов: {after_household_expenses}\n'
  f'Премиальный доход: {annual_bonus}\n'
  f'На ипотеку было потрачено: {mortgage_payment * 12}\n'
  f'Накоплено за год: {(after_household_expenses * 12) + annual_bonus}'
)
print(conclusion)