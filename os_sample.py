import os
import logging
"""Studying functions from os module"""


logging.basicConfig(level=logging.DEBUG,
                    filename="os_sample.log",
                    filemode="w")

logging.info('List of files in working directory: ')
file_list = os.listdir('.')
logging.info(file_list)

file_list.sort()

logging.info('Sorted list of files in working directory: ')
logging.info(file_list)
