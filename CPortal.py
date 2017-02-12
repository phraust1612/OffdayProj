import sys
import random
import mysql.connector
from mysql.connector import errorcode
from CRefine import *
class InfoStr:
    def __init__(self):
        self.start = CRefine(1990,1,1)
        self.end = CRefine(1990,1,1)

class Member:
    def __init__(self):
        self.name = ""
        self.allocated = 0
        self.wish = [InfoStr(),InfoStr(),InfoStr()]

class Slot:
    def __init__(self):
        self.start = CRefine(1990,1,1)
        self.end = CRefine(1990,1,1)
        self.num = 0
        self.list = []

class CPortal:
    def __init__(self):
        self.loginsuccess = 0
        self.p_err = 0
        self.slot = []
        self.member = []
        self.maxMem = 0
        self.maxSlot = 0
        self.remained = 0
        self.p = []
        self.r = []
    def __del__(self):
        try:
            self.cursor
        except NameError:
            pass
        else:
            self.connection.close()
            self.cursor.close()
    def SQLLogin(self,ID,PW):
        try:
            self.connection = mysql.connector.connect(user=ID,password=PW,host='172.22.55.148',database='OffdayProj3',port=3306)
        except mysql.connector.Error as err:
            return err.errno
        else:
            self.cursor=self.connection.cursor()
            self.loginsuccess = 1
            return 0
    def q_sort(self,left,right):
        if left>=right:
            return
        lhold=left
        rhold=right
        pivot=self.r[left]
        ppivot=self.p[left]
        while left<right:
            while self.r[right]>=pivot and left<right:
                right-=1
            if left!=right:
                self.r[left]=self.r[right]
                self.p[left]=self.p[right]
                left+=1
            while self.r[left]<=pivot and left<right:
                left+=1
            if left!=right:
                self.r[right]=self.r[left]
                self.p[right]=self.p[left]
                right-=1
        self.r[left]=pivot
        self.p[left]=ppivot
        pivot=left
        left=lhold
        right=rhold
        if left<pivot:
            self.q_sort(left,pivot-1)
        if right>pivot:
            self.q_sort(pivot+1,right)
    def LoadMember(self):
        self.maxMem=0
        self.maxSlot=0
        self.remained=0
        if self.loginsuccess==0:
            return 1
        query="select name from Member"
        self.cursor.execute(query)
        for name in self.cursor:
            self.AddMember(name[0],0)
    def LoadData(self,y,m,d):
        if self.loginsuccess==0:
            return 1
        y2=y
        m2=m+2
        if m2>12:
            y2+=1
            m2 -= 12
        for i in range(0,self.maxMem):
            tmpname = self.member[i].name
            query = "select outdate,indate,priority from Application where memNo like "
            query += str(i)+" and outdate>='"
            query += str(y)+"-"+str(m)+"-"+str(d)
            query += "' and indate<'"
            query += str(y2)+"-"+str(m2)+"-1'"
            self.cursor.execute(query)
            self.member[i].allocated=1
            for (outdate,indate,priority) in self.cursor:
                self.member[i].allocated=0
                self.member[i].wish[priority].start = CRefine(outdate)
                self.member[i].wish[priority].end = CRefine(indate)
    def FlushData(self,y,m):
        self.member.clear()
        self.slot.clear()
        self.maxMem=0
        self.maxSlot=0
        self.p.clear()
        self.r.clear()
        self.remained=0
        if self.loginsuccess==0:
            return
        y2 = y
        m2 = m+2
        if m2>12:
            y2 += 1
            m2 -= 12
        query = "delete from Application where outdate>='%d-%d-1' and outdate<'%d-%d-1'"
        self.cursor.execute(query,y,m,y2,m2)
        query = "delete from Fixed where outdate>='%d-%d-1' and outdate<'%d-%d-1'"
        self.cursor.execute(query,y,m,y2,m2)
    def SearchMemNo(self,name):
        for i in range(0,self.maxMem):
            if self.member[i].name == name:
                return i
        return -2
    def AddMember(self,name,qgo):
        i=self.SearchMemNo(name)
        if i>=0:
            return i
        if self.loginsuccess>0 and qgo>0:
            query = "insert into Member values ("+str(self.maxMem)+",'"+name+"')"
            self.cursor.execute(query)
        self.member.append(Member())
        self.member[self.maxMem].name=name
        self.maxMem+=1
        self.remained+=1
        return self.maxMem-1
    def AddSlot(self,y,m,d):
        self.LoadData(y,m,d)
        self.slot.append(Slot())
        self.slot[self.maxSlot].start=CRefine(y,m,d)
        self.slot[self.maxSlot].end=CRefine(y,m,d)
        self.slot[self.maxSlot].end.addDay(3)
        self.slot[self.maxSlot].num=0
        self.maxSlot+=1
        return 0
    def AutoAllocateSlot(self,y,m,d):
        PeriodEnd = CRefine(y,m,d)
        while PeriodEnd.m-m<2 and m-PeriodEnd.m<2:
            self.slot.append(Slot())
            self.slot[self.maxSlot].start = PeriodEnd.clone()
            self.slot[self.maxSlot].end = PeriodEnd.clone()
            self.slot[self.maxSlot].end.addDay(3)
            self.slot[self.maxSlot].num=0
            self.maxSlot+=1
            PeriodEnd.addDay(4)
        return 0
    def RandSimulate(self,y,m,d):
        for i in range(0,self.maxSlot):
            self.slot[i].list.clear()
        for i in range(0,self.maxMem):
            #allocate fixed vacations
            if self.member[i].allocated>0:
                slotleft=0
                while slotleft<self.maxSlot and self.member[i].wish[0].start.diffBtwn(self.slot[slotleft].start)>=0:
                    slotleft+=1
                slotleft-=1
                if slotleft>=self.maxSlot:
                    self.member[i].allocated=3
                    self.remained-=1
                    continue
                slotright=slotleft
                while slotright<self.maxSlot and self.member[i].wish[0].end.diffBtwn(self.slot[slotright].end)>0:
                    slotright+=1
                if slotright>=self.maxSlot:
                    slotright=self.maxSlot-1
                for j in range(slotleft,slotright+1):
                    self.slot[j].list.append(i)
                    self.slot[j].num+=1
        self.p.clear()
        self.r.clear()
        for i in range(0,self.maxMem):
            self.p.append(i)
            self.r.append(random.random())
        self.q_sort(0,self.maxMem-1)
        level=0
        while self.remained>0 and level<2:
            for i in range(0,self.maxMem):
                if self.member[self.p[i]].allocated > 0:
                    continue
                for j in range(0,self.maxSlot):
                    if self.slot[j].start.diffBtwn(self.member[self.p[i]].wish[0].start) == 0:
                        break
                if self.slot[j].num<=level:
                    self.slot[j].list.append(self.p[i])
                    self.slot[j].num += 1
                    self.member[self.p[i]].allocated = 1
                    self.remained -= 1
                    continue
                for j in range(0,self.maxSlot):
                    if self.slot[j].start.diffBtwn(self.member[self.p[i]].wish[1].start) == 0:
                        break
                if self.slot[j].num<=level:
                    self.slot[j].list.append(self.p[i])
                    self.slot[j].num += 1
                    self.member[self.p[i]].allocated = 1
                    self.remained -= 1
                    continue
                for j in range(0,self.maxSlot):
                    if self.slot[j].start.diffBtwn(self.member[self.p[i]].wish[2].start) == 0:
                        break
                if self.slot[j].num<=level:
                    self.slot[j].list.append(self.p[i])
                    self.slot[j].num += 1
                    self.member[self.p[i]].allocated = 1
                    self.remained -= 1
                    continue
            level += 1
        return 0
    def SubmitWish(self,no,priority, y,m,d):
        priority -= 1
        if type(no)==str:
            no=self.AddMember(no,1)
            if no<0:
                return no
        if no>=self.maxMem or no<0:
            return -1
        if priority<0 or priority>2:
            return -2
        for i in range(priority,3):
            self.member[no].wish[i].start = CRefine(y,m,d)
            self.member[no].wish[i].end = CRefine(y,m,d)
            self.member[no].wish[i].end.addDay(3)
        self.member[no].allocated = 0
        if self.loginsuccess>0:
            outdatestr = self.member[no].wish[priority].start.refineToString()
            indatestr = self.member[no].wish[priority].end.refineToString()
            query = "insert into Application (memNo,outdate,indate,priority) values ("
            query += str(no)+",'"+outdatestr + "','"+ indatestr + "'," + str(priority) + ")"
            self.cursor.execute(query)
        return 0
    def InsertFixed(self,no, y,m,d, y2,m2,d2):
        if type(no)==str:
            no=self.AddMember(no,1)
            if no<0:
                return no
        self.member[no].wish[0].start = CRefine(y,m,d)
        self.member[no].wish[0].end = CRefine(y2,m2,d2)
        self.member[no].allocated = 2
        self.remained -= 1
        if self.loginsuccess>0:
            outdatestr = self.member[no].wish[0].start.refineToString()
            indatestr = self.member[no].wish[0].end.refineToString()
            query = "insert into fixed (outdate,indate) values ('%s','%s')"
            self.cursor.execute(query,outdatestr,indatestr)
        return 0
