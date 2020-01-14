# -*- coding:utf-8 -*-
import json
import xlrd

name="ObjectName"
id="Id"
children="children"

data = xlrd.open_workbook('Office_type_tree.xlsx')
raw_data=data.sheets()[0]

tree_list=[]

for i in range(1,raw_data.nrows):
    tmp_data=raw_data.row_values(i)
    pid=tmp_data[4]
    if pid == '0':
        tmp_dict={id:tmp_data[0],name:tmp_data[3]}
        tree_list.append(tmp_dict)
    else :
        left=len(pid)
        list_tmp=tree_list
        k=1
        while(left>0):
            nid=pid[:2*k]
            left -= 2
            flag = 0
            for j in range(len(list_tmp)):
                #print (list_tmp[j][id])
                #print (nid)
                if list_tmp[j][id] == nid :
                    flag = 1
                    if children in list_tmp[j]:
                        list_tmp=list_tmp[j][children]
                    else:
                        list_tmp[j][children]=[]
                        list_tmp=list_tmp[j][children]
            if flag == 0:
                raise Exception("没有找到父节点")
            k+=1
        tmp_dict = {id: tmp_data[0], name: tmp_data[3] }
        list_tmp.append(tmp_dict)

with open("office.json",'w',encoding='utf-8') as f:
    f.write(json.dumps(tree_list,indent=2,ensure_ascii=False))






