from functools import reduce
import xlsxwriter


def export_check(text):
    with xlsxwriter.Workbook('res.xlsx') as workbook:
        worksheet = workbook.add_worksheet()

        data = list(reversed(reduce(lambda result, element: [element.split('\t')]
                                    + result, text.split('\n'), [])))

        for row, (item, price, quantity) in enumerate(data):
            worksheet.write(row, 0, item)
            worksheet.write(row, 1, float(price))
            worksheet.write(row, 2, int(quantity))
            worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

        worksheet.write(len(data), 0, 'Итого')
        worksheet.write(len(data), 3, f'=SUM(D1:D{len(data)})')
