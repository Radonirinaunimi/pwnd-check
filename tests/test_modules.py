# This file collects a few examples on how the modules of
# the package can be tested. This file can also be used by
# the github continuous integration (CI) to the test the code
# everytime there is a push.
#
# The <test coverage> can then be assessed using pytest-cov.
# This basically tests how many percents of the modules are
# being tested.
#
# Documentation:
# https://docs.pytest.org/en/stable/contents.html

from pwnedcheck.run import check_str
from pwnedcheck.check_pwd import check_pwd


# -- Test check_pwd --------------------------------------------------


def test_check_pwd():
    """Check if the modules `check_pwd` is return a tuple of hash and
    integer.
    """
    pwd = "password"
    pwd_hash, pwd_count = check_pwd(pwd)
    assert isinstance(pwd_count, int) and isinstance(pwd_hash, str)


# -- Test check string -----------------------------------------------


def test_check_str():
    """Test the modules that checks the type of the argument that is
    parsed from the command line.
    """
    string = "This is just a test"
    assert check_str(string) == string
