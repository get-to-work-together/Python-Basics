import logging

logging.basicConfig(filename = 'example.log', # or to a file 'example.log',
                    level = logging.WARNING,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%Y-%m-%dT%H:%M:%S')


# ---------------------------------------------------

for s in 'what the hell is going on'.split():
    logging.debug(s)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('Watch out!')
logging.critical('ERROR!!!!!')

try:
    n = int('one')
except Exception as ex:
    logging.error(ex)
