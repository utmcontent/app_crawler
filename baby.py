import requests,json
from requests.exceptions import RequestException
from config import *
from datetime import date
def get_json(url,data="{}",headers=HEADERS,cookies=COOKIES):
    try:
        response = requests.post(url,data=data,headers=headers,cookies=cookies)
        response.raise_for_status()
        return json.loads(response.text)
    except RequestException as err:
        print(err)


def get_baby_info_list():
    url='https://zths.szy.cn/family/baby/list/1343/v3.0'
    return get_json(url)


def get_all_growth(cid,filter='1,2,3'):
    url ='https://zths.szy.cn/ZTHServer/growup/list',
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded;charset=utf-8"
    data = {}
    data['reqcode']='1124'
    data['reqcodeversion']='5.3'
    data['body']='{"number":20,"pageindex":1,"childid":"%s","covernum":1,"filter":"%s","labelname":""}'%(cid,filter)
    return get_json(url,data=data,headers=headers)
def get_userid():
    url="https://zths.szy.cn/ZTHServer/userinfo/init"
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
    data = {}
    data['reqcode'] ='1057'
    data['reqcodeversion']='5.3'
    data['body']="{}"
    return get_json(url,data=data,headers=headers).get('body').get('userid')

def un_star(commentid,archivesid,childid):
    url="https://zths.szy.cn/ZTHServer/growup/delcomment"
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
    data = {}
    data['reqcode'] ='1120'
    data['reqcodeversion']='5.3'
    data['body']='{"commentid":"%s","archivesid":"%s","childid":"%s"}'%(commentid,archivesid,childid)
    return get_json(url,data=data,headers=headers)

def star(archivesid,childid,userid):
    url="https://zths.szy.cn/ZTHServer/growup/pointpraise"
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
    data = {}
    data['reqcode'] ='1122'
    data['reqcodeversion']='5.3'
    data['body']='{"archivesid":"%s","childid":"%s","classalbumid":0,"userid":"%s",}'%(archivesid,childid,userid)
    return get_json(url,data=data,headers=headers)

def post_grouth(textcontent):
    url="https://zths.szy.cn/ZTHServer/growup/add"
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
    data = '''reqcode=1119&reqcodeversion=5.3&body={"studentid":"463cf42a48ea1cd573cf","childid":"05b1a4624bd71f15044d","archivestype":2,"textcontent":"%s","recordtime":"%s","addrstr":"","addrlng":"0.0","addrlat":"0.0","sendtype":0,"musicurl":"","musicname":"","labelids":"502022"}'''%(textcontent,date.today().__str__())
    return get_json(url,data=data,headers=headers)

def dele_my_post_grouth(growid):
    url="https://zths.szy.cn/ZTHServer/growup/delgrowth"
    headers = HEADERS.copy()
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=utf-8"
    data = '''reqcode=1139&reqcodeversion=5.3&body={"growthid":%s}'''%(growid)
    return get_json(url,data=data,headers=headers)

def login(userphone,password):
    url='https://zths.szy.cn/login/parent/1000/v1.0'

    data ='''{"password":"%s","apptype":1,"devkey":"b8fe01a2-ab90-4427-b15f-b25ffc44fddd","versionnum":"5.4.0","devtype":3,"logintype":"1","pwd2":"e10adc3949ba59abbe56e057f20f883e","account":"%s","release":"1","oemid":"1"}'''%(password,userphone)
    return get_json(url,data=data)
if __name__ =='__main__':

    # pass_word='456bf69de5d1b3588d61a91143524b8c'
    # phone ='13480748741'
    # print(login(phone,pass_word))

    # baby_info = get_baby_info_list()
    # #  studentid,babyuid,
    # info =baby_info['body']['babyinfolist'][0]
    # studentId=info['studentid']
    # babyId=info['babyuid']
    # list_growth = get_all_growth(babyId,'1')
    #
    # # albumcover 相册封面  albumcover.coverlist
    # # growthcount  总数量
    # # grouthnews 各个的数量
    # # groupuplist
    # uid = get_userid()
    # growthuplist = list_growth['body']['growuplist']
    # my_post_growth = [x for x in growthuplist if x['userid']==uid] # 找到自己发的动态 时间倒叙
    # last_post_growth_id = my_post_growth.pop(0).get('archivesid')
    #
    # # print(dele_my_post_grouth(last_post_growth_id)) # 删除动态
    # # post_success = post_grouth('hello')
    # # print(post_success)
    # # growthuplist.filter
    # #
    #
    # # for item in growthuplist:
    # #     # data = un_star(item['mypointid'],item['archivesid'],item['childid'],)
    # #     data = star(item['archivesid'],item['childid'],uid)
    # #     print(data)
    #
    # # 每天任务
    # # 打开掌通家园
    # # 发送成长印记 删除成长印记 混分
    # #
    # # 每周任务
    # # 给老师点赞  先取消全部老师再点赞全部老师
    # # 查看信息
    # #
    # #无法登录
