from log import Log
from commands import exec
from docker import *

log = Log()

upDocker(log)

log.createLog()
log.saveLog()