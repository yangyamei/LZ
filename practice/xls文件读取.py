import xlrd
#打开excel读取文件，open_workbook()为打开Excel文件的方法，参数为文件名
file=xlrd.open_workbook("C:\\Users\\linzi\\Desktop\\result.xls")
'''
获取sheets数目
'''
print(file.nsheets)
'''
获取sheets列表
'''
print(file.sheets())
'''
获取sheets name列表
'''
print(file.sheet_names())
'''
获取文件中的sheet
'''
sheet1=file.sheets()[0]
#sheets返回一个sheet列表
sheet2=file.sheet_by_index(0)
print(sheet2)
#索引顺序获取
sheet3=file.sheet_by_name("保单查询结果清单") #通过名称获取
shxrange=range(file.nsheets)
try:
    sh=file.sheet_by_name("保单查询结果清单")
except:
    print("no sheet in %s named '保单查询结果'".format("C:\\Users\\linzi\\Desktop\\result.xls"))
#获取行数
nrows=sh.nrows
#获取列数
ncols=sh.ncols
#打印表格的行数和列数
#print("ncows{0},ncols{1}".format(nrows,ncols))
'''
获取某行、某行值列表，某列、某列值列表
'''
#获取第一行
print(sh.row(1))
#获取第一行值列表
print(sh.row_values(1))
#获取第一列
print(sh.col(1))
#获取第一列值列表
print(sh.col_values(1))

'''
获取单元格的值
'''
cell=sh.cell(1,1)
print(cell)
cell_value1=sh.cell_value(1,1)
print(cell_value1)
cell_value2=sh.cell(1,1).value
print(cell_value2)