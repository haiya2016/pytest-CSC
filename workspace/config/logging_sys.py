'''
日志系统，用于将日志输出到控制台和日志文件
'''
import logging
import logging.handlers
import logging.config
import yaml

class Logger(object):
    '''日志系统'''
    def __init__(self, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''
        self.logger = logging.getLogger(logger)     # 创建一个logger，作为日志的容器
        yaml_file = './workspace/config/logging_config.yaml'
        with open(yaml_file, 'rt') as yfile:
            conf = yaml.safe_load(yfile.read())
        logging.config.dictConfig(conf)         # 使用yaml文件作为配置

    def getlog(self):
        '''返回一个logger'''
        return self.logger


# datacenter_loc = ('By.XPATH', '//*[@id="dragDiv5"]/div[2]/div[1]/select')
# lo = Logger('test').getlog()
# lo.info(f'就是这样：{datacenter_loc}')
# lo = Logger('test2').getlog()
# lo.info(f'就是这样2：{datacenter_loc}')
