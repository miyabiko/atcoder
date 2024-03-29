import os
import sys
from shutil import copyfile


def path_check(directory_name):
    return os.path.exists('./' + directory_name)


def make_contest_dir(contest_name, contest_num):
    if contest_num != '':
        new_contest = contest_name.upper() + '/' + contest_name.upper() + contest_num
    else:
        new_contest = 'other/' + contest_name
    if path_check(new_contest):
        print('This contest is already there.')
        return
    print('Making ' + new_contest)
    os.mkdir(new_contest)
    for i in range(6):
        new_problem = chr(ord('A') + i) + '.py'
        copyfile('./template.py', './' + new_contest + '/' + new_problem)
    print('Done')
    return


if __name__ == '__main__':
    g_contest_name, g_contest_num = '', ''
    exe_arg = sys.argv[1:]
    if len(exe_arg) == 2:
        g_contest_name, g_contest_num = exe_arg
    elif len(exe_arg) == 1:
        g_contest_name = exe_arg[0]
    if g_contest_num != '':
        g_contest_num = g_contest_num.zfill(3)
    
    make_contest_dir(g_contest_name, g_contest_num)