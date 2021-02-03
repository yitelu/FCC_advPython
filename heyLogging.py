import logging

'''
##########
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')

# 5 different logging level

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is an error message')
logging.critical('this is a critical message')

logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logger.FileHandler('file.log')

# level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')


# include the stack trace in log

try:
    a =[1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)

#############
'''

