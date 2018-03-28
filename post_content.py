import requests,json
# 添加成长印记 返回growthid 可以用来控制

headers = {'SVER':'3','User-Agent':'zhang tong jia yuan/5.4.0(Android)',
           'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
           'Accept-encoding':'gzip',
           }
formdata={}

formdata['reqcode']='1119'
formdata['reqcodeversion']='5.3'
formdata['body']='{"studentid":"463cf42a48ea1cd573cf","childid":"05b1a4624bd71f15044d","archivestype":2,"textcontent":"111","recordtime":"2018-03-28","addrstr":"","addrlng":"0.0","addrlat":"0.0","sendtype":0,"musicurl":"","musicname":"","labelids":"502022"}'

cookies={}
cookies['JSESSIONID']='D4DBD7E0019945B188855362B4FB2A98'
cookies['ClientVersion']='5.4.0'
url ="https://zths.szy.cn/ZTHServer/growup/add"
# # response = requests.post("https://h5server.ztjy61.com/H5Server/rank/getBabyRanking/V2.0.0",headers=headers,cookies=cookies,data=formdata)
response = requests.post(url,data=formdata,cookies=cookies,headers=headers)
print(response.request.headers)
print(response.text)
