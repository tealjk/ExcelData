#!/usr/bin/python

import xlsxwriter



workbook = xlsxwriter.Workbook('/Users/junkim/Desktop/PythonTOexcel/staging/testDataInput/testdata.xlsx')

worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', 20)


worksheet.write('A1','Hello')

workbook.close()




