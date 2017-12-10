import pandas as pd
import openpyxl as op
from pandas import ExcelWriter


def enhance_excel(filename):
    foo = pd.read_excel(filename)
    if 'Status' not in list(foo.columns):
        foo['Status'] = 'Not Sent'
        writer = ExcelWriter(filename)
        foo.to_excel(writer, 'Sheet1', index=False)
        writer.save()

def change_color(filename):
    df = pd.read_excel(filename)
    writer = ExcelWriter(filename,engine = 'openpyxl')
    color_code = {'Sent':'green','Not Sent':'red'}
    styled = (df.style.applymap(lambda v: 'background-color: %s' % color_code[v] if v in color_code else '') )
    styled.to_excel(filename, engine='openpyxl')

def update_excel(filename,index):
    foo = pd.read_excel(filename)
    char = chr(65+len(foo.columns))
    xfile = op.load_workbook(filename)
    sheet = xfile.get_sheet_by_name('Sheet1')
    sheet['{}{}'.format(char,index)] = 'Sent'
    xfile.save(filename)

def read_pdf_in(filename):
    foo =pd.read_excel(filename)
    enhance_excel(filename)
    excel_dict = {}
    for index,row in foo.iterrows():
        excel_dict[row['Encoded Code']] = { i:getattr(row,i) for i in list(foo.columns) }
        excel_dict[row['Encoded Code']]['index'] = index
    return excel_dict
    
# print(read_pdf_in('./input_data.xlsx'))
# # read_pdf_in('./input_data.xlsx')
# enhance_excel('./input_data.xlsx')
# update_excel('./input_data.xlsx')
# change_color('./input_data.xlsx')