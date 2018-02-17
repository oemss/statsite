import os

from stats.models import analyz, pfr

def add2bd(link):
    cur_dir = os.path.abspath(os.curdir)
    outfile = open(cur_dir + link.replace('.', '_out.'), 'w')
    log = open(cur_dir + link.replace('.', '_log.'), 'w')
    answer = analyz.objects.filter(link).values()
    if len(answer) != 0:
        answer[0]
