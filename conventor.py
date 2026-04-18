from bs4 import BeautifulSoup
import requests

url = "https://minfin.com.ua/ua/currency/nbu/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

rate = soup.find("div", class_="fevpFL").contents[0].strip()
rate = float(rate.replace(",", "."))

choice = input("Оберіть валюту для конвертації (USD, UAH): ").upper()
amount = float(input("Введіть суму: "))

if choice == "USD":
    converted_amount = amount * rate
    print(f"{amount} USD = {converted_amount:.2f} UAH")

elif choice == "UAH":
    converted_amount = amount / rate
    print(f"{amount} UAH = {converted_amount:.2f} USD")
    
else:    
    print("Невірний вибір валюти. Будь ласка, виберіть USD або UAH.")
