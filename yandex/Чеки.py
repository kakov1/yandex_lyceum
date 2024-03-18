from functools import reduce
import xlsxwriter


def export_check(text):
    with xlsxwriter.Workbook('res.xlsx') as workbook:

        data = [list(reversed(reduce(lambda result, element:
                       [element.split('\t')] + result,
                i, [])[1:])) for i in [i.split('\n') for i in text.split('---\n')]]
        print(data)
        for i in data:
            worksheet = workbook.add_worksheet()
            already = []
            for row, (item, price, quantity) in enumerate(i):
                worksheet.write(row, 0, item)
                worksheet.write(row, 1, float(price))
                worksheet.write(row, 2, int(quantity))
                worksheet.write(row, 3, f'=B{row + 1}*C{row + 1}')

            worksheet.write(len(data), 0, 'Итого')
            worksheet.write(len(data), 3, f'=SUM(D1:D{len(data)})')


export_check('товар 1\t100\t5\n'
             'товар 3\t7\t500\n'
             'товар 1\t100\t5\n'
             'товар 2\t200\t6\n'
             'товар 3\t7\t500\n'
             '---\n'
             'товар 1\t100\t5\n'
             'товар 1\t100\t5\n'
             'товар 1\t100\t5\n'
             'товар 3\t7\t500\n')