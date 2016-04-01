#!/usr/bin/env python
import os
import sys
import socket

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coldlands.settings")

    if socket.gethostname() == 'ws-2227':
        os.environ["DJANGO_SETTINGS_MODULE"] = "coldlands.settings_local"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
