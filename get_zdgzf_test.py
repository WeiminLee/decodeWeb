# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 22:33:30 2019

@author: lwm
"""


import json
import requests
header_dict = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/76.0.3809.132Safari/537.36',
               "Content-Type": "application/json",
               'Host': 'webzf.pdgzf.com',
               'nonce': '8QNWHL45Q1AJOO4UB2HXJ4K1GHHNUBJQ',
               'Origin': 'http://webzf.pdgzf.com',
               'Referer': 'http://webzf.pdgzf.com/houseLists',
                'signature': 'U8EIYM1156VVJV6ELA9Y9KZZX55N6GSL',
                'timestamp': 'GDWYTHJMPH2AEAAQRZSI3R726ZNHO8XV',
                'token': 'TLRA8Z3IITXK54WPMVB2KJYHYKJANTJB'
               }
url = 'http://webzf.pdgzf.com/api/api/PStruct/GetAreaList'
url = 'http://webzf.pdgzf.com/api/api/PStruct/QueryGZFPStruct'
data = json.dumps({'CityCode': '310115','AreaCode': '310115'})

data = json.dumps({'QueryJson':{'Type':1}})
req = requests.post(url=url,data=data,headers=header_dict)
res_dic = json.loads(req.text)
print(res_dic)

for val in res_dic['Data']['Rows']:
    print(val['name'])

 
    

===========================================================================================================
import json,base64,os
from urllib import parse
import requests
url = 'http://webzf.pdgzf.com/api/api/PStruct/QueryVerificationCodeErrorCount'
header_dict = {'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/76.0.3809.132Safari/537.36',
               "Content-Type": "application/x-www-form-urlencoded",
               'EagleId': '65e21a1f15674322042822401e',
               'Host': 'webzf.pdgzf.com',
               'nonce': 'YEBDP4V5V3689TX5VFT9LFHKNHPI8QSG',
               'Origin': 'http://webzf.pdgzf.com',
               'Referer': 'http://webzf.pdgzf.com/houseLists',
               'signature': 'UU1CADZ2CX6RFQYGIIDKZZYMMAIXY19T',
               'timestamp': 'GDWYTHJMPH2AEAAQRZSI3R726ZNHO8XV',
               'token': 'a3b49b2c-1545-4d2c-908a-f1f050b9e20e'
               }
FormData = {'AccountId':'c5576f3d-6820-42fa-9788-f1be923a831e','RoomId': 'E66C5DD9-BEFB-405B-B0FF-6DC717FA59BC'}
data = parse.urlencode(FormData)

for i in range(200,300):
    req = requests.post(url=url,data=data,headers=header_dict)
    res_dic = json.loads(req.text)
    base64_data = res_dic['Data']['VerificationCode']
    
    save_dir = r'D:\LearningProgram\getAPI\imgs'
    imgdata = base64.b64decode(base64_data)    
    print(i)
    with open(os.path.join(save_dir,'{}.jpg'.format(i)),"wb") as f:
        f.write(imgdata)


===========================================================================================================

url = 'data:image/jpeg;base64,'+base64_data
header_dict = {'Content-Type': 'image/jpeg',
               'Referer': 'http://webzf.pdgzf.com/houseDetails?Id=E66C5DD9-BEFB-405B-B0FF-6DC717FA59BC'}

req = requests.get(url=url,headers=header_dict)
res_dic = json.loads(req.text)



===========================================================================================================

import sys,os
import numpy as np
from PIL import Image,ImageDraw
 
image = Image.open(r'D:\LearningProgram\getAPI\imgs\48.jpg','r')
img_arr = np.array(image.convert("L"))
img_arr.shape



threshold = 200
table = np.zeros(shape=img_arr.shape)
for i in range(img_arr.shape[0]):
    for j in range(img_arr.shape[1]):
        if img_arr[i][j] > threshold:
            table[i][j] = 255
Image.fromarray(np.uint8(table))


def denoising(table):
    (w,h)=table.shape
    for j in range(1,h-1):
        for i in range(1,w-1):
            count=0
            if table[i,j-1] == 255:count=count+1
            if table[i,j+1] == 255:count=count+1
            if table[i+1,j] == 255:count=count+1
            if table[i-1,j] == 255:count=count+1
            if count==4:table[i,j]=255
    return table
    
table_ = denoising(table)
Image.fromarray(np.uint8(table_))


binary_image = image.convert("1")

#测试代码
def main():
    #打开图片
    image = Image.open(r'D:\LearningProgram\getAPI\imgs\0.jpg','r')
    np.array(image)
    #将图片转换成灰度图片
    image = image.convert("L")
 
    #去噪,G = 50,N = 4,Z = 4
    clearNoise(image,50,7,10)
 
    #保存图片
    image.save("1.jpg")
 
 
if __name__ == '__main__':
    main()   
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      