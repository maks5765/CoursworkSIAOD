import csv
from collections import defaultdict

# Чтение CSV файла
try:
    with open("C:\\Users\\Salin\\.vscode-cli\\coursework\\saves.csv", 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
except FileNotFoundError:
    print("Файл не найден.")
    exit()
except Exception as e:
    print("Ошибка при чтении файла:", e)
    exit()

# Проверка на пустой файл
if not data:
    print("Файл пуст.")
    exit()

# Инициализация словарей для хранения данных
product_sales = defaultdict(int)
product_revenue = defaultdict(int)

# Рассчитать общую выручку магазина и количество продаж для каждого товара
total_revenue = 0
for row in data:
    try:
        product_name = row['Название товара']
        sales_count = int(row['Количество продаж'])
        total_cost = float(row['Общая стоимость'])
    except ValueError:
        print("Некорректные данные в строке:", row)
        continue

    product_sales[product_name] += sales_count
    product_revenue[product_name] += total_cost
    total_revenue += total_cost
    
# Вывод общей выручки
print(f'Общая выручка магазина: {total_revenue}')

# Найти товар, который был продан наибольшее количество раз
most_sold_product = max(product_sales, key=product_sales.get)
print(f'Товар, который был продан наибольшее количество раз: {most_sold_product}')

# Найти товар, который принес наибольшую выручку
most_revenue_product = max(product_revenue, key=product_revenue.get)
print(f'Товар, который принес наибольшую выручку: {most_revenue_product}')

# Составить отчет
report = []
for product in product_sales:
    report.append({
        'Название товара': product,
        'Количество продаж': product_sales[product],
        'Общая стоимость': product_revenue[product],
        'Доля в выручке': product_revenue[product] / total_revenue
    })
 

# Вывод отчета
for row in report:
    print(row)