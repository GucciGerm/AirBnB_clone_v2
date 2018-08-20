#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

"""
    This fabric script will generate a .tgz archive from web_static folder
"""
env.hosts = ['104.196.101.39', '104.196.187.5']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    This fabric script will distribute an archive to our servers
    using a function we create called do_deploy
    Return True if file at the path archive or else False if not existent
    """

    if os.path.exists(archive_path):
        archive_input = archive_path[9:]
        new_arch_path = "/data/web_static/releases/" + archive_input[:-4]
        archive_input = "/tmp/" + archive_input
        print(archive_input)
        print(new_arch_path)
        print(archive_input)
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_arch_path))
        run("sudo tar -xzf {} -C {}/".format(archive_input, new_arch_path))
        run("sudo rm {}".format(archive_input))
        run("sudo mv {}/web_static/* {}".format(new_arch_path, new_arch_path))
        run("sudo rm -rf {}/web_static".format(new_arch_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_arch_path))
        print("New version deployed!")
        return True

    return False
