"""
Fabfile for pacman related tasks
"""

from fabric import task


@task
def get_installed_packages(conn):
    """
    Get list of installed packages with pacman
    """

    conn.run("pacman -Qqe")
