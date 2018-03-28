import requests,json

# cookies = 'JSESSIONID=D4DBD7E0019945B188855362B4FB2A98;JSESSIONID=72740DEF668491D452692A41331FC7CA;acw_tc=AQAAADA7WyXJWg0AmxN2cWPPSYtpVoWj'
headers = {'SVER':'3','User-Agent':'zhang tong jia yuan/5.4.0(Android)',
           'Content-Type':'application/json;chartset=utf-8',
           'Accept-encoding':'gzip'
           }
formdata={}
# formdata = {'babyUserId':'05b1a4624bd71f15044d'}
# formdata['reqcode']="1094"
# formdata['reqcodeversion']="5.3"
# formdata['body']='''{"msgtypelist":[{"msgtype":8},{"msgtype":9},{"msgtype":10},{"msgtype":11},{"msgtype":12},{"msgtype":13},{"msgtype":41},{"msgtype":26},{"msgtype":6},{"msgtype":7},{"msgtype":33},{"msgtype":21},{"msgtype":25},{"msgtype":31},{"msgtype":32},{"msgtype":3},{"msgtype":2},{"msgtype":1},{"msgtype":19},{"msgtype":60},{"msgtype":14},{"msgtype":15},{"msgtype":16},{"msgtype":17},{"msgtype":57},{"msgtype":55},{"msgtype":51},{"msgtype":45},{"msgtype":50}]}'''
# formdata['body']=""
# formdata['studentId']='463cf42a48ea1cd573cf'
formdata['babylist']='[{"babyuid":"05b1a4624bd71f15044d","studentId":"463cf42a48ea1cd573cf"}]'
# formdata['parentUserId'] = 'a16458896020b8200394'
# formdata['sessionid']='D4DBD7E0019945B188855362B4FB2A98'
cookies={}
cookies['JSESSIONID']='D4DBD7E0019945B188855362B4FB2A98'
cookies['ClientVersion']='5.4.0'
url ="https://zths.szy.cn/family/baby/list/1357/v1.0"
# response = requests.post("https://h5server.ztjy61.com/H5Server/rank/getBabyRanking/V2.0.0",headers=headers,cookies=cookies,data=formdata)
response = requests.post(url,data='''{'babylist':[{"babyuid":"05b1a4624bd71f15044d","studentId":"463cf42a48ea1cd573cf"}]}''',cookies=cookies,headers=headers)
# print(response.request.headers)
print(response.text)
