import xlsxwriter
from sys import stdin

data = list(map(str.split, map(str.strip, stdin)))

with xlsxwriter.Workbook('Суммы.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row, (item, price) in enumerate(data):
        worksheet.write(row, 0, item)
        worksheet.write(row, 1, int(price))

    chart = workbook.add_chart({'type': 'pie'})
    chart.add_series({'categories': '=Sheet1!A1:A5', 'values': '=Sheet1!B1:B5'})
    worksheet.insert_chart('C3', chart)
