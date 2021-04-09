import subprocess as sbp

class Commands:
    def __init__(self):
        self.output = ''
        self.status = ''
        self.outputs = []

    def exec(self, cmd):
        self.status, self.output = sbp.getstatusoutput(cmd)
        self.outputs.append({'output': self.output, 'status': self.status, 'cmd': cmd})