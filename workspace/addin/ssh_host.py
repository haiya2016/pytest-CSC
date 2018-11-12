# coding = utf-8

import paramiko

hosts_list = [
    {
        '周末关机':False,
        'IP':'192.168.206.209',
        '端口':'22',
        '账号':'root',
        '密码':'winserver123!@#'
    },
    {
        '是否周末关机':True,
        'IP':'192.168.206.222',
        '端口':'22',
        '账号':'root',
        '密码':'passw0rd1'
    }
]

for index, host_info in enumerate(hosts_list):
    if host_info['周末关机']:
        SSH = paramiko.SSHClient()
        SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 跳过了远程连接中选择‘是’的环节,
        SSH.connect(host_info['IP'], host_info['端口'], host_info['账号'], host_info['密码'])
        STDIN, STDOUT, STDERR = SSH.exec_command('shutdown')
        if STDOUT.read():
            result = STDOUT.read().decode('utf-8')
        else:
            result = STDERR.read().decode('utf-8')
        print(result)
        if 'Shutdown scheduled for' in result:
            print(host_info['IP'] + '即将关机')
        SSH.close()


