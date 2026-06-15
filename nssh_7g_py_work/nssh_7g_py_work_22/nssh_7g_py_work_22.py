def print_table(file):
    data = open(file,'r')
    for record in data:
        fields = record.split() # fields[0]=Oranges, fields[1]=5.6, fields[2]=1.33
        print(" {0:10}  {1:5.1f} {2:7.2f} ". format(fields[0], eval(fields[1]), eval(fields[2])))

print_table('file22.txt')

# 第 4 行已經把每筆資料切成 fields[0](水果名稱)、fields[1](重量)、fields[2](價格)三個字串欄位
# 水果名稱:{0:10} → 寬度 10、字串預設靠左對齊
# 重量:{1:5.1f} → 寬度 5、靠右對齊（數字預設靠右）、小數點後 1 位
# 價格:{2:7.2f} → 寬度 7、靠右對齊、小數點後 2 位