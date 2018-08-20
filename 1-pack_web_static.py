#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

"""
    This fabric script will generate a .tgz archive from web_static folder
"""


def do_pack():
    """
    do_pack: This function will convert the file into the .tgz format
    running on local for contents in web_static

    Return archive path if correctly generated or else return None
    """
    local("mkdir -p versions")
    cur_time = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_name = "versions/web_static_{}.tgz".format(cur_time)
    tgz_vert = local("tar -cvzf {} web_static".format(arch_name))

    if tgz_vert.succeeded:
        return arch_name
    else:
        return None
