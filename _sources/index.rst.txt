CheckPwd documentation
======================

**CheckPwd** is a package that allows you to (1) check wether your passwords (already attached to some accounts)
have been leaked, or (2) give you an idea on which password you should not adopt for your next accounts. There 
are real dangers in using passwords that have already been breached. The password might have been added to a
dictionary that is used for hacking and therefore makes all the accounts attached to it extremely vulnerable.

`Have I Benn Pwned <https://haveibeenpwned.com/>`_ is a website that stores all of the credentials (email 
adrreses, passwords) that have been breached online. It also provides APIs that allows users to make specific 
requests. **CheckPwd** uses the `pwnedpasswords <https://haveibeenpwned.com/API/v3>`_ API to request the 
list of leaked password in a hashed format.


Is this secure?
---------------

Obviously, it is not ideal to send the entirety of your password to any website. What **CheckPwd** does is the 
following:

* splits the password into two parts and encrypts both using a SHA-1 hash format
* sends the first half to the website which then sends back a list of hashed passwords that contains the first
  half of the password
* finalizes the checks locally by comparing the list of hashed passwords to the second half of the password

This process makes sure that your password is not uploaded anywhere.


.. toctree::
   :maxdepth: 2
   :caption: HowTo


   howto/howto


.. toctree::
   :maxdepth: 2
   :caption: Modules


   modules/checkpwd/modules


.. automodule:: checkpwd
    :members:
    :noindex:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
