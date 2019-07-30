import xlrd
file=xlrd.open_workbook("C:\\Users\\linzi\\Desktop\\result.xls")
#获取当前文件的表
shxrange=range(file.nsheets)
try:
    sh=file.sheet_by_name("保单查询结果清单")
except :
    print("no sheet in %s named '保单查询结果清单'".format("C:\\Users\\linzi\\Desktop\\result.xls"))
#获取行数和列数
nrows=sh.nrows
ncols=sh.ncols
#获取第二行第一列的数据
cell_value=sh.cell_value(1,0)
#新建空列表
row_list=[]
for i in range(0,nrows):
    row_data=sh.row_values(i)
    row_list.append(row_data)
print(row_list)
cell=sh.cell_value(2,5)
print(cell)