import time
import logging

logging.basicConfig(
    filename = 'example.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d - %(message)s',
)

t0 = time.perf_counter_ns()

logging.critical('CRITICAL ERROR !!!!')
logging.error('OOPS')
logging.warning('Watch out')
logging.info('I am now here')
logging.debug('Value=10')
time.sleep(1)

t1 = time.perf_counter_ns()

print('Duration in ns', t1 - t0)
