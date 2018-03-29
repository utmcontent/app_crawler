import requests,json
from requests.exceptions import RequestException

from datetime import date
import pickle
from multiprocessing import Pool
import os,time,random

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
class Baby(object):

    def __init__(self,session):
        self.session={'JSESSIONID':session,'ClientVersion':'5.4.0'}
        self.headers={'User-Agent':'zhang tong jia yuan/5.4.0(Android)','SVER':'3','Content-Type':'application/json;charset=utf-8'}

    def get_json(self,url,data="{}",headers=None):
        try:
            response = requests.post(url,data=data,headers=headers,cookies=self.session)
            response.raise_for_status()
            return json.loads(response.text)
        except RequestException as err:
            print(err)

    def get_baby_info_list(self):
        url='https://zths.szy.cn/family/baby/list/1343/v3.0'
        return self.get_json(url,headers=self.headers)
    def get_childid(self):
            baby_info = self.get_baby_info_list()
            #  studentid,babyuid,
            info =baby_info['body']['babyinfolist'][0]
            return info['babyuid'],info['studentid']
    def get_all_growth(self,cid,filter='1,2,3'):
        url ='https://zths.szy.cn/ZTHServer/growup/list/'
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded;charset=utf-8"
        data = {}
        data['reqcode']='1124'
        data['reqcodeversion']='5.3'
        data['body']='{"number":20,"pageindex":1,"childid":"05b1a4624bd71f15044d","covernum":1,"filter":"%s","labelname":""}'%(filter)
        return self.get_json(url,data=data,headers=headers)
    def get_userid(self):
        url="https://zths.szy.cn/ZTHServer/userinfo/init"
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data = {}
        data['reqcode'] ='1057'
        data['reqcodeversion']='5.3'
        data['body']="{}"
        return self.get_json(url,data=data,headers=headers)
    def get_ranking(self,studentid):
        headers={}
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        return json.loads(self.get_json("https://h5server.ztjy61.com/H5Server/rank/getBabyRanking/V2.0.0",headers=headers,data={'studentId':studentid}).get('body'))
    def un_star(self,commentid,archivesid,childid):
        url="https://zths.szy.cn/ZTHServer/growup/delcomment"
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data = {}
        data['reqcode'] ='1120'
        data['reqcodeversion']='5.3'
        data['body']='{"commentid":"%s","archivesid":"%s","childid":"%s"}'%(commentid,archivesid,childid)
        return self.get_json(url,data=data,headers=headers)

    def star(self,archivesid,childid,userid):
        url="https://zths.szy.cn/ZTHServer/growup/pointpraise"
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data = {}
        data['reqcode'] ='1122'
        data['reqcodeversion']='5.3'
        data['body']='{"archivesid":"%s","childid":"%s","classalbumid":0,"userid":"%s",}'%(archivesid,childid,userid)
        return self.get_json(url,data=data,headers=headers)

    def star_all_teachers(self,cid,uid):
        growlist = self.get_all_growth(cid=cid,filter='1,2')
        print(growlist)
        # results = []
        # for i in range(6):
        #     for item in growlist['body']['growuplist']:
        #         results.append(self.un_star(item['mypointid'],item['archivesid'],item['childid']))
        #         results.append(self.star(item['archivesid'],item['childid'],uid))
        # return results

    def post_grouth(self,textcontent,sid,cid):
        url="https://zths.szy.cn/ZTHServer/growup/add"
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data = '''reqcode=1119&reqcodeversion=5.3&body={"studentid":"%s","childid":"%s","archivestype":2,"textcontent":"%s","recordtime":"%s","addrstr":"","addrlng":"0.0","addrlat":"0.0","sendtype":0,"musicurl":"","musicname":"","labelids":"502022"}'''%(sid,cid,textcontent,date.today().__str__())
        return self.get_json(url,data=data,headers=headers)

    def dele_my_post_grouth(self,growid):
        url="https://zths.szy.cn/ZTHServer/growup/delgrowth"
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data = '''reqcode=1139&reqcodeversion=5.3&body={"growthid":%s}'''%(growid)
        return self.get_json(url,data=data,headers=headers)
    def init_loged(self):
        url='https://zths.szy.cn/ZTHServer/userinfo/init'
        headers = self.headers.copy()
        headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
        data="reqcode=1057&reqcodeversion=5.3&body={}"
        return self.get_json(url,data=data,headers=headers)
    def start(self):
        '''定制成执行该类的所有任务，只需添加任务即可'''

        id=self.get_userid().get('body').get('phonenumber')
        print('%s 开始了每日任务....'%id)
        print('Run task %s (%s).' %(id,os.getpid()))
        start=time.time()
        uid=self.get_userid().get('body').get('userid')
        cid,stuid=self.get_childid()
        # post_a_growth = self.post_grouth(random.choice(INSPIRE),stuid,cid)
        # print(post_a_growth)
        # self.dele_my_post_grouth(post_a_growth['body']['growthid']) # 添加删除成长记录
        print('点赞')
        print(self.star_all_teachers(cid,uid))# 取消并点赞所有老师
        end = time.time()
        print('%s 完成了每日任务 用时%.2f seconds'%(id,(end-start)))


def save_login():
    results=[]
    with open('family_mumbers.txt','r') as f:
        for line in f.readlines():
            if line:
                phone,passwd=line.strip().split(',')
                login_user=login(phone,passwd)
                print(login_user)
                sessionid=login_user.get('body').get('sessionid')
                results.append(sessionid)
    with open('passwd.pickle','wb') as pf:
        pickle.dump(results,pf)



def login(userphone,password):
    url='https://zths.szy.cn/login/parent/1000/v1.0'

    data ='''{"password":"%s","apptype":1,"devkey":"b8fe01a2-ab90-4427-b15f-b25ffc44fddd","versionnum":"5.4.0","devtype":3,"logintype":"1","pwd2":"e10adc3949ba59abbe56e057f20f883e","account":"%s","release":"1","oemid":"1"}'''%(password,userphone)
    return get_json(url,data=data)
def main():
    '''
        # # 每天任务
        # # 打开掌通家园
        # # 发送成长印记 删除成长印记 混分
        # #
        # # 每周任务
        # # 给老师点赞  先取消全部老师再点赞全部老师
        # # 查看信息
        # #
        # #无法登录
    '''
    if not os.path.isfile("passwd.pickle"):
        save_login()

    with open('passwd.pickle','rb') as f:
        session_list = pickle.load(f)
    tasks = [Baby(session) for session in session_list]

    p =Pool()
    print('Parent process %s.'%os.getpid())
    for item in tasks:
        p.apply_async(item.start)
    print('Waiting for all subprocesses done..')
    p.close()
    p.join()
    print('Done')

if __name__ =='__main__':
    main()
