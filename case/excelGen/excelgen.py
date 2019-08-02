import xlrd
import xlwt
from io import BytesIO
from collections import OrderedDict
import simplejson as json

# folder_path = './data/shopify.xlsx'
# wb = xlrd.open_workbook(folder_path)
# sh = wb.sheet_by_index(0)

def makeData(jsonData):
  data_list = []
  for row in (jsonData):
    # data = OrderedDict()
    # row_values = sh.row_values(rownum)
    # data['open_id'] = row_values[0]
    # data['company_name'] = row_values[0]
    # data['ppp'] = row_values[0]
    # data_list.append(data)
    if row['a'] <= 0:
      row['exception'] = 'a must large than 0'
      data_list.append(row)
  return data_list

requestBody = [{'a':-1,'b':'ccc','c':'dd'},{'a':1,'b':'ccc','c':'dd'}]
print(makeData(requestBody))

def makeExcel():
  f=open('test.xlsx','w')
  f.close()
  return f