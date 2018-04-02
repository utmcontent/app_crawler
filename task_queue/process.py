import requests,json
from requests.exceptions import RequestException

from datetime import date
import pickle
from multiprocessing import Pool
import os,time,random
# NUMBERS_PATH=os.path.join("family_mumbers.txt")
INSPIRE=[
'When there is no desire, all things are at peace. - Laozi',
'Simplicity is the ultimate sophistication. - Leonardo da Vinci',
'Simplicity is the essence of happiness. - Cedric Bledsoe',
'Smile, breathe, and go slowly. - Thich Nhat Hanh',
'Simplicity is an acquired taste. - Katharine Gerould',
'Well begun is half done. - Aristotle',
'He who is contented is rich. - Laozi',
'Very little is needed to make a happy life. - Marcus Antoninus',
]

class TaskInterface(object):
  priority=0
  name=None
  GHEADER={'User-Agent':'zhang tong jia yuan/5.4.0(Android)','SVER':'3','Content-Type':'application/json;charset=utf-8'}
  PHEADER={'User-Agent':'zhang tong jia yuan/5.4.0(Android)','SVER':'3','Content-Type':'application/x-www-form-urlencoded; charset=utf-8'}
  def __init__(self,session=None):
    self.session={'JSESSIONID':session,'ClientVersion':'5.4.0'}

  def run(self):
    pass

  def get_json(self,url,data="{}",headers=PHEADER):
        try:
            response = requests.post(url,data=data,headers=headers,cookies=self.session)
            response.raise_for_status()
            # print(response.request.headers)
           
            return json.loads(response.text)
        except RequestException as err:
            print(err)
  def get_userid(self):
        data = {}
        url="https://zths.szy.cn/ZTHServer/userinfo/init"
        data['reqcode'] ='1057'
        data['reqcodeversion']='5.3'
        data['body']="{}"
        return self.get_json(url,data=data)

  def login(self,userphone,password,imei):
    url='https://zths.szy.cn/login/parent/1000/v1.0'
    data ='''{"password":"%s","apptype":1,"devkey":"%s","versionnum":"5.4.0","devtype":3,"logintype":"1","pwd2":"e10adc3949ba59abbe56e057f20f883e","account":"%s","release":"1","oemid":"1"}'''%(password,imei,userphone)
    return self.get_json(url,data=data,headers=self.GHEADER)
  def save_login_data(self):
    results = []
    data_file = os.getcwd()
    try:
        with open(data_file+'/family_mumbers.txt','r') as f:
          for line in f.readlines():
            if line:
              phone,passwd,imei=line.strip().split(',')
              login_user=self.login(phone,passwd,imei)
              sessionid=login_user.get('body').get('sessionid')
              results.append(sessionid)
    except Exception as err:
        print("需提供账号密码",str(err))
        return False
    with open('passwd.pickle','wb') as pf:
        pickle.dump(results,pf)
  def check_valid_file(self):
    return os.path.isfile('passwd.pickle') and os.path.isfile('family_mumbers.txt')

  def get_all_growth(self,cid,filter='1,2,3'):
    url ='https://zths.szy.cn/ZTHServer/growup/list/'

    data = {}
    data['reqcode']='1124'
    data['reqcodeversion']='5.3'
    data['body']='{"number":20,"pageindex":1,"childid":"05b1a4624bd71f15044d","covernum":1,"filter":"%s","labelname":""}'%(filter)
    return self.get_json(url,data=data)

  def get_childid(self):
     url='https://zths.szy.cn/family/baby/list/1343/v3.0'
     return self.get_json(url,headers=self.GHEADER)


class Login(TaskInterface):
  priority=3
  name="login"
  def run(self):
    if not self.check_valid_file():
      r = self.save_login_data()
      print('login',r)



class Day_first(TaskInterface):
  priority=0
  name="first use today"

  def run(self):
    r = self.daily_log_score()
    print(r)

  def daily_log_score(self):
    url = "https://zths.szy.cn/ZTHServer/app/logineverydayonetimes"
    data ="reqcode=1236&reqcodeversion=5.3&body={}"

    return self.get_json(url,data=data)

class Post_a_message(TaskInterface):
  priority=0
  name="post a message"

  def run(self):
    # .get('body').get('phonenumber')
    # uid =self.get_userid().get('body').get('phonenumber')
    uid =self.get_userid().get('body').get('userid')
    # print(self.get_childid())

    info = self.get_childid()['body']['babyinfolist'][0]

    cid,stuid=info['babyuid'],info['studentid']
    r = self.post_growth(random.choice(INSPIRE),stuid,cid)
    dr = self.delete_growth(r['body']['growthid'])
    print(dr)

  def post_growth(self,textcontent,sid,cid):
    url="https://zths.szy.cn/ZTHServer/growup/add"
    data = '''reqcode=1119&reqcodeversion=5.3&body={"studentid":"%s","childid":"%s","archivestype":2,"textcontent":"%s","recordtime":"%s","addrstr":"","addrlng":"0.0","addrlat":"0.0","sendtype":0,"musicurl":"","musicname":"","labelids":"502022"}'''%(sid,cid,textcontent,date.today().__str__())
    return self.get_json(url,data=data)
  def delete_growth(self,growid):
    url="https://zths.szy.cn/ZTHServer/growup/delgrowth"
    data = '''reqcode=1139&reqcodeversion=5.3&body={"growthid":%s}'''%(growid)
    return self.get_json(url,data=data)

class Star(TaskInterface):
  priority=0
  name="delete the message"

  def run(self):
    info = self.get_childid()['body']['babyinfolist'][0]

    cid,stuid=info['babyuid'],info['studentid']
    uid =self.get_userid().get('body').get('userid')
    growlist = self.get_all_growth(cid=cid,filter='1,2')
    results=[]
    for item in growlist['body']['growuplist']:
        results.append(self.unstar(item['mypointid'],item['archivesid'],item['childid']))
        results.append(self.star(item['archivesid'],item['childid'],uid))
    print(results)


  def star(self,archivesid,childid,userid):
    url="https://zths.szy.cn/ZTHServer/growup/pointpraise"
    data = {}
    data['reqcode'] ='1122'
    data['reqcodeversion']='5.3'
    data['body']='{"archivesid":"%s","childid":"%s","classalbumid":0,"userid":"%s",}'%(archivesid,childid,userid)
    return self.get_json(url,data=data)

  def unstar(self,commentid,archivesid,childid):
    url="https://zths.szy.cn/ZTHServer/growup/delcomment"
    data={}
    data['reqcode'] ='1120'
    data['reqcodeversion']='5.3'
    data['body']='{"commentid":"%s","archivesid":"%s","childid":"%s"}'%(commentid,archivesid,childid)
    return self.get_json(url,data=data)

class Talk(TaskInterface):
  priority=2
  name='给老师留言获取分数'

  def afterTalk(self):
    url="https://zths.szy.cn/ZTHServer/im/task"
    data='''reqcode=1210&reqcodeversion=5.3&body=%7B%22groupid%22%3A%22%40TGS%23236JCEDFD%22%2C%22improvider%22%3A2%7D'''
    return self.get_json(url,data=data) 
  
  def run(self):
    r=self.afterTalk()
    print(r)