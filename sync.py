#!/usr/bin/python

import git
import os
import time

rpath = '/home/hermit/coldlands'
rpath = 'C:\Users\zolotko\workspace\coldlands'
g = git.cmd.Git('C:\Users\zolotko\workspace\coldlands')
message = g.pull()

print ('%s: %s' % (time.strftime("%H:%M:%S"),message))
