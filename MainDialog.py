import sys
"""import uuid
import decimal
import Queue
import xmlrpc
import xmlrpc.client
import urllib.request
import configparser"""
from CPortal import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MainDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.portal = CPortal()
        self.logintry = 0
        self.initUI()
    def initUI(self):
        self.setFixedSize(890,480)
        self.center()
        self.setWindowTitle('외박포탈프로그램4.0 beta+')
        self.setWindowIcon(QIcon('charm2.ico'))
        self.mode = 0
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.WindowTitleHint)

        self.LabelID = QLabel('ID : ', self)
        self.LabelPW = QLabel('PW : ', self)
        self.LabelID.move(360,205)
        self.LabelPW.move(360,225)

        self.EditID = QLineEdit(self)
        self.EditPW = QLineEdit(self)
        self.EditID.resize(100,20)
        self.EditID.move(400,200)
        self.EditPW.resize(100,20)
        self.EditPW.move(400,220)
        self.EditPW.setEchoMode(QLineEdit.Password)
        
        self.Button1 = QPushButton('확인',self)
        self.Button1.resize(50,20)
        self.Button1.move(505,220)
        self.Button1.clicked.connect(self.Confirm)
        
        self.MainButton1 = QPushButton('슬롯배치 (F2)',self)
        self.MainButton1.resize(150,35)
        self.MainButton1.move(730,30)
        self.MainButton1.clicked.connect(self.Func2)
        self.MainButton2 = QPushButton('휴가입력 (F3)',self)
        self.MainButton2.resize(150,35)
        self.MainButton2.move(730,70)
        self.MainButton2.clicked.connect(self.Func3)
        self.MainButton3 = QPushButton('지망입력 (F4)',self)
        self.MainButton3.resize(150,35)
        self.MainButton3.move(730,110)
        self.MainButton3.clicked.connect(self.Func4)
        self.MainButton4 = QPushButton('배치시작 (F5)',self)
        self.MainButton4.resize(150,35)
        self.MainButton4.move(730,150)
        self.MainButton4.clicked.connect(self.Func5)
        self.MainButton5 = QPushButton('결과보기 (F6)',self)
        self.MainButton5.resize(150,35)
        self.MainButton5.move(730,190)
        self.MainButton5.clicked.connect(self.Func6)
        self.MainButton6 = QPushButton('초기화 (F7)',self)
        self.MainButton6.resize(150,35)
        self.MainButton6.move(730,230)
        self.MainButton6.clicked.connect(self.Func7)
        self.MainButton8 = QPushButton('사용자추가 (F8)',self)
        self.MainButton8.resize(150,35)
        self.MainButton8.move(730,270)
        self.MainButton8.clicked.connect(self.Func9)
        self.MainButton7 = QPushButton('종료 (F9)',self)
        self.MainButton7.resize(150,35)
        self.MainButton7.move(730,430)
        self.MainButton7.clicked.connect(self.Func8)
        
        self.Label1 = QLabel('이름 : ',self)
        self.Label21 = QLabel("시작날짜 : ",self)
        self.Label22 = QLabel("-",self)
        self.Label23 = QLabel("-",self)
        self.Label31 = QLabel("복귀날짜 : ",self)
        self.Label32 = QLabel("-",self)
        self.Label33 = QLabel("-",self)
        self.Label4 = QLabel("지망 : ",self)
        self.Label1.move(20,35)
        self.Label21.move(20,65)
        self.Label22.move(120,65)
        self.Label23.move(155,65)
        self.Label31.move(20,95)
        self.Label32.move(120,95)
        self.Label33.move(155,95)
        self.Label4.move(20,95)

        self.ResLabel = []
        for i in range(0,16):
            self.ResLabel.append(QLabel(self))
            self.ResLabel[i].move(50,20*i+25)
            self.ResLabel[i].hide()
        
        self.Edit1 = QLineEdit(self)
        self.Edit21 = QLineEdit(self)
        self.Edit22 = QLineEdit(self)
        self.Edit23 = QLineEdit(self)
        self.Edit31 = QLineEdit(self)
        self.Edit32 = QLineEdit(self)
        self.Edit33 = QLineEdit(self)
        self.Edit4 = QLineEdit(self)
        self.Edit1.resize(80,20)
        self.Edit21.resize(40,20)
        self.Edit22.resize(30,20)
        self.Edit23.resize(30,20)
        self.Edit31.resize(40,20)
        self.Edit32.resize(30,20)
        self.Edit33.resize(30,20)
        self.Edit4.resize(30,20)
        self.Edit1.move(80,30)
        self.Edit21.move(80,60)
        self.Edit22.move(125,60)
        self.Edit23.move(160,60)
        self.Edit31.move(80,90)
        self.Edit32.move(125,90)
        self.Edit33.move(160,90)
        self.Edit4.move(80,90)
        """
        self.lbl = QLabel('start',self)
        self.lbl.move(300,40)
"""
        self.Label1.hide()
        self.Label21.hide()
        self.Label22.hide()
        self.Label23.hide()
        self.Label31.hide()
        self.Label32.hide()
        self.Label33.hide()
        self.Label4.hide()
        self.Edit1.hide()
        self.Edit21.hide()
        self.Edit22.hide()
        self.Edit23.hide()
        self.Edit31.hide()
        self.Edit32.hide()
        self.Edit33.hide()
        self.Edit4.hide()
        self.MainButton1.hide()
        self.MainButton2.hide()
        self.MainButton3.hide()
        self.MainButton4.hide()
        self.MainButton5.hide()
        self.MainButton6.hide()
        self.MainButton8.hide()
        self.show()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def keyPressEvent(self, e):
        if e.key()==Qt.Key_F1:
            msg = QMessageBox.information(self,'제작자','1064기 민병욱 제작\n010-6220-9334\nphraust@kaist.ac.kr', QMessageBox.Ok)
        elif e.key()==Qt.Key_F2 and self.mode!=0:
            self.Func2()
        elif e.key()==Qt.Key_F3 and self.mode!=0:
            self.Func3()
        elif e.key()==Qt.Key_F4 and self.mode!=0:
            self.Func4()
        elif e.key()==Qt.Key_F5 and self.mode!=0:
            self.Func5()
        elif e.key()==Qt.Key_F6 and self.mode!=0:
            self.Func6()
        elif e.key()==Qt.Key_F7 and self.mode!=0:
            self.Func7()
        elif e.key()==Qt.Key_F9:
            self.Func8()
        elif e.key()==Qt.Key_F8 and self.mode!=0:
            self.Func9()
        elif e.key()==Qt.Key_Enter or e.key()==Qt.Key_Return:
            self.Confirm()
            if self.mode==2:
                self.Edit21.setFocus()
                self.Edit21.selectAll()
            elif self.mode==3 or self.mode==4 or self.mode==9:
                self.Edit1.setFocus()
                self.Edit1.selectAll()
            else:
                pass
        else:
            pass
    def Func2(self):
        self.mode = 2
        self.Label1.hide()
        self.Label21.show()
        self.Label22.show()
        self.Label23.show()
        self.Label31.hide()
        self.Label32.hide()
        self.Label33.hide()
        self.Label4.hide()
        self.Edit1.hide()
        self.Edit21.show()
        self.Edit22.show()
        self.Edit23.show()
        self.Edit31.hide()
        self.Edit32.hide()
        self.Edit33.hide()
        self.Edit4.hide()
        self.LabelID.hide()
        self.LabelPW.hide()
        self.EditID.hide()
        self.EditPW.hide()
        for i in range(0,16):
            self.ResLabel[i].hide()
        self.Button1.move(200,60)
        self.Button1.show()
        self.Edit21.setFocus()
        self.Edit21.selectAll()
    def Func3(self):
        self.mode = 3
        if self.portal.loginsuccess != 2:
            self.Label1.show()
            self.Edit1.show()
            self.Label1.move(20,35)
            self.Edit1.move(80,30)
        self.Label21.show()
        self.Label22.show()
        self.Label23.show()
        self.Label31.show()
        self.Label32.show()
        self.Label33.show()
        self.Label4.hide()
        self.Edit21.show()
        self.Edit22.show()
        self.Edit23.show()
        self.Edit31.show()
        self.Edit32.show()
        self.Edit33.show()
        self.Edit4.hide()
        self.LabelID.hide()
        self.LabelPW.hide()
        self.EditID.hide()
        self.EditPW.hide()
        for i in range(0,16):
            self.ResLabel[i].hide()
        self.Button1.move(200,90)
        self.Button1.show()
        self.Edit1.setFocus()
        self.Edit1.selectAll()
    def Func4(self):
        self.mode = 4
        if self.portal.loginsuccess != 2:
            self.Label1.show()
            self.Edit1.show()
            self.Label1.move(20,35)
            self.Edit1.move(80,30)
        self.Label21.show()
        self.Label22.show()
        self.Label23.show()
        self.Label31.hide()
        self.Label32.hide()
        self.Label33.hide()
        self.Label4.show()
        self.Edit21.show()
        self.Edit22.show()
        self.Edit23.show()
        self.Edit31.hide()
        self.Edit32.hide()
        self.Edit33.hide()
        self.Edit4.show()
        self.LabelID.hide()
        self.LabelPW.hide()
        self.EditID.hide()
        self.EditPW.hide()
        for i in range(0,16):
            self.ResLabel[i].hide()
        self.Button1.move(115,90)
        self.Button1.show()
        self.Edit1.setFocus()
        self.Edit1.selectAll()
    def Func5(self):
        err = self.Simulate()
        if err==0:
            msg = QMessageBox.information(self,'ㅇㅋ','랜덤배치성공', QMessageBox.Yes, QMessageBox.Yes)
        else:
            msg = QMessageBox.warning(self,'ㄴㄴ!!','실패!! : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
    def Func6(self):
        self.mode = 6
        self.Label1.hide()
        self.Label21.hide()
        self.Label22.hide()
        self.Label23.hide()
        self.Label31.hide()
        self.Label32.hide()
        self.Label33.hide()
        self.Label4.hide()
        self.Edit1.hide()
        self.Edit21.hide()
        self.Edit22.hide()
        self.Edit23.hide()
        self.Edit31.hide()
        self.Edit32.hide()
        self.Edit33.hide()
        self.Edit4.hide()
        self.LabelID.hide()
        self.LabelPW.hide()
        self.EditID.hide()
        self.EditPW.hide()
        self.Button1.move(165,60)
        self.Button1.hide()
        self.ShowResult()
    def Func7(self):
        self.portal.FlushData()
        msg = QMessageBox.information(self,'ㅇㅋ','초기화됨', QMessageBox.Yes, QMessageBox.Yes)
    def Func8(self):
        self.portal.__del__()
        self.close()
    def Func9(self):
        self.mode = 9
        self.Label1.show()
        self.Label1.move(360,185)
        self.Edit1.show()
        self.Edit1.move(400,180)
        self.Label21.hide()
        self.Label22.hide()
        self.Label23.hide()
        self.Label31.hide()
        self.Label32.hide()
        self.Label33.hide()
        self.Label4.hide()
        self.Edit21.hide()
        self.Edit22.hide()
        self.Edit23.hide()
        self.Edit31.hide()
        self.Edit32.hide()
        self.Edit33.hide()
        self.Edit4.hide()
        self.LabelID.show()
        self.LabelPW.show()
        self.EditID.show()
        self.EditPW.show()
        self.Button1.move(505,220)
        for i in range(0,16):
            self.ResLabel[i].hide()
        self.Button1.show()
        self.Edit1.setFocus()
        self.Edit1.selectAll()
    def Confirm(self):
        name = self.Edit1.text()
        year1 = self.Edit21.text()
        try:
            year1 = int(year1)
        except:
            if year1=='':
                pass
            else:
                # alert message
                return
        month1 = self.Edit22.text()
        try:
            month1 = int(month1)
        except:
            if month1=='':
                pass
            else:
                # alert message
                return
        day1 = self.Edit23.text()
        try:
            day1 = int(day1)
        except:
            if day1=='':
                pass
            else:
                # alert message
                return
        year2 = self.Edit31.text()
        try:
            year2 = int(year2)
        except:
            if year2=='':
                pass
            else:
                # alert message
                return
        month2 = self.Edit32.text()
        try:
            month2 = int(month2)
        except:
            if month2=='':
                pass
            else:
                # alert message
                return
        day2 = self.Edit33.text()
        try:
            day2 = int(day2)
        except:
            if day2=='':
                pass
            else:
                # alert message
                return
        prior = self.Edit4.text()
        try:
            prior = int(prior)
        except:
            if prior=='':
                pass
            else:
                # alert message
                return
        """self.lbl.setText(name+str(year1)+str(month1)+str(day1)+str(year2)+str(month2)+str(day2)+str(prior))
        self.lbl.adjustSize()"""
        if self.mode == 0:
            ID = self.EditID.text()
            PW = self.EditPW.text()
            self.TryLogin(ID,PW)
        elif self.mode == 2:
            err = self.SlotAlloc(year1,month1,day1)
            if err==0:
                msg = QMessageBox.information(self,'ㅇㅋ','슬롯배치됨', QMessageBox.Yes, QMessageBox.Yes)
            else:
                msg = QMessageBox.warning(self,'ㄴㄴ!!','슬롯배치실패 : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
        elif self.mode == 3:
            err = self.InputFixed(name,year1,month1,day1,year2,month2,day2)
            if err==0:
                msg = QMessageBox.information(self,'ㅇㅋ','입력됨', QMessageBox.Yes, QMessageBox.Yes)
            else:
                msg = QMessageBox.warning(self,'ㄴㄴ!!','휴가입력실패 : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
        elif self.mode == 4:
            err = self.SubmitWish(name,prior,year1,month1,day1)
            if err==0:
                msg = QMessageBox.information(self,'ㅇㅋ','입력됨', QMessageBox.Yes, QMessageBox.Yes)
            else:
                msg = QMessageBox.warning(self,'ㄴㄴ!!','지망입력실패 : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
        elif self.mode == 9:
            ID = self.EditID.text()
            PW = self.EditPW.text()
            err = self.portal.SQLNewID(ID,PW,name)
            if err==0:
                msg = QMessageBox.information(self,'ㅇㅋ','생성됨', QMessageBox.Yes, QMessageBox.Yes)
            else:
                msg = QMessageBox.warning(self,'ㄴㄴ!!','생성실패 : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
        else:
            return
    def TryLogin(self,ID,PW):
        err = self.portal.SQLLogin(ID,PW)
        if err == 0 or ID=="guest":
            self.mode = 1
            self.LabelID.hide()
            self.LabelPW.hide()
            self.EditID.hide()
            self.EditPW.hide()
            self.Button1.hide()
            self.MainButton3.show()
            self.MainButton8.show()
            self.portal.LoadMember()
            if self.portal.loginsuccess == 2:
                self.MainButton3.move(730,30)
                self.MainButton8.move(730,70)
                self.MainButton8.setText("비밀번호 수정 (F8)")
                self.MainButton7.move(730,110)
            else:
                self.MainButton1.show()
                self.MainButton2.show()
                self.MainButton4.show()
                self.MainButton5.show()
                self.MainButton6.show()
                self.MainButton7.move(730,310)
        elif err == 1045:
            msg = QMessageBox.warning(self,'에러!!!','ID 혹은 비밀번호가 잘 못 되었습니다.', QMessageBox.Yes, QMessageBox.Yes)
        elif err == 1049:
            msg = QMessageBox.warning(self,'에러!!!','DB 없음', QMessageBox.Yes, QMessageBox.Yes)
        else:
            msg = QMessageBox.warning(self,'에러!!!','에러 : '+str(err), QMessageBox.Yes, QMessageBox.Yes)
        self.logintry += 1
    def SlotAlloc(self,y,m,d):
        return self.portal.AutoAllocateSlot(y,m,d)
    def InputFixed(self,name,y,m,d,y2,m2,d2):
        return self.portal.InsertFixed(name,y,m,d,y2,m2,d2)
    def SubmitWish(self,name,p,y,m,d):
        return self.portal.SubmitWish(name,p,y,m,d)
    def Simulate(self):
        return self.portal.RandSimulate()
    def ShowResult(self):
        for i in range(0,self.portal.maxSlot):
            tmp = self.portal.slot[i].start.refineToString()
            tmp += " ~ "
            tmp += self.portal.slot[i].end.refineToString()
            tmp += " : "
            for j in self.portal.slot[i].list:
                tmp += self.portal.member[j].name
                tmp += " "
            self.ResLabel[i].setText(tmp)
            self.ResLabel[i].show()
        remaincount = 0
        tmp=""
        for i in range(0,self.portal.maxMem):
            if self.portal.member[i].allocated==0:
                tmp += self.portal.member[i].name + " "
                remaincount += 1
        if remaincount>0:
            tmp += "는(은) 3지망까지 안됐음. 남는자리에서 재배정하셈"
            msg = QMessageBox.warning(self,'낙오자들ㅠㅠ',tmp, QMessageBox.Yes, QMessageBox.Yes)

app = QApplication(sys.argv)
MD = MainDialog()
sys.exit(app.exec_())
