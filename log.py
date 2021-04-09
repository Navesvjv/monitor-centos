import os
import datetime as dt
import subprocess as sbp

pathABS = os.path.abspath(os.path.dirname(__file__))
pathABS += f'/log'

class Log:
    def __init__(self, nameLog='LogMonitor', pathLog=pathABS):
        self.outputs = []
        self.dateNow = dt.datetime.now().strftime(r'%d-%m-%Y--%H-%M-%S')
        self.nameLog = f'{nameLog}-{self.dateNow}'
        self.pathLog = pathLog
        self.touch   = f'{self.pathLog}/{self.nameLog}'

    def createLog(self):
        sbp.getoutput(f'mkdir -p {self.pathLog}')
        sbp.getoutput(f'touch {self.touch}')

    def appendOutputs(self, output):
        self.outputs.append(output)

    def saveLog(self):
        with open(self.touch, 'w') as arqLog:
            for i in self.outputs:
                strr = f'====================   status: {i["status"]} --> {i["cmd"]}     ====================\n'
                strr += f'{i["output"]}\n\n'
                arqLog.write(strr)

                


                