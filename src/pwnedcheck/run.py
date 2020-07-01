# Main file for the PwnedCheck distribution.
# This file retrieves the password, calls the module check_pwd,
# and check if the password has been breached by checking it with
# the database in the following website
# https://haveibeenpwned.com/Passwords

import sys
import logging
from getpass import getpass
from pwnedcheck.check_pwd import check_pwd

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
log = logging.getLogger(__name__)


def splash():
    """Splash `pwnedcheck` logo and information."""
    print(" ____________________________________________________________ ")
    print("|                               _      _               _     |")
    print("|  _ ____      ___ __   ___  __| | ___| |__   ___  ___| | __ |")
    print("| | '_ \ \ /\ / / '_ \ / _ \/ _` |/ __| '_ \ / _ \/ __| |/ / |")
    print("| | |_) \ V  V /| | | |  __/ (_| | (__| | | |  __/ (__|   <  |")
    print("| | .__/ \_/\_/ |_| |_|\___|\__,_|\___|_| |_|\___|\___|_|\_\ |")
    print("| |_|                                                        |")
    print("| Author: Tanjona R. Rabemananjara                           |")
    print("| URL: https://radonirinaunimi.github.io/pwnd-check/         |")
    print("|____________________________________________________________|")


def main():
    """Function that fetchs the password given by the user from the command
    line using `getpass`. The password is then checked.
    """
    splash()
    print("Enter your password:")
    pwd = getpass()
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
