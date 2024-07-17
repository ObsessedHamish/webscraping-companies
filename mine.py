from bs4 import BeautifulSoup
import requests
import csv
from collections import defaultdict


def def_value():
    return "Not Present"


website = """
https://app.companiesoffice.govt.nz/companies/app/ui/pages/companies/8998861?backurl=H4sIAAAAAAAAAC2LMQrDMBAEf6PGhV9whFRuXASSDyy6wxZEJ1l3Cvj3FibdzjA7V2xicyy5QtNYJmhxf%2BTCQuZQRuPgZxUS9eQjCQdZhu3CU%2FIA%2FkGj8AsqX%2FLWJdzh%2BRkfo%2Be6%2Fvnt8G5LK73e%2BgLAB3OEegAAAA%3D%3D#"""
source = requests.get(website).text

soup = BeautifulSoup(source, 'html.parser')
containers = soup.find_all('div', class_='fullWidth panel panelContent')

csv_file = open('company_info.csv', 'w')  # second arg is "write"
data = defaultdict(def_value)

for c in containers:
    companySummary = c.find_all('div', class_='row')

    for num in range(len(companySummary)):

        line = companySummary[num]
        value = line.text.splitlines()
        print(value)

    companySummary = c.find_all('table', class_='otherDetailsTable')
    for num in range(len(companySummary)):


        line = companySummary[num]
        value = line.text.splitlines()
        print(value)
