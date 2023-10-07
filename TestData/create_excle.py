from openpyxl import *
wb=Workbook()
ws=wb.active


testdata=[['Username','password','exp'],
          ["admin@yourstore.com","admin","pass"],
          ["admin@yourstore.com","admin1","fail"],
          ["addmin@yourstore.com", "admin1", "fail"],
          ["addmin@yourstore.com", "admin", "fail"]]

for data in testdata:
    ws.append(data)
wb.save('LoginData.xlsx')