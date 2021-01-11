#--------------Tile----------------------------------------#
__author__ = "QC"
__title__ ="List Function"
__desc__="""
    Tong hop danh sach cac function test Feature
"""
#--------------End Tile------------------------------------#
#--------------Import LIB----------------------------------#
import json
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.cocosjs import CocosJsPoco
from poco.exceptions import PocoTargetTimeout
#--------------End Import Lib------------------------------#
#--------------Import FILE---------------------------------#
# from Lavuavi.Config.Api import *
#link cheat:
from Laviuda.Config.Api import *
#----------------------------------------------------------#
from Laviuda.Config.config import *
from Laviuda.Report.report import *
from Laviuda.Img.img import *
from Laviuda.Poco.poco import *
#--------------End Import FILE-----------------------------#
#--------------Connect Device------------------------------#

if not cli_setup():
    auto_setup(__file__)
    
#--------------End Connect---------------------------------#
#--------------Poco----------------------------------------#

poco = CocosJsPoco()

#--------------End Poco------------------------------------#
# script content
#--------------bien----------------------------------------#

#-------------end bien-------------------------------------#
#----------------------------Function-------------------------------------------------#
#Function general:----------------->
#highlight
def killApp():
    try:
        clear_app("com.zingplay.laviuda")
        print('kill App')
        return True
    except:
        print('error kill App')
        return False
def openApp():
    try:
        start_app("com.zingplay.laviuda")
        print('open App')
        return True
    except:
        print('error open App')
        return False
def waitNoLimit(obj,time):
    try:
        wait(obj,time,0.5)
        return True 
    except:
        return False
def waitNolimitPoco(obj,time):
    return obj.wait(time).exists()
def pipeSubGold(strGold):
    gold=0
    lenght = len(strGold)-1
    gold= float(strGold[0:lenght])
    if strGold[lenght:len(strGold)]=='K':
        gold=gold*1000
    elif strGold[lenght:len(strGold)]=='M':
        gold=gold*1000000
        print(type(gold))
    elif strGold[lenght:len(strGold)]=='B':
        gold=gold*1000000000
    else:
        gold=float(strGold)
    return gold
def fortmartTime(time):
    timeStr= str(time['D'])+"/"+str(time['M'])+"/"+str(time['Y'])+" "+str(time['h'])+":"+str(time['m'])+":"+str(time['s'])
    print(timeStr)
    return timeStr
#cheat
def cheatGoldEmpty(gold):
    try:
        pocoTag.btnCheat.click()
        if exists(imageWC.imgGoldCheat):
            touch(imageWC.imgGoldCheat)
        else:
            touch(imageWC.imgGoldCheat1)
        text(str(gold))
        pocoTag.btnSendCheatPlayer.click()
        pocoTag.btnCheat.click()
        print("Cheat tien thanh cong")
        return True
    except:
        print("Khong tim thay")
        return False
# Action
def reloadLobby():
    try:
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        sleep(1)
        pocoTag.btnLeaveGame.click()
        print('reload lobby')
        return True
    except:
        print('error reload lobby')
        return False
def reloadLoby2():
    poco = CocosJsPoco()
    poco.click([0.04817596456992819, 0.9241753578186035])
    pocoTag.btnHide.click()
def closeEvent():
    try:
        sleep(1)
        poco = CocosJsPoco()
        if waitNolimitPoco(pocoTag.btnClose,1):
            pocoTag.btnClose.click()
    except:
        print("error close ev")
def out():
    try:
        poco = CocosJsPoco()
        pocoTag.btnSetting.click()
        sleep(1)
        wait(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgBtnOut)
        touch(imageInOutAcc.imgOutOk)
        print("out")
    except:
        print("error out")
def changeAcc(userN,passW):
    try:
        out()
        poco = CocosJsPoco()
        pocoTag.btnSwitch.click()
        pocoTag.inputUser.click()
        sleep(1)
        text("")
        pocoTag.inputUser.click()
        sleep(1)
        User=str(userN)
        text(User)
        pocoTag.logo.click()
        pocoTag.inputPass.click()
        PassW=str(passW)
        text(PassW)
        pocoTag.logo.click()
        pocoTag.btnLogin.click()
        return True
    except:
        print("error login")
        return False
def joinTable():
    try:
        sleep(2)
        poco = CocosJsPoco()
        pocoTag.btnPlay.click()
        print("joinTable")
        return 1
    except:
        print("error joinTable")
        return 0
def clickOutTable():
    try:
        poco = CocosJsPoco()
        pocoTag.btnLeaveGame.click()
        print("register back")
        return True
    except:
        print("error register back")
        return False
def addBot():
    try:
        poco = CocosJsPoco()
        pocoTag.btnCheat.click()
        for i in range(2):
            sleep(1)
            pocoTag.btnAddBot.click()
        pocoTag.btnCheat.click()
        print("event addBot")
        return True
    except:
        print("error addBot")
        return False
def clickKnock():
    try:
        if waitNolimitPoco(pocoTag.btnKnock,60):
            pocoTag.btnKnock.click()
            print("event clickKnock")
            return True
        else:
            print("end countdown time")
            return False
    except:
        print("error clickKnock")
        return False
def clickPass():
    try:
        if waitNolimitPoco(pocoTag.btnPass,60):
            pocotag.btnPass.click()
            print("pass")
            return True
        else:
            print("no find btn pass")
            return False  
    except:
        print("error Pass")
        return False
def clickExchange1():
    try:
        if waitNolimitPoco(pocoTag.btnExchange1,60):
            pocoTag.btnExchange1.click()
            sleep(1)
            poco.click([0.6264933239634575, 0.8615635156631469])
            sleep(1)
            poco.click([0.6602340558843552, 0.4599999904632568])
            sleep(1)
            pocoTag.btnSwap.click()
            print("event Exchange1")
            return True
        else:
            print("end countdown time")
            return False  
    except:
        print("error Exchange1")
        return False
def clickExchange5():
    try:
        if waitNolimitPoco(pocoTag.btnExchange5,60):
            pocoTag.btnExchange5.click()
            return True
        else:
            return False
    except:
        return FalseCheckBtnEvent
def clickClaim():
    try:
        if waitNolimitPoco(pocoTag.btnClaim,1):
            pocoTag.btnClaim.click()
            return True
        else:
            return False
    except:
        return False
# check
def tableGame():
    try:
        if waitNolimitPoco(pocoTag.bg_table,10):
            print("table play")
            return True
        else:
            print("end countdown time")
            return False
    except:
        print("error table play")
        return False
def CheckLobby():
    try:
        if waitNolimitPoco(pocoTag.btnPlay,60):
            print("check back lobby")
            return True
        else:
            print("back lobby fail")
            return False
    except:
        print("error back lobby")
        return False
def waitEndGame():
    try:
        poco = CocosJsPoco()
#       if waitNolimitPoco(poco("imgOtherWin"),100):  
        if waitNoLimit(imageWC.imgWin,100):
            print(0)
            print("end game")
            return True
        else:
            print("end time down")
            return False
    except:
        print("error")
        return False
def checkGold():
    numGold = pocoTag.lbGold.attr("text")
    return pipeSubGold(numGold)
#Function DB:---------------------->
#Function VIP:--------------------->
def convertDayToSecond(day):
    second = int(day*24*60*60)
    return second
def cheatTimeRemain(UserID,day):
    try:
        cheat_remain = api_postDoFunction(UserID, "CHEAT_TIME_REMAIN_VIP", [convertDayToSecond(day)])
        print("cheat time remain thanh cong")
        reloadLobby()
        print("Vao shop vip thanh cong")
        killApp()
        openApp()
        #check show pop-up gia han
        back_to_lobby()
        return True    
    except:
        print("Error")
        return False
def open_vip():
    try:
        if exists(image_vip.btn_vip):
            pocoTag.btnVip.click()
            print("Vao thanh cong")
        time.sleep(2)
    except:
        print("error")
        time.sleep(2)
def open_pack(pack):
    try:
        poco(pack).click()
        touch(image_vip.btn_cancel)
        print("Mo thanh cong")
    except:
        print("error")
def back_to_lobby():
    btns = [image_vip.back, image_vip.close, image_vip.outroom]
    try:
        for btn in btns:
            if exists(btn):
                touch(btn)
                print("back lobby thanh cong")
            continue
    except:
        print("back lobby khong thanh cong")
def check_item():
    items = [image_vip.cachua, image_vip.votay, image_vip.xonuoc, image_vip.trung, image_vip.hoahong, image_vip.hoavang, image_vip.sungnuoc]
    try:
        touch(image_vip.btn_profile)
        if exists(image_vip.list_item):
            #return False
            for item in items:
                if exists(item):
                    touch(item)
                    time.sleep(2)
                    touch(image_vip.btn_profile)
                else:
                    #swipe(image_vip.hoahong, record_pos=(0.113, 0.122), resolution=(2340, 1079)), vector=[-0.1553, -0.0043]
                    time.sleep(2)
                    touch(item)
            print("List item co ton tai")
        else:
            #return True
            print("List item khong ton tai")
        back_to_lobby()
    except:
        print("Error")
def to_table():
    try:
        pocoTag.btnPlay.click()
        pocoTag.btnCheat.click()
        pocoTag.btnAddBot.click()
        time.sleep(2)
        pocoTag.btnCheat.click()
        time.sleep(2)
        print("Vao ban, cheat bot thanh cong")  
    except:
        print("Khong thanh cong")
def buy_vip_thap(pack):
    try:
        poco(pack).click()
        time.sleep(1)
        touch(image_vip.btn_ok)
        print("Khong mua duoc vip thap hon")
    except:
        print("Error")
#Function WC:---------------------->
    #------------------#
def beforEvent():
    clearReport()
    #Cheat time-------------24/11/2020 7:00:00----------
    timeCheat = api_changeTimeServer(1605051600000)
#     timeCheat = api_changeTimeServer(timeC["timeD0"]["mili"])
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    dayS['D'] = dayS['D']-2
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #End Cheatime---------------------------------------
    #changeAcc
    changeAcc(user["user0"]["user"],user["user0"]["pass"])
    sleep(5)
    closeEvent()
    #In Game--------------------------------------------
    #---------reload lobby------------------------------
    reloadLobby()
    reloadLoby2()
    #---------end reload lobby--------------------------
    #End in Game----------------------------------------
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        dataReportConfig["Button"]="Fail"
    else:
        dataReportConfig["Button"]="Pass"
    #end Check btn event--------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    print(dataReportConfig)
    reportBeforEvent(dataReportConfig)
def afterEvent():
    poco = CocosJsPoco()
    sleep(2)
#-------------In Game-------------------------------------------------#
    #-------------Cheat time-----------------------------------#
    #26/11/2020 06:59:00
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    dayS['h'] = dayS['h']-1
    dayS['m'] = dayS['m']+59
    dayS['s'] = dayS['s']+40
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    print(dayS)
    print(timeWC["start"])
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #-------------End Cheatime---------------------------------#
    #reload lobby------------------------------
    sleep(2)
    reloadLobby()
    if waitNolimitPoco(pocoTag.btnClose,1):
          closeEvent()
#     clickClaim()
    reloadLoby2()
    # poco("btnClaim").click()
 #Check event--------------------------------------------------#
    #Check btn event -----------------------------------
    if CheckBtnEvent():
        try:
            poco = CocosJsPoco()
            #Join event
            eventWCOpen()
            #Check noti event befor event---------------
            if CheckNotiEvent():
                dataReportConfig['Befor']="Pass"
                #Open pop-up wait event
                if coutDownTime()==1:
                    sleep(1)
                    dataReportConfig["Coutdown"]="Pass"
                else:
                    dataReportConfig["Coutdown"]="Fail"
                #Join event
                if eventWCOpen():
                    sleep(1)
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                sleep(1)
                if waitNolimitPoco(pocoTag.btnJoin,2):
                    dataReportConfig['ShowBtnJoin']="Pass"
                else:
                    dataReportConfig['ShowBtnJoin']="Fail"
                closeEvent()
                #cheat time back 1p
                #26/11/2020 06:59:20
                timeCheat = api_changeTimeServer(1605051600000)
                dayS1 = {
                    "Y": timeWC["start"]['Y'],
                    "M": timeWC["start"]['M'],
                    "D": timeWC["start"]['D'],
                    "h": timeWC["start"]['h'],
                    "m": timeWC["start"]['m'],
                    "s": timeWC["start"]['s']
                }
                dayS1['h'] = dayS1['h']-1
                dayS1['m'] = dayS1['m']+59
                print(dayS1)
                timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS1))
                dataReportConfig["TimeCheat1"]=fortmartTime(dayS1)
                print(timeCheat)
                if timeCheat ==200:
                    dataReportConfig['CheatTime1']="Pass"
                else:
                    dataReportConfig['CheatTime1']="Fail"
                sleep(1)
                #kill app
                killApp()
                #open app
                sleep(2)
                openApp()
                #wait
                sleep(20)
                CheckLobby()
                #changeAcc
                if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                    CheckLobby()
                    #join table wait
                    joinTable()
                    #wait event
                    if coutDownTimeIntable():
                        dataReportConfig['ShowProg']="Pass"
                    else:
                        dataReportConfig['ShowProg']="Fail"
                    #back to lobby
                    clickOutTable()
                    closeEvent()
            else:
                print(21)
                dataReportConfig['Befor']="Fail"
                dataReportConfig["Coutdown"]="Fail"
                #Join event
                if eventWCOpen():
                    sleep(1)
                    dataReportConfig["After"]="Pass"
                else:
                    dataReportConfig["After"]="Fail"
                sleep(1)
                if waitNolimitPoco(pocoTag.btnJoin,2):
                    dataReportConfig['ShowBtnJoin']="Pass"
                else:
                    dataReportConfig['ShowBtnJoin']="Fail"
                closeEvent()
                #cheat time back 1p
                #26/11/2020 06:59:20
                timeCheat = api_changeTimeServer(1605051600000)
                dayS1 = {
                    "Y": timeWC["start"]['Y'],
                    "M": timeWC["start"]['M'],
                    "D": timeWC["start"]['D'],
                    "h": timeWC["start"]['h'],
                    "m": timeWC["start"]['m'],
                    "s": timeWC["start"]['s']
                }
                dayS1['h'] = dayS1['h']-1
                dayS1['m'] = dayS1['m']+59
                print(dayS1)
                timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS1))
                dataReportConfig["TimeCheat1"]=fortmartTime(dayS1)
                print(timeCheat)
                if timeCheat ==200:
                    dataReportConfig['CheatTime1']="Pass"
                else:
                    dataReportConfig['CheatTime1']="Fail"
                sleep(1)
                #kill app
                killApp()
                #open app
                sleep(2)
                openApp()
                #wait
                sleep(20)
                CheckLobby()
                #changeAcc
                if  changeAcc(user["user1"]["user"],user["user1"]["pass"]):
                    CheckLobby()
                    #join table wait
                    joinTable()
                    #wait event
                    if coutDownTimeIntable():
                        dataReportConfig['ShowProg']="Pass"
                    else:
                        dataReportConfig['ShowProg']="Fail"
                    #back to lobby
                    clickOutTable()
                    closeEvent()
        except:
            print('btnMain no find')
    #end Check btn event--------------------------------
  #end check event---------------------------------------------#
#End in Game----------------------------------------------------------#
#-------------End script----------------------------------#
#-------------Report--------------------------------------#
    reportAfterEvent(dataReportConfig)
def day1():
    #join event
    eventWCOpen()
    #Check enable ngay 1 va nhiem vu ngay 1
    if waitNoLimit(imgDay.tabDay1,5):
        dataReportConfig["Tab"]="Pass"
        print("ton tai day 1")
    else:
        dataReportConfig["Tab"]="Fail"
        print("error day1")  
    if waitNolimitPoco(challengePlay[challenge["day1"]["mission"]]["data"]["detailMission"],5):
        dataReportConfig["Mission"]="Pass"
        print("nv day1")
    else:
        dataReportConfig["Mission"]="Fail"
        print("error day1")
    print(dataReportConfig)
    closeEvent()
     #------------------------#
    #report
    reportDay1(dataReportConfig)
    checkMission("day1")
def day2():
    #resetDataReport
    resetDataReportConfig()
    #cheat time pass 1 ngay-> 27/11/2020 07:00:00
    timeCheat = api_changeTimeServer(1605051600000)
    dayS = {
        "Y": timeWC["start"]['Y'],
        "M": timeWC["start"]['M'],
        "D": timeWC["start"]['D'],
        "h": timeWC["start"]['h'],
        "m": timeWC["start"]['m'],
        "s": timeWC["start"]['s']
    }
    dayS['D'] = dayS['D']+1
    timeCheat = api_changeTimeServer(convertDayTimeToMili(dayS))
    dataReportConfig["TimeCheat"]=fortmartTime(dayS)
    if timeCheat ==200:
        dataReportConfig['CheatTime']="Pass"
    else:
        dataReportConfig['CheatTime']="Fail"
    #reload lobby
    if reloadLobby():
        dataReportConfig['Reload']="Pass"
    else:
        dataReportConfig['Reload']="Fail"
    #check auto show event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
    #close Gui Event
    clickClaim()
    closeEvent()
    closeEvent()
    #check auto show deal
    if CheckGUIDeal():
        dataReportConfig['GuiEDeal']="Pass"
    else:
        dataReportConfig['GuiEDeal']="Fail"
    #close Gui Deal
    closeEvent()
    #check mission
     #join event
    eventWCOpen()
    #Check enable ngay 2 va nhiem vu ngay 2
    if CheckLableDay()==2:
        dataReportConfig["Tab"]="Pass"
        print("ton tai day2")
    else:
        dataReportConfig["Tab"]="Fail"
        print("error day2")   
#     if waitNolimitPoco(challenge["day2"]["data"]["detailMission"],5):
    if waitNolimitPoco(challengePlay[challenge["day2"]["mission"]]["data"]["detailMission"],5):
        dataReportConfig["Mission"]="Pass"
        print("nv day2")
    else:
        dataReportConfig["Mission"]="Fail"
        print("error day2")
    closeEvent()
        #------------------------#
    print(dataReportConfig)
    #report
    reportDay2(dataReportConfig)
    #------------------------#
    checkMission("day2")
def day3():
        #resetDataReport
    resetDataReportConfig()
    #------------------------#
    #report
    reportDay3(dataReportConfig)
    #------------------------#
    checkMission("day3")
def exchange1(day):
    try:
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        print(prog1)
        closeEvent()
        cheatGold(user["user2"]["id"],1000000) 
        #click btn play
        if joinTable():
            dataReportConfig["BtnPlay"]="Pass"
        else:
            data1["BtnPlay"]="Fail"
        #cheat cheatPorkerSpecial
        #add bot
        if addBot():
            dataReportConfig["Bot"]="Pass"
        else:
            dataReportConfig["Bot"]="Fail"
        #Click exchange5
        clickExchange5()
        #Click Exchange1
        if clickExchange1():
            dataReportConfig["Exchange1"]="Pass"
        else:
            dataReportConfig["Exchange1"]="Fail"
        #check update progess
        prog2=checkProgressCurrent()
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
        #click knock
        clickKnock()
        #chon thoat table
        if clickOutTable():
            dataReportConfig["ChooseLeave"]="Pass"
        else:
            dataReportConfig["ChooseLeave"]="Fail"
        #wait end game
        waitEndGame()
        #check update progess
        prog3=checkProgressCurrent()
        if checkUpdateProgessTable(prog2,prog3):
            dataReportConfig["NoUpdate"]="Fail"
        else:
            dataReportConfig["NoUpdate"]="Pass"
        #check lobby
        if CheckLobby():
            dataReportConfig["Leave"]="Pass"
        else:
            dataReportConfig["Leave"]="Fail"
    except:
        print("error exchange1")
    print(dataReportConfig)
    reportExchange1(dataReportConfig)
def knock(day):
    try:
        #join event
        eventWCOpen()
        #check progress
        prog1=checkProgressCurrent()
        closeEvent()
        #cheat gold du play
        if cheatGold(user["user1"]["id"],1000000) :
            dataReportConfig["CheatGold"]="Pass"
        else :
            dataReportConfig["CheatGold"]="Fail"
        #click btn play
        if joinTable():
            dataReportConfig["BtnPlay"]="Pass"
        else:
            dataReportConfig["BtnPlay"]="Fail"
        #Check table
        if tableGame():
            dataReportConfig["JoinTable"]="Pass"
        else:
            dataReportConfig["JoinTable"]="Fail"
        #cheat cheatPorkerSpecial
        #add bot
        if addBot():
            dataReportConfig["Bot"]="Pass"
        else:
            dataReportConfig["Bot"]="Fail"
        #Click knock
        if clickKnock():
            dataReportConfig["Knock"]="Pass"
        else:
            dataReportConfig["Knock"]="Fail"
        prog2=checkProgressCurrent()
        #cheat win finished game
        # cheatNumMision(1)
        #chon thoat table
        clickOutTable()
        #wait end game
        waitEndGame()
        #check update progess
        if checkUpdateProgessTable(prog1,prog2):
            dataReportConfig["Update"]="Pass"
        else:
            dataReportConfig["Update"]="Fail"
           #check lobby
        if CheckLobby():
            dataReportConfig["Leave"]="Pass"
        else:
            dataReportConfig["Leave"]="Fail" 
        closeEvent()
    except:
        print("error knock")
    print(dataReportConfig)
    reportKnock(dataReportConfig)
def claimGift():
    # script content
    #back to loby
    CheckLobby()
    #check gold init
    goldInit=checkGold()
    #Cheat finished mission-----------------------
    if cheatFinishedMision(user["user1"]["id"],1):
        dataReportConfig['CheatFM']="Pass"
    else:
        dataReportConfig['CheatFM']="Fail"
    #---------reload lobby------------------------------
    reloadLobby()
    #check GUI event
    if CheckGUIEvent():
        dataReportConfig['GuiEvent']="Pass"
    else:
        dataReportConfig['GuiEvent']="Fail"
        eventWCOpen()
    to1=checkTocos()
    #check gold claim
    goldClaim=challengePlay[challenge["day1"]["mission"]]["data"]["gold"]
    tocosConf=challengePlay[challenge["day1"]["mission"]]["data"]["tacos"]
    #click claim gift
    clickClaimMission()
    to2=checkTocos()
    #exit GUI event
    closeEvent()
    #check update gold
    goldAfter=checkGold()
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    if checkTocosUpdate(tocosConf,to1,to2):
        dataReportConfig['UpdateTocos']="Pass"
    else:
        dataReportConfig['UpdateTocos']="Fail"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportClaimGift(dataReportConfig)
def noClaimGift():
    # script content
   #back to loby
    CheckLobby()
    #check gold init
    goldInit=checkGold()
    #Cheat finished mission-----------------------
    cheatFinishedMision(user["user1"]["id"],2)
    #---------reload lobby------------------------------
    reloadLobby()
    #check GUI event
    if CheckGUIEvent():
        closeEvent()
    else:
        eventWCOpen()
        sleep(1)
        closeEvent()
    #check gold claim
    goldClaim=0
    #check update gold
    goldAfter=checkGold()
    if checkUpdateGold(goldClaim,goldInit,goldAfter):
        dataReportConfig['GoldUpdate']="Pass"
    else:
        dataReportConfig['GoldUpdate']="Fail"
    #End in Game----------------------------------------
    #-------------End script----------------------------------#
    #-------------Report--------------------------------------#
    reportNoClaimGift(dataReportConfig)
    #------------------#
    #check
def CheckBtnEvent():
    try:
#         if waitNolimitPoco(poco("btnMain"),10):
        if waitNoLimit(imageWC.imgBtnEvent,5):
            return True
        else:
            return False
    except:
        print("error btn event")
        return False
def CheckNotiEvent():
    try:
        if notiShow.attr("type")=="ImageView":
            print("check noti event")
            return True
        else:
            print("check noti event no exists")
            return False
    except:
        print("check noti event no exists")
        return False
def coutDownTime():
    cout=65
    while 1:
        sleep(1)
        cout-=1
        time=pocoTag.lbTime.attr("text")
        print(time)
        if time=="Abierto en: 00:00:-01":
            print("Error coutdown time")
            return 0
            break
        if time=="6 días":
            print("Pass coutdown time")
            return 1
            break
        if cout==0:
            if time!="6 días":
                print("Error coutdown time")
                return 0
                break
def coutDownTimeIntable():
    cout=20
    while 1:
        sleep(1)
        cout-=1
        if cout==0 or cout<0:
            print("Error coutdown time")
            return False
            break
        if exists1(pocoTag.btnMain):
            print("show")
            return True
            break
def checkMission(day):
    if challenge[day]["mission"]=="win":
        return win(day)
    if challenge[day]["mission"]=="play":
        return play(day)
    if challenge[day]["mission"]=="knock":
        return knock(day)
    if challenge[day]["mission"]=="exchange1":
        return exchange1(day)
def checkProgressCurrent():
    try:
        if waitNolimitPoco(pocoTag.lbProgress,5):
            progress=pocoTag.lbProgress.get_text()
            prg=progress.split("/")
            prgL=int(prg[0].strip())
            prgR=int(prg[1].strip())
            print(prgR)
            print(prgL)
            print("Progess checkProgressCurrent")
            return prgL
        else:
            print("NO find progress")
            return False
    except:
        print("error checkProgressCurrent")
        return False
def checkUpdateProgessTable(prg1,prg2):
    try:
        print(prg1)
        print(prg2)
        if (prg2-prg1) > 0 :
            print("Progess update")
            return True
        else:
            print("Progess no update")
            return False
    except:
        print("error checkUpdateProgessTable")
        return False
def CheckGUIEvent():
    try:
        if waitNolimitPoco(pocoTag.imgTruck,5):
            print("check CheckGUIEvent")
            return True
        else:
            return False
    except:
        print("check CheckGUIEvent no exists")
        return False
def CheckGUIDeal():
    try:
        if waitNoLimit(imageWC.imgDeal,5):
            print("check CheckGUIDeal")
            return True
        else:
            return False
    except:
        print("check CheckGUIDeal no exists")
        return False
def CheckLableDay():
    try:
        if waitNolimitPoco(pocoTag.lbDay1,1):
               print("Día 1")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 1
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay2,1):
            print("Día 2")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 2
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay3,1):
            print("Día 3")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 3
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay4,1):
            print("Día 4")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 4
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay5,1):
            print("Día 5")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 5
            else:
                return False
        if waitNolimitPoco(pocoTag.lbDay6,1):
            print("Día 6")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 6
            else:
                return False   
        if waitNolimitPoco(pocoTag.lbDay7,1):
            print("Día 7")
        else:
            if waitNolimitPoco(pocoTag.lbDayCurrent,1):
                return 7
            else:
                return False
    except:
        return False
def checkTocos():
    try:
        if waitNolimitPoco(pocoTag.lbNumTacos,2):
            tocos=int(pocoTag.lbNumTacos.get_text())
            return tocos
    except:
        return False
def checkTocosUpdate(to1,to2,to3):
    try:
        print(to1)
        print(to2)
        print(to3)
        to=to3-to2
        if to1==to:
            print("check checkTocosUpdate")
            return True
        else:
            return False
    except:
        print("check checkTocosUpdate error" )
        return False 
def checkUpdateGold(gold1, gold2, gold3):
    try:
        print(gold1)
        print(gold2)
        print(gold3)
        claim= float(gold1)
        update= gold3 - gold2
        print(claim)
        print(update)
        if update == claim :
            print("Gold update")
            return True
        else:
            print("gold update false")
            return False
    except:
        print("Gold update error")
        return False
    #action
def eventWCOpen():
    try:
        poco = CocosJsPoco()
        if waitNolimitPoco(pocoTag.btnMain,5):
            pocoTag.btnMain.click()
            print("event WC")
            return True
    except:
        print("error event WC")
        return False
def clickClaimMission():
    try:
        if waitNolimitPoco(pocoTag.btnJoin,1):
            pocoTag.btnJoin.click()
            return True
        else:
            return False
    except:
        return False
#-------------------------------------------------------------------------------------#
def gold_number():
    gold=pocoTag.lbGold.get_text()
    dec=["M","K","B"]
    for index in range(len(dec)):
        don_vi=gold.endswith(dec[index])
        #print(don_vi)
        if don_vi== True:
            #print(dec[index])
            num = gold.split(dec[index]) 
            if dec[index]=="M":  
                num = gold.split("M")  #print(num)
                number= num[0]         #print(number)
                number= float(number)    #print(type(number)) 
                number=number*1000000
                #print(number)
            elif dec[index]=="K":
                num = gold.split("K")   #print(num) 
                number= num[0]          #print(number)
                number= float(number)   #print(type(number))
                number=number*1000
                #print(number)
            elif dec[index]=="B":
                num = gold.split("B")   #print(num)
                number= num[0]          #print(number)
                number= float(number)   #print(type(number))
                number=number*1000000000
                #print(number)
    return number
def log_in():
    poco = CocosJsPoco()
    poco("btnSwitch").exists()
    poco("btnGuest").click()
def log_out():
    data={
        "status":"Fail"
    }
    try:
        poco("btnPlay").exists
    except:
        print("Please back to lobby page!")
    else:
        print("Success!")
    poco("iconSetting").click()
    poco("bgLobbyLayer2").click()
    touch(Template(r"tpl1608523320839.png", record_pos=(0.097, 0.08), resolution=(1280, 720)))
    data["status"]="True"
    reportdailybonus(data)
def log_in_gg():
    poco = CocosJsPoco()
    pocoTag.btnGooglePlus.exists()
    pocoTag.btnGooglePlus.click()  
    #touch(Template(r"tpl1608609498145.png", record_pos=(-0.179, -0.024), resolution=(1920, 1080)))
def log_in_FB():
    pocoTag.btnFacebookNormal.click()
    time.sleep(5)
#2.2 Register_thường
def register():
    data= {
        "status": "false"
    }
    pocoTag.btnSwitch.click()
    pocoTag.inputUser.click()
    text("ngocnt93")
    pocoTag.inputPass.click()
    text("12345678")
    pocoTag.btnRegister.click()  
# Nhận dailybonus của ngày đầu tiên
def bonus_day_1():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    if pocoTag.btnClaim.exists():
        data["status"]="true"
        pocoTag.btnClaim.click()
        pocoTag.btnClaim.click()
        print("Success!")
    else:
        print("khong auto show Gui daily bonus sau play tutorial")
    reportdailybonus(data)
#kiểm tra có auto về lobby sau khi click claim nhận bonus
def check_lobby():
    try:
        pocoTag.btnPlay.exists()
    except:
        print("Không auto về lại lobby sau khi nhận bonus")
    else:
        print("Success!")
# 1. check có đang ở log_in screen hay ko
def check_login():
    data= {
        "status": "False",
        "Time": "False",
        "button": "False",
    }
    
    if pocoTag.btnSwitch.exists():
        data["status"]="true"
        print("success!")
    else:
        print ("Please go to Login page")
    reportdailybonus(data)
    # Kiểm tra có show GUI daily bonus ko, Nhận bonus
def claim_bonus():
    data={
    "status":"Fail"
    }
    time.sleep(3)
    if pocoTag.btnClaim.exists():
        data["status"]="True"
        pocoTag.btnClaim.click()
    else:
        print("Dont show GUI bonus")
        data["status"]="False"
    reportdailybonus(data)
#Kiểm tra có show GUI daily bonus khi dung o lobby cho nhan bonus
def check_show_GUI():
    api_changeTimeServer(1608796800000)
    try:
        pocoTag.btnClaim.exists()
    except:
        print("Không auto show GUI daily bonus ở lobby sau 24h")
    else:
        print("Success!")
#Vao lại Gui daily bonus
def into_gui_bonus():
    time.sleep(3)
    pocoTag.btnDaily.click()
    pocoTag.btnTomorrow.exists()
    pocoTag.btnTomorrow.click()
    pocoTag.btnPlay.exists()
#10. Log out-> vào lại sau 23h
def Logout_login_23h():
    log_out()
    api_changeTimeServer(1608879600000)
    log_in_FB()
    data={
        "status":"false"
    }
    time.sleep(5)
    if pocoTag.btnClaim.exists():
        pocoTag.btnClaim.click()
        time.sleep(3)
        data["status"]="False"
        print("Show daily GUI daily bonus khi chưa đủ 24h")
    else:
        data["status"]="True"
        print("Ko Show GUI khi chuwa ddur 24h!")
    reportdailybonus(data)
    time.sleep(3)
#11. Vao playinggame-> ra lại lobby
def playing_23h():
    pocoTag.btnPlay.click()
    api_changeTimeServer(1608882000000)
    pocoTag.btnLeaveGame.click()
    time.sleep(1)
    try:
        pocoTag.btnPlay.exists() #leave khi chưa đủ 24h
    except:
        print("playing->lobby: show GUI daily bonus khi chưa đủ 24h")
        time.sleep(3)
        pocoTag.btnClaim.click()
        data["status"]="False"
    else:
        data["status"]="True"
        print("Khong show GUI bonus khi leave tuwf playing khi chuwa ddur 24h")
    reportdailybonus(data)
#12. Vào playing game-> Chờ qua 24h rồi ra lại lobby( Ngày 4)
def playing_24h():
    data= {
        "status":"False"
    }
    time.sleep(3)
    pocoTag.btnPlay.click()
    api_changeTimeServer(1608883200000)
    time.sleep(3)
    pocoTag.btnLeaveGame.click()
    time.sleep(4)
    if pocoTag.btnClaim.exists():
        print("show GUI daily bonus day 4 Success!")
        data["status"]="True"
    else:
        print("Khong show GUI daily BONUS khi plaing ra lobby sau 24h")
        data["status"]="False"
    reportdailybonus(data) 
#14. Đứng chờ ở GUI daily bonus 23h
def GUI_bonus_23h():
    api_changeTimeServer(1608966000000)
    reloadLobby()
    pocoTag.btnDaily.click()
    pocoTag.btnTomorrow.exists()
#16 Nhận bonus 5 lần-> Log out-> Login sau 24h nhưng không nhận bonus->Login lại sau 24h tiếp theo
def claim_kill_login_24h():
    data={
        "status":"Fail"
    }
    time.sleep(3)
    if pocoTag.btnClaim.exists():
        print("Show daily bonus day 5 Success!")
        gold_befor5= gold_number()
        pocoTag.btnClaim.click()
        gold_after5= gold_number()
        if DailyBonus["day5"]["bonus"]==(gold_after5 - gold_befor5):    
            data["status"]="True"
        else:
            pocoTag.btnTomorrow.click()
            print("Update gold sai")
            data["status"]="False"
    else:
        time.sleep(3)
        pocoTag.btnTomorrow.click()
        print("Koo auto show daily bonus khi o GUI daily bonus sau 24h")
    reportdailybonus(data)
    time.sleep(2)
    log_out()
    api_changeTimeServer(1609056000000)
    log_in_FB()
         #kill app vào lại sau 24h
    # kill_app()
    # start_app()
    try:
        pocoTag.btnClaim.exists()
    except:
        print("Không auto show daily bonus khi khong nhan bonus cua ngay truoc")
    else:
        print("Show GUI khi kill app ko nhaan cuar ngay trc!")
    api_changeTimeServer(1609142400000)
#check an btn Daily bonus ở lobby khi đã nhận đủ 7 lần
def complete_icon_bonus_lobby():
    if pocoTag.btnDaily.exists():
        print("Van show icon Daily bonus ở lobby khi da nhan du 7 lan")
    else:
        print("hide Daily bonus btn khi nhan dur 7 lan success")
#19. Ra lại lobby-> đứng ở lobby chờ sau 24
def complete_lobby_24h():
    pocoTag.btnPlay.exists()
    api_changeTimeServer(1609315200000)
    if pocoTag.btnClaim.exists():
        print("Vẩn show daily bonus khi đã nhận đủ 7 lần")
    else:
        print("Success!")
#20. Log out-> Login lại sau 24h
def complete_logout_login_24h():
    log_out()
    api_changeTimeServer(1609401600000)
    log_in_FB()
    if pocoTag.btnClaim.exists():
        print("Vẩn show daily bonus khi đã nhận đủ 7 lần")
    else:
        print(" Success!")
#



