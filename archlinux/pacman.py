"""
Fabfile for pacman related tasks
"""

from fabric import task


@task
def get_installed_packages(conn):
    """
    Get list of installed packages
    """

    conn.run("pacman -Qqe")


@task
def find_packages(conn, search=None):
    """
    Find packages matching given search string
    """

    if search:
        conn.run("pacman -Ss {}".format(search))


@task
def install_packages(conn, packages=None):
    """
    Install given packages
    """

    if packages:
        conn.run("pacman -S {}".format(packages))


@task
def uninstall_packages(conn, packages=None):
    """
    Uninstall given packages
    """

    if packages:
        conn.run("pacman -R {}".format(packages))


@task
def update_packages(conn):
    """
    Update all installed packages
    """

    conn.run("pacman -Syu")
