import argparse
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt="%Y-%m-%d %H:%M:%S",
    format='[%(asctime)s] %(levelname)s --> %(module)s: %(message)s'
)

import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bt_04.main import parse_argument

class student:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age
    def infor(self):
        logging.info(self.Name)
        logging.info(self.Age)
if __name__ == "__main__":
    argument = parse_argument()
    s = student(argument.module,argument.test_name)
    s.infor()