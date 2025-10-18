import argparse
import logging
import sys
import os

# Add project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
    datefmt="%Y-%m-%d %H:%M:%S",
    format='[%(asctime)s] %(levelname)s --> %(module)s: %(message)s'
)

def parse_argument():
    # 1. Create the parser
    parser = argparse.ArgumentParser(description="A simple argparse example")

    # 2. Add arguments

    parser.add_argument("-m", "--module", type=str, help="Module")
    parser.add_argument("-t", "--test_name",nargs="+", type=str, help="test_name")

    # 3. Parse arguments
    return parser.parse_args()

if __name__ == "__main__":
    argument = parse_argument()
    print(argument.module, argument.test_name)
    logging.info("This is an info message.")