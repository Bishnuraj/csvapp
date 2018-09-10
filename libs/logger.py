import logging
logging.basicConfig(
    format='%(asctime)s\t%(name)-16s\t%(funcName)22s:%(lineno)d\t%(levelname)s\t%(message)s',
    level=logging.INFO)

# logging wrapper
def getLogger(name):
    log = logging.getLogger(name)
    return log
