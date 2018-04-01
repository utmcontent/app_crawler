# 宝宝的掌通家园 app 自动控制

### 该app使用邀请的方式注册,每个手机号可以被邀请为一个账号

#### 登录
    POST https://zths.szy.cn/login/parent/1000/v1.0 HTTP/1.1
    Cookie: JSESSIONID=xxxxxxxxxxxxseesionid;ClientVersion=5.4.0
    SVER: 3
    User-Agent: zhang tong jia yuan/5.4.0(Android)
    Content-Type: application/json; charset=utf-8
    Content-Length: 248
    Host: zths.szy.cn
    Connection: Keep-Alive
    Accept-Encoding: gzip

    {"password":"456bf69de5d1b3588d61a91143524b8c","apptype":1,"devkey":"b8fe01a2-ab90-4427-b15f-b25ffc44fddd","versionnum":"5.4.0","devtype":3,"logintype":"1","pwd2":"e10adc3949ba59abbe56e057f20f883e","account":"134xxxxxx","release":"1","oemid":"1"}


password 密码的加密之后的值,devkey:手机的imei值
pwd2,可能是加密的参数,account:手机账号
登录认证采用的是session/cookie
手机号,密码密文,还有设备号填入family_numbers.txt 中,逗号隔开,用来多开的自动登录


#### 每日首次登录
    POST https://zths.szy.cn/ZTHServer/app/logineverydayonetimes HTTP/1.1
    Cookie: JSESSIONID=xxxxxxxxxxsessid;ClientVersion=5.4.0
    SVER: 3
    User-Agent: zhang tong jia yuan/5.4.0(Android)
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Content-Length: 43
    Host: zths.szy.cn
    Connection: Keep-Alive
    Accept-Encoding: gzip

    reqcode=1236&reqcodeversion=5.3&body={}

   reqcode:路由id,每个登录之后的请求各不相同

#### 给消息点赞
    POST https://zths.szy.cn/ZTHServer/growup/pointpraise HTTP/1.1
    Cookie: JSESSIONID=xxxxxxxseesion;ClientVersion=5.4.0
    SVER: 3
    User-Agent: zhang tong jia yuan/5.4.0(Android)
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Content-Length: 192
    Host: zths.szy.cn
    Connection: Keep-Alive
    Accept-Encoding: gzip

    reqcode=1122&reqcodeversion=5.3&body=%7B%22archivesid%22%3A110341361%2C%22childid%22%3A%2205b1a4624bd71f15044d%22%2C%22classalbumid%22%3A59751347%2C%22userid%22%3A%22c692860d43ffbfd7977e%22%7D


    body参数 archivesid 文章id,childid 宝宝id,classlbuid:教室班级id,userid:用户id

#### 发成长圈微博

    POST https://zths.szy.cn/ZTHServer/growup/add HTTP/1.1
    Cookie: JSESSIONID=xxxxxxsessid;ClientVersion=5.4.0
    SVER: 3
    User-Agent: zhang tong jia yuan/5.4.0(Android)
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Content-Length: 414
    Host: zths.szy.cn
    Connection: Keep-Alive
    Accept-Encoding: gzip

    reqcode=1119&reqcodeversion=5.3&body=%7B%22studentid%22%3A%22463cf42a48ea1cd573cf%22%2C%22childid%22%3A%2205b1a4624bd71f15044d%22%2C%22archivestype%22%3A2%2C%22textcontent%22%3A%22111%22%2C%22recordtime%22%3A%222018-03-28%22%2C%22addrstr%22%3A%22%22%2C%22addrlng%22%3A%220.0%22%2C%22addrlat%22%3A%220.0%22%2C%22sendtype%22%3A0%2C%22musicurl%22%3A%22%22%2C%22musicname%22%3A%22%22%2C%22labelids%22%3A%22502022%22%7D


   studentid 学生id,childid 宝宝id,archivestype,发送内容类型,textcontent,文字内容,recordtime,定义的时间,    
   labelid 标签id ...


#### 切换设备请求短信
    POST https://zths.szy.cn/ZTHServer/sms HTTP/1.1
    Cookie: JSESSIONID=xxxxsession;ClientVersion=5.4.0
    SVER: 3
    User-Agent: zhang tong jia yuan/5.4.0(Android)
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Content-Length: 43
    Host: zths.szy.cn
    Connection: Keep-Alive
    Accept-Encoding: gzip

    reqcode=1030&reqcodeversion=5.3&body=%7B%7D



### 收到设备后发送短信验证
POST https://zths.szy.cn/ZTHServer/sms HTTP/1.1
Cookie: JSESSIONID=xxxsessid;ClientVersion=5.4.0
SVER: 3
User-Agent: zhang tong jia yuan/5.4.0(Android)
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Content-Length: 190
Host: zths.szy.cn
Connection: Keep-Alive
Accept-Encoding: gzip

reqcode=1031&reqcodeversion=5.3&body=%7B%22transactionindex%22%3A%22CFFE7E22-DBAD-4132-BA0E-7AC79624D541%22%2C%22checkid%22%3A%223146%22%2C%22devtype%22%3A%222%22%2C%22pushkey%22%3A%22%22%7D

checkid 收到的短信验证码



 ***更多内容待抓取,更新***


## 方法
    1.使用wireshark 或者fiddler监听手机wifi上网的网卡,用手机访问app时,
    截取发送的http/https请求保存,提取url,post参数.
    2.在task_queue/process.py中 新建要执行的任务    
```ptyhon
    class SomeAction(TaskInterface):    
      priority=5 #任务执行的优先级
      name = "some thing " #任务名称    
      def run(self):        
          #添加任务,如查看所有文章,删除发的内容,点赞
          self.star() #例如 star       

      def star(self):        
        url='star_url'    
        data='star_post_form_data'
        return self.get_json(url,data=data)
```
*每个动作只需要找到该动作的请求url和请求参数就可以通过获取到该url的资源信息*




---

工具python3
* requests
* multiprocessing    #多核cpu可以使用进程池加速爬取速度
* queue.PriorityQueue
