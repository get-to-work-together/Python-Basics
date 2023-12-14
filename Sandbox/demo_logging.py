import logging

##logging.basicConfig(level = logging.DEBUG)
                    
logging.basicConfig(filename = None, # or to a file 'example.log',
                    level = logging.ERROR,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%Y-%m-%dT%H:%M:%S')

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('Watch out!')
logging.critical('ERROR!!!!!')

try:
    n = int('one')
except Exception as ex:
    logging.error(ex)
