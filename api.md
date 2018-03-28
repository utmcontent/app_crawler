# 掌通家园app api

## 获取排名
<table>
  <thead>
  <tr>
    <th>方法</th>
    <th>URL</th>
    <th>参数</th>
    <th>返回结果</th>
    <th>状态码</th>
  <tr>
  </thead>
  <tbody>
    <tr>
      <td>POST</td>
      <td>https://h5server.ztjy61.com/H5Server/rank/getBabyRanking/V2.0.0</td>
      <td>{studentId:''}</td>
      <td>{returncode":"10000","message":"操作成功","body":{...}}</td>
      <td>10000</td>
    </tr>
  </tbody>
<table>

## 获取未读消息条数　
<table>
  <thead>
  <tr>
    <th>方法</th>
    <th>URL</th>
    <th>参数</th>
    <th>返回结果</th>
    <th>状态码</th>
  <tr>
  </thead>
  <tbody>
    <tr>
      <td>POST</td>
      <td>https://zths.szy.cn/ZTHServer/message</td>
      <td>{reqcode:'协议号(1094)',reqcodeversion:'版本号[可选]　(5.3)'，＇body:'获取的消息类型列表，｛"msgtypelist":[{"msgtype":8},{"msgtype":9}｝'}</td>
      <td>{returncode":"10000","message":"操作成功","body":{"msgtypelist":[{"msgtype":8},{"msgtype":9}．．．}}
      {"returncode":"102","message":"cookie信息错误","body":{}}
      {"returncode":"0","message":"未知参数","body":{}}
      {"returncode":"101","message":"协议编号不能为空","body":{}}
      </td>
      <td>10000,102,0,101</td>
    </tr>
  </tbody>
<table>

＃＃　获取 babyinfo 宝宝的基本信息
<table>
  <thead>
  <tr>
    <th>方法</th>
    <th>URL</th>
    <th>参数</th>
    <th>返回结果</th>
    <th>状态码</th>
  <tr>
  </thead>
  <tbody>
    <tr>
      <td>POST</td>
      <td>https://zths.szy.cn/family/baby/list/1357/v1.0</td>
      <td>{reqcode:'协议号(1094)',reqcodeversion:'版本号[可选]　(5.3)'，＇body:'获取的消息类型列表，｛"msgtypelist":[{"msgtype":8},{"msgtype":9}｝'}</td>
      <td>{returncode":"10000","message":"操作成功","body":{"msgtypelist":[{"msgtype":8},{"msgtype":9}．．．}}
      {"returncode":"102","message":"cookie信息错误","body":{}}
      {"returncode":"0","message":"未知参数","body":{}}
      {"returncode":"101","message":"协议编号不能为空","body":{}}
      </td>
      <td>10000,102,0,101</td>
    </tr>
  </tbody>
<table>
