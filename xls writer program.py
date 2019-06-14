student= (
    ['inzmam',20],
    ['chandni',11],
    ['sameer',22],
    ['sher',33]
    )

import xlsxwriter

workbook= xlsxwriter.Workbook('student.xlsx')
worksheet= workbook.add_worksheet()

row=0
col=0

for name,roll in (student):
   worksheet.write(row,col, name)
   worksheet.write(row,col+1, roll)
   row+=1

worksheet.write(row,col, 'Total')
worksheet.write(row,col+1, '=sum(B1:B4)')

workbook.close()
