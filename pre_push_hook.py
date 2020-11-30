#!/usr/bin/env python

import argparse
import os
import subprocess
import sys


def run_checks():
    checks = ['run-qa-checks', 'runtests.py']
    MAIN_DIR = os.getcwd()
    failed_checks = []
    for check in checks:
        task = subprocess.Popen(f'{MAIN_DIR}/{check}')
        task.communicate()
        if task.returncode:
            failed_checks.append(check)
    if len(failed_checks):
        print("The following checks failed")
        print("---------------------------")
        for check in failed_checks:
            print(check)
        sys.exit(1)


def make_executable(f):
    task = subprocess.Popen(
        ['chmod', '+x', f], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    res, err = task.communicate()
    return res, err


def install_hook():
    MAIN_DIR = os.getcwd()
    HOOKS_DIR = os.path.join(MAIN_DIR, '.git', 'hooks')
    hook_file = os.path.join(HOOKS_DIR, 'pre-push')
    symlink = os.path.islink(hook_file)
    if symlink and os.path.exists(hook_file):
        print('Symlink already exists')
    else:
        if symlink:
            os.unlink(hook_file)
        os.symlink(os.path.abspath(__file__), hook_file)
        print('Symlink created')

    # Makes the hook file executable
    res, err = make_executable(hook_file)
    if err:
        raise ValueError(err)


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('remote', nargs='?', help='provided by git before push')
    parser.add_argument('url', nargs='?', help='provided by git before push')
    parser.add_argument(
        '--install', action='store_true', default=False,
    )
    args = parser.parse_args(args=args)
    if args.install:
        return install_hook()
    run_checks()


if __name__ == '__main__':
    main()
