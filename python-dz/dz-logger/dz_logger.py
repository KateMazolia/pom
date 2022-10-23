# ОБЩЕЕ ЗАДАНИЕ:
#
# возьмите или напишите любую функцию(с параметрами) в отедельном файле
# произведите запись в лог файл данные о ее запуске (что она запустилась и закончила работу)
#
# *усложнение
# отоборазите данные переданных параметров

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )
logger = logging.getLogger("Mult_log")
logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logger.debug("logger with name: %s created", logger.name)


def multiply(a, b):
    logger.debug("received params %s, %s", a, b)
    res = a * b
    logger.debug("received number %s", res)
    return res

def main(name):
    logger.debug(f'Enter in the main() function: name={name}')


if __name__ == '__main__':
    main('multiply')
    multiply(9, 3)
