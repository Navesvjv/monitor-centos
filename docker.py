from commands import exec

def upDocker(log):
    count = 0
    while True:
        retr = exec('docker info', log)
        if retr['status'] != 0:
            exec('systemctl start docker', log)
        elif retr['status'] == 0 or count > 3:
            break
        count += 1

def upSamba(log):
    while True:
        retr = exec('ping -c1 192.168.1.4', log)
        if retr['status'] != 0:
            exec('docker start samba', log)
        else:
            break