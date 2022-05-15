# coding=utf-8


import time
import requests, re
import data
"""
 可以改善的地方：
 1、添加再服务器上自动打卡，无需手动连网
 2、生成打卡日志，并将打卡信息发送到手机
 3、添加账号信息设置页面，能够方便为他人打卡
 4、为大量账号自动打卡


"""

# 姓名，学号，密码，学校编码
# name = "欧礼洪"
# stucode = "1913304129"
# password = "991023oulihong"
# schoolcode = "xmut"
state = 0
cooks = '默认'

def get_student_info():
    #  读取学生信息 姓名 学号 密码 学校
    global name, stucode, password, schoolcode
    try:
        name = data.read_date("student_info")[0].split("\n")[0]
        stucode = data.read_date("student_info")[1].split("\n")[0]
        password = data.read_date("student_info")[2].split("\n")[0]
        schoolcode = data.read_date("student_info")[3].split("\n")[0]
    except:
        print("无学生信息，请填写学生信息，并确认")
        name = ""
        stucode = ""
        password = ""
        schoolcode = ""
    print(name)
    print(stucode)
    print(password)
    print(schoolcode)

def login(retry=False):
    """获取处理后的数据
    :param user:用户信息
    :return : 传回登陆成功的cookie

    """
    try:
        get_student_info()  # 在此函数内读取用户信息
    except:
        print("找不到用户信息")

    try:
        url = "https://xiaoyuan.weishao.com.cn"
        csrf_html = requests.get(f"{url}/login?path=%2Fhome")
        csrf = re.compile('(?<=value=")(.+)(?=">)').search(csrf_html.text)[0]
        data = {"domain": schoolcode, "stuNo": stucode, "pwd": password, "vc": "", "_csrf": csrf}
        cook = "locale=zh; " + re.compile("xiaoyuan=(.+)(?=; P)").search(csrf_html.headers['set-cookie'])[0]
        head = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Cookie': cook,
        }
        res = requests.post(url + "/login/api/login", json=data, headers=head)
        errmsg = res.json().get("errmsg")
        if errmsg.find("错误") != -1:
            print(name + " " + errmsg)
            state = 1
            return "登录错误"
        cook2 = res.headers['set-cookie'].split(";")[0]

        head2 = {
            "Cookie": cook + "; " + cook2
        }
        res = requests.get(
            url + "/link?type=1&id=aa13361944680028&url=https%3A%2F%2Fyq.weishao.com.cn%2Fcheck%2Fquestionnaire",
            headers=head2,
            allow_redirects=False).headers["location"]
        cook3 = requests.get(res, allow_redirects=False).headers['set-cookie'].split(";")[0] + ";" + cook2
        # 　print(cook3)
        return cook3
    except requests.exceptions.ConnectionError as e:
        print("网络错误 1", e)
        state = 2
        return "网络错误2"
    except KeyError:
        if retry:
            print(name + " 登录错误3")
            state = 3
            return "登录错误3"
        else:
            return login(True)


def loging():
    global cooks
    cook = login()  # 登录微哨 获取cookie
    cooks = cook
    print(cooks)

def getdata():
    """获取处理后的数据

    :param studata:学生信息
    :param cook:传入的cookie
    :return : 昨天/上一次的打卡数据
    """
    # 只需要得到cookie即可获取信息
    url1 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionNaireList?sch_code={schoolcode}&stu_code={stucode}&authorityid=0&type=3&pagenum=1&pagesize=1000&stu_range=999&searchkey='
    head = {
        'Cookie': cooks,
    }
    # 获取 昨天/最新 的打卡信息
    info = requests.get(url1, headers=head).json().get("data")[0]
    # 如果今天已完成打卡
    if info.get("createtime") == time.strftime("%Y-%m-%d"):
        return 0
    private = info['private_id']
    activityid = str(info["activityid"])
    url2 = f'https://yq.weishao.com.cn/api/questionnaire/questionnaire/getQuestionDetail?sch_code={schoolcode}&stu_code={schoolcode}&activityid={activityid}&can_repeat=1&page_from=my&private_id={private}'
    # info里面存放着最新的的打卡记录
    info = requests.get(url2, headers=head).json().get("data")
    questions = info.get("question_list")
    private_id = info.get("last_private_id")
    flag = 0
    answers = []

    while flag < len(questions):
        answer = {
            "questionid": questions[flag].get("questionid"),
            "optionid": questions[flag].get("user_answer_optionid"),
            "optiontitle": 0,
            "question_sort": 0,
            'question_type': questions[flag].get("question_type"),
            "option_sort": 0,
            'range_value': "",
            "content": questions[flag].get("user_answer_content"),
            "isotheroption": questions[flag].get("otheroption"),
            "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
            "isanswered": questions[flag].get("user_answer_this_question"),
            "answerid": questions[flag].get("answerid"),
        }
        jump = 0
        type = answer["question_type"]

        if type == 1:
            for i in questions[flag].get("option_list"):
                if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                    answer["optiontitle"] = i.get("title")
                    if questions[flag].get("hsjump"):
                        jump = i.get("jumpid") - 1

        elif type in [3, 4, 7, 8, 9]:
            answer["optionid"] = 0
        answer["answered"] = answer["isanswered"]
        answers.append(answer)
        if jump:
            flag = jump
        else:
            flag += 1

    flag = 0
    totalArr = []
    while flag < len(questions):
        answer = {
            "questionid": questions[flag].get("questionid"),
            "optionid": questions[flag].get("user_answer_optionid"),
            "optiontitle": 0,
            "question_sort": 0,
            'question_type': questions[flag].get("question_type"),
            "option_sort": 0,
            'range_value': "",
            "content": questions[flag].get("user_answer_content"),
            "isotheroption": questions[flag].get("otheroption"),
            "otheroption_content": questions[flag].get("user_answer_otheroption_content"),
            "isanswered": questions[flag].get("user_answer_this_question")
        }
        type = answer['question_type']

        if type == 1 and answer["optionid"] != "":
            for i in questions[flag].get("option_list"):
                if answer["optionid"].isdigit() and i.get("optionid") == int(answer["optionid"]):
                    answer["optiontitle"] = i.get("title")
        elif type in [3, 4, 7, 8, 9]:
            answer["optionid"] = 0

        if questions[flag].get("user_answer_this_question"):
            answer["isanswered"] = True
            answer["answerid"] = questions[flag].get("answerid")
            answer["answered"] = answer["isanswered"]
        else:
            answer["hide"] = True
            answer["optionid"] = 0
            answer["isanswered"] = ''
            answer["answered"] = False

        totalArr.append(answer)
        flag += 1

    head['Referer'] = 'https://yq.weishao.com.cn/questionnaire'
    userinfo = requests.get("https://yq.weishao.com.cn/userInfo", headers=head).json().get("data")
    data = {
        "sch_code": userinfo.get("schcode"),
        "stu_code": userinfo.get("stucode"),
        "stu_name": userinfo.get("username"),
        "identity": userinfo.get("identity"),
        "path": userinfo.get("path"),
        "organization": userinfo.get("organization"),
        "gender": userinfo.get("gender"),
        "activityid": activityid,
        "anonymous": 0,
        "canrepeat": 1,
        "repeat_range": 1,
        "question_data": answers,
        "totalArr": totalArr,
        "private_id": private_id
    }
    return data


def run():
    """获取处理后的数据
    :param studata:学生信息
    :param cook:传入的cookie
    :return :打卡结果
    """
    # 读取个人提交信息
    info = getdata()
    if info == 0:
        print("今日打卡已完成，自动打卡取消\n")
        return "已完成"
    # 提交今日打卡
    url = 'https://yq.weishao.com.cn/api/questionnaire/questionnaire/addMyAnswer'
    head = {
        'Content-Type': 'application/json',
        'Cookie': cooks,
    }
    data = requests.post(url, json=info, headers=head).json()
    if data.get("errcode") == 0:
        print("打卡成功！")
        sendMsgToQQ()  # 打卡完成就发送消息给QQ
        return "成功！"
    else:
        print("---未知的errcode\n" + str(data) + "\n")
        return "未知结果"


def sendMsgToQQ():
    """有效期：2029-12-31 23:59:59
    TOKEN：ZMEWYMNJOTLJMMEXNZA5OWY1NTDKZMI2
    示    例：http://push.weitip.com/qq/task/sendMsg?token=ZMEWYMNJOTLJMMEXNZA5OWY1NTDKZMI2&number=1756950720&message=Hello,Qpush!
    注意：每日限三条
    """
    # 打卡时间
    date = time.strftime("%Y/%m/%d")
    # qq账号
    qqnumber = '1756950720'
    # 发送内容
    if state == 0:
        sendmsg = '打卡成功'  # 大概只会看见打卡成功的消息，因为失败的话就发送不了这个消息（doge）
    elif state == 1:
        sendmsg = '登录错误'
    elif state == 2:
        sendmsg = '网络错误'
    elif state == 3:
        sendmsg = '登录失败'
    # requests 提供的接口地址
    request_url = 'http://push.weitip.com/qq/task/sendMsg?token=ZMEWYMNJOTLJMMEXNZA5OWY1NTDKZMI2&number=' + \
                  qqnumber + '&message=' + \
                  date + '\n' + \
                  sendmsg
    print(sendmsg)
    # 返回的请求
    response = requests.post(url=request_url)
    print(response.text)

"""
if __name__ == '__main__':
    # 获取用户cookie
    cook = login()  # 登录微哨
    cooks = cook
    print(cook)
    run()  # 尝试进行打卡
    sendMsgToQQ()  # 打卡完成就发送消息给QQ
    print("完成")
"""

