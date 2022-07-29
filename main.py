# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import chardet

# 处理文档
# 需求，在关键字Key和key后，#之前加入换行符
def processFile(fileAddr):
    writeFlag = True
    eco = getEncoding(fileAddr)
    fr = open(fileAddr, 'r', encoding=eco)
    lines=fr.readlines()
    fr.close()
    print("Start process document!")
    fw=open(fileAddr,'w',encoding="UTF-8")
    for i in lines:
        if 'ey:' in i:
            writeFlag=False
        if '#' in i:
            writeFlag=True
        if writeFlag:
            fw.write(i)
    fw.close()
    print("Ending!")
# 获取文件编码
def getEncoding(addr):
    with open(addr, 'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']


# def replaceEcoding(addr):

# 转换文件编码为utf-8
def convertEcoding(fileAddr):
    eco = getEncoding(fileAddr)
    fr = open(fileAddr, 'r', encoding=eco)
    lines = fr.readlines()
    fr.close()
    fw = open(fileAddr, 'w', encoding='UTF-8')
    for i in lines:
        fw.write(i)


if __name__ == '__main__':
    t = 1
    while t < 45:
        addr = "/Users/xzx/Documents/1/chapter" + str(t) + ".txt"
        
        processFile(addr)
        t += 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
