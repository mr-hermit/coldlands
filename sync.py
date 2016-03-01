import git
import os

g = git.cmd.Git(os.path.dirname(__file__))
g.pull()