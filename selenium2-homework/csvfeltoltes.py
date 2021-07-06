# csv fájl beolvasás, űrlapkitöltés, egyezőség ellenőrzése
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import difflib
import filecmp
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/another_form.html")


# keresés és mező törlés
def find_and_clear_by_id(id):
    element = driver.find_element_by_id(id)
    element.clear()
    return element


kuldes_button = driver.find_element_by_id('submit')
row_count = 0

with open('table_in.csv', "r", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        row_count += 1
        # print(row)
        find_and_clear_by_id('fullname').send_keys(row[0])
        find_and_clear_by_id('email').send_keys(row[1])
        find_and_clear_by_id('dob').send_keys(row[2])
        find_and_clear_by_id('phone').send_keys(row[3])
        kuldes_button.click()

print(row_count)

# táblázat export
time.sleep(1)
driver.find_element_by_xpath('//button').click()
time.sleep(2)

# Próbálkozások egyezőségvizsgálatra

# 1. verzió
print('*' * 50)
print('1. verzió FILECMP használatával - byte szinten (Win CRLF - UNIX LF)')
print('*' * 50)
if filecmp.cmp('C:\\T360\\PycharmProjects\\selenium-py-peldatar\\selenium2-homework\\table_in.csv',
               'C:\\Users\\T360\\Downloads\\table.csv'):
    print('A két fájl megegyezik.')
else:
    print('A két fájl eltérő.', '\n')
print('-' * 50, '\n')

# 2. verzió
print('*' * 50)
print('2. verzió soronkénti listába olvasással byte szinten - különböző sorok egymás alatt listázva')
print('*' * 50)
table_in = open('table_in.csv', 'r', encoding='utf-8').readlines()
table = open('C:\\Users\\T360\\Downloads\\table.csv', 'r', encoding='utf-8').readlines()
table_diff = []
if len(table_in) == len(table):
    for item in range(len(table_in)):
        if table_in[item] == table[item]:
            continue
        else:
            table_diff.append(table_in[item])
            table_diff.append(table[item])

if table_diff == []:
    print('A két fájl megegyezik.')
else:
    print('A két fájl eltérő.', '\n')
    for i in table_diff:
        print(i)
print('-' * 50, '\n')

# 3. verzió
print('*' * 50)
print('3. verzió by Stackoverflow')
print('*' * 50)
with open('table_in.csv') as file_1:
    file_1_text = file_1.readlines()
with open('C:\\Users\\T360\\Downloads\\table.csv') as file_2:
    file_2_text = file_2.readlines()

# A különbségek keresése és megjelenítése
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='table_in.csv',
        tofile='C:\\Users\\T360\\Downloads\\table.csv', lineterm=''):
    print(line)
print('-' * 50)

driver.close()
