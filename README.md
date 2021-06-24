# thundercrypt

This is a simple script for supporting the task of setting a new password for [thunderhub](https://github.com/apotdevin/thunderhub).

No flag gives error message and the supported flags
```
$ python thundercrypt.py 
usage: thundercrypt.py [-h] -p NEWPASSWORD [-t]
thundercrypt.py: error: the following arguments are required: -p/--password
```
Thunderhub-Mode is default, -p waits for the password:
```
$ python thundercrypt.py -p securepassword
masterPassword: thunderhub-$2b$12$dysPVg6cRkoz0Qkq1EjMTu.iCXKOVSEybza8b8z3kxVlgyhLPpEW2
```
For just getting the hash and no thunderhub configuration line use the -t flag as well:
```
python thundercrypt.py -p securepassword -t
$2b$12$iE1uGSYSqPMS2wOZAmObae7qGO/qM7S5GXt0YvuFs380V.Cq6XRcS
```

# Happy Securing
