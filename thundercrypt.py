#!/usr/bin/env python

import bcrypt
import argparse


__tool_version__ = '0.1'
__tool_author__ = 'lc0des'

def run(args):
    newpassword = args.newpassword.encode()
    thunderoff = args.thunderoff

    hashedpw = bcrypt.hashpw(newpassword,bcrypt.gensalt()).decode()
    if thunderoff:
        print(hashedpw)
    else:
        line = 'masterPassword: thunderhub-{0}'.format(hashedpw)
        print(line)

def main():
	parser_desc = 'bcrypt password generator with thunderhub umbrel support'.format(__tool_version__,__tool_author__)
	prog_desc = 'thundercrypt.py'
	parser = argparse.ArgumentParser(prog = prog_desc, description=parser_desc)
	parser.add_argument("-p","--password",action="store",required=True,help='password to bcrypt',dest='newpassword')
	parser.add_argument("-t","--thunderhub-off",action="store_true",required=False,help='disable thunderhub mode',default=False, dest='thunderoff')
	args = parser.parse_args()
	run(args)

if __name__ == "__main__":
	main()
