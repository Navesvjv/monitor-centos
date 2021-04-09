from log import Log
from commands import Commands

cmd = Commands()
log = Log()

cmd.exec('ls -la')
cmd.exec('ping -c1 8.8.8.8')
cmd.exec('ping -c1 192.168.21.34')

log = Log()
log.createLog()
log.saveLog(cmd.outputs)