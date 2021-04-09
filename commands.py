from log import Log
import subprocess as sbp

def exec(cmd, log):
    status, output = sbp.getstatusoutput(cmd)
    info = {'output': output, 'status': status, 'cmd': cmd}
    log.appendOutputs(info)
    return info
