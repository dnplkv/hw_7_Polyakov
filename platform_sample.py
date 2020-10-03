import platform
import logging
"""Studying functions from platform module"""


logging.basicConfig(level=logging.DEBUG,
                    filename="platform_sample.log",
                    filemode="w")

logging.info('Underlying platform’s identifying data: ')

logging.info(f'Version           : {platform.python_version()}')
logging.info(f'Version tuple     : {platform.python_version_tuple()}')
logging.info(f'Compiler          : {platform.python_compiler()}')
logging.info(f'Build             : {platform.python_build()}')


logging.info(f'System            : {platform.system()}')
logging.info(f'Node              : {platform.node()}')
logging.info(f'Release           : {platform.release()}')
logging.info(f'Version           : {platform.version()}')
logging.info(f'Machine           : {platform.machine()}')
logging.info(f'Processor         : {platform.processor()}')
logging.info(f'Interpreter       : {platform.architecture()}')
