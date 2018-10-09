"""
    csc相关配置
"""
import pymysql

IP = '192.168.208.70'
URL = f"https://{IP}:8099/csc/index.html"
CREATE_VM_URL = f'{URL}#pages/resources/instances/vms/vm_create?previousPage=1'
DB = pymysql.connect(
    host=f'{IP}',
    port=3306,
    user='csc',
    password='csc',
    db='csc')
USER_ADMIN = {
    'username': 'admin',
    'password': '1234567890',
    'usertype': 'local'
}

