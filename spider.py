import requests,json

formdata['studentId']='463cf42a48ea1cd573cf'
response = requests.post("https://h5server.ztjy61.com/H5Server/rank/getBabyRanking/V2.0.0",data=formdata)
print(response.text)
