import pandas
import os
from xml.dom import minidom

def writeXML(country:str,keyList:list,textList:list):     
    print("创建文件夹："+country)
    if not os.path.exists(country):
        os.mkdir(country)
    newDoc=minidom.Document()
    resourcesNode=newDoc.createElement('resources')
    newDoc.appendChild(resourcesNode)
    for index in range(len(textList)):
        stringNode=newDoc.createElement('string')
        stringNode.setAttribute('name',str(keyList[index]))
        resourcesNode.appendChild(stringNode)
        textNode=newDoc.createTextNode(str(textList[index]))
        stringNode.appendChild(textNode)
        print("name="+str(keyList[index])+" value="+str(textList[index]))
    print("写入文件：")
    with open(country + "/strings.xml", "w", encoding="utf-8") as fo:
        newDoc.writexml(fo, indent='', addindent='\t', newl='\n', encoding="utf-8")
        fo.close()
   
def readExcel(inputFile):
    f = open(inputFile, 'r')
    print('文件名='+f.name)   
    wb =pandas.read_excel(io=inputFile)
    keyList=wb[wb.columns[0]] 
    for index in range(len(wb.columns)):
        columsName=wb.columns[index]
        if index>0: 
            texts=wb[columsName]
            writeXML(columsName,keyList,texts)
           
def main():
    inputFile='language.xlsx'
    readExcel(inputFile)

main()

