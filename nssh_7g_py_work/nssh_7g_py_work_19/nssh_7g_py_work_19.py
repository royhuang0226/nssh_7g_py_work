import sys

#file_name = "out.txt"

try:
    file_in = open("in.txt", 'r')
    file_out = open("out.txt", 'w+')
except:
    print('cannot open ', file_name)
else:
    # 當 try 內的所有檔案都成功開啟，才會執行此處的讀寫邏輯
    i = 1
    for line in file_in:
        # 印出去除末尾換行符號的文字到螢幕上
        print(line.rstrip())
        # 將含有行號的字串寫入 out.txt
        file_out.write("line" + str(i) + ":" + line)
        i = i + 1
    
    # 確保釋放檔案資源
    file_in.close()
    file_out.close()
    print("\n[系統提示] 檔案處理完成，已成功寫入 out.txt")