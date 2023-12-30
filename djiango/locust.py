from locust import HttpUser, task, between

import random
import string


def usernumber_generator():
    for i in range(100000, 200000):
        yield str(i).zfill(5)
def studentnumber_generator():
    for i in range(200000, 300000):
        yield str(i).zfill(5)
def coursenumberG():
    for i in range(200000, 500000):
        yield str(i).zfill(5)
class QuickstartUser(HttpUser):
    # wait_time = between(0, 0.3)

    usernumber_genlogin = usernumber_generator()
    usernumber_genregister = usernumber_generator()
    coursenumber=coursenumberG()
    studentnumberR=studentnumber_generator()
    studentnumberL=studentnumber_generator()
    studentCourseNumber=coursenumberG()
    token = []
    stuToken=[]


    @task
    def login(self):
        usernumber = next(self.usernumber_genlogin)

        rsp=self.client.post("/login", json={
            "Authentication": 1,
            "password": "1111",
            "username": "test",
            "usernumber": usernumber
        })
        if rsp.status_code == 200:
            if(rsp.json()['status']=='success'):
                self.token.append(rsp.json()['token'])
    @task
    def studentResgister(self):
        usernumber = next(self.studentnumberR)
        rsp=self.client.post("/register", json={
            "Authentication": 0,
            "password": "1111",
            "username": "test",
            "usernumber": usernumber,
            "course": "1",
            "academy": "bdi"
        })
    @task
    def StuLogin(self):
        usernumber = next(self.studentnumberL)
        rsp=self.client.post("/login", json={
            "Authentication": 0,
            "password": "1111",
            "username": "test",
            "usernumber": usernumber
        })
        if rsp.status_code == 200:
            if(rsp.json()['status']=='success'):
                self.stuToken.append(rsp.json()['token'])
    @task
    def StuAddCourseAndgetSignData(self):
        coursenumber=next(self.studentCourseNumber)
        if len(self.stuToken)!=0:
            token=self.stuToken[random.randint(0,len(self.stuToken)-1)]
            rsp=self.client.post("/addCourse", json={
                "classnumber": coursenumber,
                "classname": coursenumber,
            }, headers={'Authorization': f'Token {token}'})
            rsp = self.client.get("/student/getStudentSignin", params={"classname":coursenumber},
                                  headers={'Authorization': f'Token {token}'})

    @task
    def addCourseBeginSign(self):
        coursenumber=next(self.coursenumber)
        if len(self.token)!=0:
            token=self.token[random.randint(0,len(self.token)-1)]

            rsp=self.client.post("/addCourse", json={
                "classnumber": coursenumber,
                "classname": coursenumber,
            }, headers={'Authorization': f'Token {token}'})
            rsp = self.client.post("/teacher/teacherRegisterEachCourse", params={
                "classnumber": coursenumber,
                "limittime": "60",
            }, headers={'Authorization': f'Token {token}'})

    @task
    def getCourse(self):
        if len(self.token) != 0:

            token = self.token[random.randint(0, len(self.token) - 1)]
            rsp=self.client.get("/getCourseList", headers={'Authorization': f'Token {token}'})


    @task
    def register(self):
        # Generate random usernumber and username for each new user

        usernumber = next(self.usernumber_genregister)
        # print("register",usernumber)
        username = 'test'

        self.client.post("/register", json={
            "Authentication": 1,
            "password": "1111",
            "username": username,
            "usernumber": usernumber,
            "course": "1",
            "academy": "bdi"
        })

        # headers = {'Authorization': self.client.reque}
    # def on_start(self):
    #     self.register()
    #     self.login()
    #     self.addCourse()
    #     self.getCourse()

