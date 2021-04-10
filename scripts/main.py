from utils.log import Log
from utils.commands import exec
from docker import *

log = Log()

#upDocker(log)
exec('ls -la | grep "git"', log)


log.createLog()
log.saveLog()