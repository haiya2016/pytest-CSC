"""
    csc相关配置
"""
import pymysql

IP = '192.168.208.110'

URL = f"https://{IP}:8099/csc/index.html"

GET_USER_ROLE = f'https://{IP}:8099/csc/api/v5.0.0/homepage/user'   # 云主机创建页面

MEMU_TREE = {
    '系统管理员': {
        '首页': [],
        '服务管理': [],
        '资源管理': ['数据中心', '可用分区', '物理主机'],
        '虚拟化资源管理': ['资源实例', 'VDC管理', 'VPC管理', '弹性伸缩组管理', '业务系统', '资源回收', '资源纳管'],
        '应用管理': ['软件管理', '脚本管理', '软件安装', '软件升级', '安装日志', '命令脚本'],
        '订单审批': [],
        '计费': ['计费规则', '计费清单'],
        '报表': ['资源报表', '使用报表', '自定义报表'],
        '系统配置': ['用户管理', '角色管理', '流程管理', '服务器配置', '告警配置', '首页配置', '告警通知', '字典管理', 'License']
    }
}

DB = pymysql.connect(
    host=f'{IP}',
    port=3306,
    user='csc',
    password='csc',
    db='csc'
)

USER_ADMIN = {
    '账号': 'admin',
    '密码': '1234567890',
    '昵称': '系统管理员',
    '类型': '本地'
}

LOGIN_COOKIE_PATH = ".\\workspace\\data\\cookie.txt"  # cookie文件保存位置

POWERVC = 'https://192.168.214.246/powervc/login.html'

USER_PVC = {
    '账号': 'root',
    '密码': '1qaz@WSX3edc'
}


