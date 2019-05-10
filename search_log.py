#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import paramiko,time,signal,os,requests,json,sys
import interactive

def get_data(api, project):
        url = api +'?server_name='+ project
        try:
                res = requests.get(url, timeout = 5)
        except requests.RequestException as e:
                print (e)
        else:
                return res.json()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_utf8(value):
    if isinstance(value,int):
        return value
    return value.encode('utf-8').strip()

def log_print(colour,content):
    print colour + content + bcolors.ENDC

def get_raw_input(title):
    try:
        action = raw_input(title)
        return action.encode('utf-8').strip()
    except KeyboardInterrupt:
        log_print(bcolors.OKGREEN,"\nGoodbye!")
        sys.exit(0)

def get_print_info():
    os.system("clear")
    log_print(bcolors.OKGREEN,"=========================================")
    log_print(bcolors.OKGREEN,"=       Server logs viewer V1.8 beta")
    log_print(bcolors.OKGREEN,"=       Powered by python")
    log_print(bcolors.OKGREEN,"=       DevOps group")
    log_print(bcolors.OKGREEN,"=       Usage:./search_log.py")
    log_print(bcolors.OKGREEN,"=       Tail logfile: use tail -100f file.log")
    log_print(bcolors.OKGREEN,"=       View logfile: use less file.log")
    log_print(bcolors.OKGREEN,"=       View logfile: (Consider using the less command with 'less filename.log' rather than running 'cat filename.log')")
    log_print(bcolors.OKGREEN,"=========================================")


def get_project_info():
    aa = get_raw_input('Pls input e.g.(pre-jar-benzbmw-server|奔驰宝马-预发布):')
    if aa == '':
        get_project_info()
    HOSTS_API = 'https://ops.huihuang200.com/api/ansible/ProjectDetailExceptProd'
    hosts_inventory = get_data(HOSTS_API, str(aa))
    hosts_json = json.dumps(hosts_inventory,sort_keys=True, indent=4)
    print(hosts_json)
    s = json.loads(hosts_json)
    if s['server_type'] <> '':
        ssh_command(s)
    else:
	os.system("clear")
        get_print_info()
        get_project_info()

def ssh_command(s):
    private_key = paramiko.RSAKey.from_private_key_file('.id_rsa')
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(s['target'])
    channel=ssh.invoke_shell()
    channel.send('cd '+ s['app_logs_path'] +';ls -alt\n')
    time.sleep(0.1)
    interactive.interactive_shell(channel)
    channel.close()
    ssh.close()

def do_ssh_command():
    s = get_project_info()
    ssh_command(s)


def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    get_print_info()
    get_project_info()


if __name__ == '__main__': main()

