#给NUM_FOLLOWER加上人名和流派

from xlrd import open_workbook
import xlwt


wb = open_workbook('influencer_jiangxu.xls')
wc = open_workbook('NUM_FOLLOWER.xls')

a_data=[]
b_data=[]
c_data=[]
d_data=[]
for s in wb.sheets():
    for row in range(s.nrows):
        
        values = []
        if row >= 1:
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)    #values是存行的数列
                                        
            a_data.append(values[0])    #id
            b_data.append(values[1])    #名字
            c_data.append(values[2])    #流派
            d_data.append(values[3])    #时间


book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('名字流派',cell_overwrite_ok=True)
col=('名字','流派','时间') #元组col定义列的数量和名称
#第一列写入sheet表
for i in range(0,3):
		sheet.write(0,i,col[i])

for s in wc.sheets():
    for row in range(s.nrows):
        if row>=1:
            num=s.cell(row,0).value     #num是id值
            loco=a_data.index(num)      #在id列表中寻找id值的位置
            loco_name=b_data[loco]      #找到名字
            loco_pai=c_data[loco]       #找到流派
            loco_time=d_data[loco]      #找到时间
            sheet.write(row,0,loco_name)
            sheet.write(row,1,loco_pai)
            sheet.write(row,2,loco_time) #写入

savepath = 'D:/Desktop/excel.xls'
book.save(savepath)

        
