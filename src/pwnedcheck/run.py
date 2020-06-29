# Main file for the PwnedCheck

import sys
import logging
import argparse
from pwnedcheck.check_pwd import check_pwd

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
log = logging.getLogger(__name__)


def check_str(value):
    """check if the input value is actually a string.

    Parameters
    ----------
        value: str
            User input
    """
    ivalue = value
    if not isinstance(ivalue, str):
        raise argparse.ArgumentTypeError(f"{ivalue} is not a valid argument")
    return ivalue


def parser():
    """Parse input from command line."""
    parser = argparse.ArgumentParser(description="Password breach checkers")
    parser.add_argument("-p", "--passd", help="Password", type=check_str, required=True)
    args = parser.parse_args()
    return args


def main():
    """Main function that looks for the password."""
    args = parser()
    pwd = args.passd.strip()
    try:
        # Check the pwd and add the values to some variables
        hashed_pwd, nb_match = check_pwd(pwd)
        # Print the result
        if nb_match:
            print(f"The password occurs {nb_match} times (hash: {hashed_pwd})")
        else:
            print("Your password was not found")
    except UnicodeError:
        errormsg = sys.exc_info()[1]
        log.warning(f"Your password could not be checked: {errormsg}")
