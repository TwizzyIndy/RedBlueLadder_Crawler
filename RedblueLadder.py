#!/usr/bin/env python3

"""

redblueladdertool by TwizzyIndy
on 1/2020

"""

import os
import logging
import json
import requests
from colorama import Fore, Back, Style
from threading import Thread, Event, Timer
import datetime
import math
import re

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=f'{Style.DIM}%(asctime)s{Style.RESET_ALL} %(message)s')

curr_time = 0
def_time = 0
user_time = 0
view_time = 0
regame_time = 0

g_login_cookie = []

""" betting infos global variables """
gMoney = ""
gPoint = ""
bet_date = ""
bet_atime = ""
mb_id = ""
IG_Idx = ""
sadari_min = ""
sadari_max = ""
limit_min = ""
limit_max = ""
clac_type = ""
bet_type = ""

""" login global variables """

g_username = ""
g_password = ""

"""
betting options for Red and Blue

BLUE 1.95 : <a class='btn_bet_1 s_games game_0 game0_1 betting_submit' gidx='1852263' betting='1' game='1' bmax='500000' togglename='game0_1' rate='1.95'>1.95</a>
RED 1.95 : <a class='btn_bet_2 s_games game_0 game0_1 betting_submit' gidx='1852263' betting='2' game='2' bmax='500000' togglename='game0_1' rate='1.95'>1.95</a>
3LINE BLUE 1.95 : <a class='btn_bet_3 s_games game_0 game0_2 betting_submit' gidx='1852265' betting='1' game='3' bmax='500000' togglename='game0_2' rate='1.95'>1.95</a>
4LINE RED 1.95 : <a class='btn_bet_4 s_games game_0 game0_2 betting_submit' gidx='1852265' betting='2' game='4' bmax='500000' togglename='game0_2' rate='1.95'>1.95</a>
BLUE LEFT 1.95 : <a class='btn_bet_5 s_games game_0 game0_3 betting_submit' gidx='1852264' betting='1' game='5' bmax='500000' togglename='game0_3' rate='1.95'>1.95</a>
RED RIGHT 1.95 : <a class='btn_bet_6 s_games game_0 game0_3 betting_submit' gidx='1852264' betting='2' game='6' bmax='500000' togglename='game0_3' rate='1.95'>1.95</a>
BLUE 3LINE + BLUE LEFT 3.8 : <a class='btn_bet_7 s_games game_0 game0_4 betting_submit' gidx='1852266' betting='1' game='7' bmax='500000' togglename='game0_4' rate='3.8'>3.8</a>
RED 4LINE + BLUE LEFT 3.8 :<a class='btn_bet_8 s_games game_0 game0_4 betting_submit' gidx='1852266' betting='2' game='8' bmax='500000' togglename='game0_4' rate='3.8'>3.8</a>
BLUE 3LINE + RED RIGHT 3.8 : <a class='btn_bet_9 s_games game_0 game0_5 betting_submit' gidx='1852267' betting='1' game='9' bmax='500000' togglename='game0_5' rate='3.8'>3.8</a>
RED 4LINE + RED RIGHT 3.8 : <a class='btn_bet_10 s_games game_0 game0_5 betting_submit' gidx='1852267' betting='2' game='10' bmax='500000' togglename='game0_5' rate='3.8'>3.8</a>

"""


def bet_red_195():
    global gMoney, gPoint, mb_id, IG_Idx, g_login_cookie, sadari_max, sadari_min, limit_max, limit_min, clac_type, bet_type, curr_time
    global g_username

    try:
        response = requests.post(
            url="http://win00.vvip7.com/game/ladder/ladder.asp",
            headers={
                "Accept-Encoding": "utf-8",
                "Cookie": g_login_cookie,
                "Accept": "application/json,application/javascript, */*, q=0.01",
                "Referer": "http://win00.vvip7.com/m/game/betgame_s.asp",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "http://win00.vvip7.com/m/game/betgame_s.asp",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Accept-Language": "en-US",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
            },
            data={
                "bet_date": str(datetime.date.today()),
                "clac_type": "B",
                "bet_atime": curr_time,  # "181",
                "bet_gtype": "0",
                "limit_min": limit_min,
                "bet_type": "non_mixed",
                "Benefit": "1.95",
                "sadari_min": sadari_min,
                "limit_max": limit_max,
                "gpoint": gPoint,
                "gmoney": gMoney,
                "betting": "2",
                "betting_money": "1000",  # TODO: make dynamic if need
                "mb_id": g_username,
                "ICT_BetNum": "2",
                "IG_Idx": IG_Idx,
                "sadari_max": sadari_max,
            },
        )

        reply = json.loads(response.content.decode('utf-8'))
        print(reply["msg"])

    except requests.exceptions.RequestException:
        print("request exception")
    return


def bet_blue_195():
    global gMoney, gPoint, mb_id, IG_Idx, g_login_cookie, sadari_max, sadari_min, limit_max, limit_min, clac_type, bet_type, curr_time
    global g_username, g_password

    try:
        response = requests.post(
            url="http://win00.vvip7.com/game/ladder/ladder.asp",
            headers={
                "Accept-Encoding": "utf-8",
                "Cookie": g_login_cookie,
                "Accept": "application/json,application/javascript, */*, q=0.01",
                "Referer": "http://win00.vvip7.com/m/game/betgame_s.asp",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "http://win00.vvip7.com/m/game/betgame_s.asp",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Accept-Language": "en-US",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
            },
            data={
                "bet_date": str(datetime.date.today()),
                "clac_type": "B",
                "bet_atime": curr_time,  # "181",
                "bet_gtype": "0",
                "limit_min": limit_min,
                "bet_type": "non_mixed",
                "Benefit": "1.95",
                "sadari_min": sadari_min,
                "limit_max": limit_max,
                "gpoint": gPoint,
                "gmoney": gMoney,
                "betting": "1",
                "betting_money": "1000",  # TODO: make dynamic if need
                "mb_id": g_username,
                "ICT_BetNum": "1",
                "IG_Idx": IG_Idx,
                "sadari_max": sadari_max,
            },
        )

        reply = json.loads(response.content.decode('utf-8'))

        print(reply["msg"])

    except requests.exceptions.RequestException:
        print("request exception")
    return


def get_betting_infos():
    """
    get infos from GET http://win00.vvip7.com/m/game/betgame_s.asp
    gmoney *
    gpoint *
    betting_money
    bet_gtype
    bet_date *
    bet_atime *
    betting *
    mb_id *
    sadari_min *
    sadari_max *
    limit_min *
    limit_max *
    clac_type *
    bet_type *
    IG_Idx *
    ICT_BetNum
    Benefit
    :return:
    """
    global gMoney, gPoint, mb_id, IG_Idx, g_login_cookie, sadari_max, sadari_min, limit_max, limit_min, clac_type, bet_type

    try:
        response = requests.get(
            url="http://win00.vvip7.com/m/game/betgame_s.asp",
            headers={
                "Accept-Encoding": "utf-8",
                "Cookie": g_login_cookie,
                "Accept": "application/json,application/javascript, */*, q=0.01",
                "Referer": "http://win00.vvip7.com/m/",
                "Origin": "http://win00.vvip7.com/m/",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
                "Accept-Language": "en-US",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
            },
        )

        if response.status_code is not 200:
            print(response.content)
            return

        # get page content first
        page = response.content.decode('utf-8').strip()

        # get gMoney
        index_gMoney = page.find("id=\"gmoney\" value=\"")
        if index_gMoney == -1:
            print("cant find gMoney on page")

        line = page[index_gMoney:index_gMoney + 25]  # 6 Digits only now (e.g 500000 )
        value = re.findall('"([^"]*)"', line)[1]
        gMoney = value
        # print("gMoney : " + gMoney)

        # get gpoint
        index_gPoint = page.find("id=\"gpoint\" value=\"")
        if index_gPoint == -1:
            print("cant find gPoint on page")

        line = page[index_gPoint:index_gPoint + 25]
        value = re.findall('"([^"]*)"', line)[1]
        gPoint = value
        # print("gPoint : " + gPoint)

        # get mb_id
        index_mbID = page.find("id=\"mb_id\" value=\"")
        if index_mbID == -1:
            print("cant find mb_id on page")

        line = page[index_mbID:index_mbID + 29]  # 10 chars username
        value = re.findall('"([^"]*)"', line)[1]
        mb_id = value
        # print("mb_id : " + mb_id)

        # get IG_Idx
        index_gidx = page.find("class='btn_bet_2 s_games game_0 game0_1 betting_submit' gidx='")
        if index_gidx == -1:
            print("cant find gidx on page")

        line = page[index_gidx:index_gidx + 70]  # including 8 digits
        value = re.findall('\'([^\']*)\'', line)[1]
        IG_Idx = value
        # print("IG_Idx : " + IG_Idx)

        # get sadari_min
        index_sadari_min = page.find("id=\"sadari_min\" value=\"")
        if index_sadari_min == -1:
            print("cant find sadari_min on page")

        line = page[index_sadari_min:index_sadari_min + 29]  # 4 digits
        value = re.findall('"([^"]*)"', line)[1]
        sadari_min = value
        # print("sadari_min : " + sadari_min)

        # get sadari_max
        index_sadari_max = page.find("id=\"sadari_max\" value=\"")
        if index_sadari_max == -1:
            print("cant find sadari_max on page")

        line = page[index_sadari_max:index_sadari_max + 33]  # 7 digits
        value = re.findall('"([^"]*)"', line)[1]
        sadari_max = value
        # print("sadari_max : " + sadari_max)

        # get limit_min
        index_limit_min = page.find("id=\"limit_min\" value=\"")
        if index_limit_min == -1:
            print("cant find limit_min on page")

        line = page[index_limit_min:index_limit_min + 28]  # 5 digits
        value = re.findall('"([^"]*)"', line)[1]
        limit_min = value
        # print("limit_min : " + limit_min)

        # get limit_max
        index_limit_max = page.find("id=\"limit_max\" value=\"")
        if index_limit_max == -1:
            print("cant find limit_max on page")

        line = page[index_limit_max:index_limit_max + 33]  # 6 digits
        value = re.findall('"([^"]*)"', line)[1]
        limit_max = value
        # print("limit_max : " + limit_max)

        # get clac_type
        index_clac_type = page.find("id=\"clac_type\" value=\"")
        if index_clac_type == -1:
            print("cant find clac_type on page")

        line = page[index_clac_type:index_clac_type + 26]  # 1 char
        value = re.findall('"([^"]*)"', line)[1]
        clac_type = value
        # print("clac_type : " + clac_type)

        # get bet_type
        index_bet_type = page.find("id=\"bet_type\" value=\"")
        if index_bet_type == -1:
            print("cant find bet_type on page")

        line = page[index_bet_type:index_bet_type + 32]  # 9 char
        value = re.findall('"([^"]*)"', line)[1]
        bet_type = value
        # print("bet_type : " + bet_type)

        # TODO: ICT_BetNum for wide betting but now its now only 2

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return


def login(user_id, user_passwd):
    # POST http://win00.vvip7.com/Login/Login_Proc.asp

    global g_login_cookie

    try:
        response = requests.post(
            url="http://win00.vvip7.com/Login/Login_Proc.asp",
            headers={
                "Accept-Encoding": "utf-8",
                "Cookie": "__cfduid=de90b27183e4a8380ec3aba560eaf43a11579590108; ASPSESSIONIDASACTSAT=OAPDBDBDCMDLMAMOFKHFABMP; _ga=GA1.2.2038594054.1579590109; _gid=GA1.2.1088972013.1579590109; ladder_sound=on; ASPSESSIONIDAQCDQQCT=HAKBHOMDFHBCOJKAEGPJGEOO",
                "Accept": "application/json",
                "Referer": "http://win00.vvip7.com/m/",
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                "Accept-Language": "en-US",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
            },
            data={
                "IU_ID": user_id,
                "IU_PW": user_passwd,
            },
        )

        if response.status_code != 200:
            print(response.content)

        # for cookie in response.cookies:
        #    g_login_cookie = cookie

        for cookie in response.cookies:
            g_login_cookie = cookie.name + '=' + cookie.value

        # print(g_login_cookie)

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return


def get_regame_time():
    r"""
    get regame time from page
    :return:
    """
    global regame_time

    try:
        res = requests.get(url="http://win00.vvip7.com/game/ladder/v2_index.asp",
                           headers={
                               "Accept-Encoding": "utf-8",
                               "Cookie": "__cfduid=de90b27183e4a8380ec3aba560eaf43a11579590108; ASPSESSIONIDASACTSAT=OAPDBDBDCMDLMAMOFKHFABMP; _ga=GA1.2.2038594054.1579590109; _gid=GA1.2.1088972013.1579590109; ladder_sound=on; ASPSESSIONIDAQCDQQCT=HAKBHOMDFHBCOJKAEGPJGEOO",
                               "Accept": "application/json",
                               "Referer": "http://win00.vvip7.com/m/",
                               "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                               "Accept-Language": "en-US",
                               "X-Requested-With": "XMLHttpRequest",
                               "DNT": "1",
                           },
                           )

        if res.status_code is not 200:
            logger.info("response error : {content}".format(content=res.content))
            return

        page = res.content.decode('utf-8').strip()
        index_start = page.find('var regame_time =')

        if index_start == -1:
            print("cant find index_start")
            return
        line = page[index_start:index_start + 22]
        value = line.split('=')[1].replace(';', '')

        regame_time = int(value.strip())

    except requests.exceptions.RequestException:
        print("error")


def now_timer():
    r"""
    get server time
    :return:
    """

    global curr_time, def_time, user_time, view_time

    browser_time = datetime.datetime.now()
    bt_hh = browser_time.hour * 3600
    bt_ii = browser_time.minute * 60
    bt_ss = browser_time.second
    user_time = bt_hh + bt_ii + bt_ss

    try:
        res = requests.post(url="http://win00.vvip7.com/game/ladder/ajax/timer.asp",
                            headers={"Accept-Encoding": "utf-8",
                                     "Cookie": "__cfduid=de90b27183e4a8380ec3aba560eaf43a11579590108; ASPSESSIONIDASACTSAT=OAPDBDBDCMDLMAMOFKHFABMP; _ga=GA1.2.2038594054.1579590109; _gid=GA1.2.1088972013.1579590109; ladder_sound=on; ASPSESSIONIDAQCDQQCT=HAKBHOMDFHBCOJKAEGPJGEOO",
                                     "Accept": "application/json",
                                     "Referer": "http://win00.vvip7.com/m/",
                                     "Accept-Language": "en-US",
                                     "X-Requested-With": "XMLHttpRequest",
                                     "DNT": "1",
                                     },
                            )
        if res.status_code is not 200:
            logger.info("response error : {content}".format(content=res.content))
            return

        s = res.content.decode('utf-8')
        s = s.replace('\'', '\"')  # skip json decode error while parsing single quote in response
        jsReply = json.loads(s)
        curr_time = jsReply['curr_time']
        def_time = user_time - curr_time
        view_time = user_time - def_time

    except requests.exceptions.RequestException:
        print("error")

    return


def fetching_result():
    r"""

    fetching RED, BLUE result in every 1 second

    :return: None
    """

    global curr_time, def_time, user_time, view_time, regame_time

    try:
        response = requests.get(
            url="http://win00.vvip7.com/data/json/ladder/dist.asp",
            headers={
                "Accept-Encoding": "utf-8",
                "Cookie": "__cfduid=de90b27183e4a8380ec3aba560eaf43a11579590108; ASPSESSIONIDASACTSAT=OAPDBDBDCMDLMAMOFKHFABMP; _ga=GA1.2.2038594054.1579590109; _gid=GA1.2.1088972013.1579590109; ladder_sound=on; ASPSESSIONIDAQCDQQCT=HAKBHOMDFHBCOJKAEGPJGEOO",
                "Accept": "application/json",
                "Referer": "http://win00.vvip7.com/game/ladder/v2_index.asp",
                "Accept-Language": "en-US",
                "X-Requested-With": "XMLHttpRequest",
                "DNT": "1",
            },
        )

        if response.status_code is not 200:
            logger.info("response error : {content}".format(content=response.content))

        # logger.info("response : {content}".format(content=Fore.RED + str(response.content) ))

        jsReply = json.loads(response.content.decode('utf-8'))
        evenNumber = int(jsReply['e'])  # RED
        oddNumber = int(jsReply['o'])   # BLUE

        # TODO: identify here, whos better

        logger.info("{:4} : {:10}".format(Fore.BLUE + 'BLUE', str(oddNumber)))
        logger.info("{:3} : {:10}".format(Fore.RED + 'RED', str(evenNumber)))

        now_timer()

        hh = math.floor(view_time / 3600)
        ii = math.floor((view_time % 3600) / 60)
        ss = math.floor((view_time % 3600) % 60)
        if hh < 10:
            hh = "0" + str(hh)
        if ii < 10:
            ii = "0" + str(ii)
        if ss < 10:
            ss = "0" + str(ss)

        get_regame_time()
        regame_ii = math.floor((regame_time % 3600) / 60)
        regame_ss = math.floor((regame_time % 3600) % 60)

        # TODO: if regame time is near 20 second, identify whos better and bet
        if regame_ii is 0 and regame_ss < 30:
            logger.info("{:16} ITS TIME TO BET".format(Fore.WHITE))

        logger.info("SERVER TIME => {:2}:{:2}:{:2}".format(Fore.YELLOW + str(hh), Fore.YELLOW + str(ii), str(ss)))

        # TODO: if server time got 5 mins or exceeds, load the result.asp

        logger.info("REMAINING TIME => {:2}:{:2}\n".format(Fore.YELLOW + str(regame_ii), str(regame_ss)))

        get_betting_infos()

    except requests.exceptions.RequestException:
        print('HTTP Request failed')

    return


class GetGraphThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):  # 1 second here
            fetching_result()


"""

server time : http://win00.vvip7.com/game/ladder/ajax/timer.asp
ladder swf  : http://win00.vvip7.com/game/ladder/ladder.swf

betting js  : http://win00.vvip7.com/main_files/sadari_m.js


"""


def main():
    global g_username, g_password

    g_username = input("username : ")
    g_password = input("password : ")

    login(g_username, g_password)

    # get Red, Blue Graph result
    stopFlag = Event()
    thread = GetGraphThread(stopFlag)
    thread.start()

    try:
        input()
    except KeyboardInterrupt:
        stopFlag.set()
        pass
    finally:
        logger.info(" end ")


if __name__ == "__main__":
    main()
