from commands import exec

def upDocker(log):
    info = exec('docker info', log)
    if info['status'] != 0:
        start = exec('systemctl start dockera', log)
        if start['status'] != 0:
            pass
            # Notificar
            # exit


def upSamba(log):
    retr = exec('ping -c1 192.168.1.4', log)
    if retr['status'] != 0:
        exec('docker start samba', log)