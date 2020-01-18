"""
Fabfile for pacman related tasks
"""

import pathlib

from fabric import task


@task
def is_installed_package(conn, package=None):
    """
    Check if given package is installed
    """

    if package:
        result = conn.run("pacman -Qi {}".format(package), hide="both",
                          warn=True)
        if result.ok:
            print(True)
            return True

    print(False)
    return False


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
def install_package_file(conn, package=None):
    """
    Install given package file
    """

    if not package:
        return

    # get filename
    path = pathlib.PurePath(package)
    filename = path.name
    if not filename:
        return

    # copy file to remote host if not already there
    result = conn.run("ls {}".format(filename), hide="both", warn=True)
    copy = result.failed
    if copy:
        conn.put("{}".format(package))

    # install the package
    conn.sudo("pacman -U --noconfirm {}".format(filename), warn=True)

    # if we copied the package, clean up
    if copy:
        conn.run("rm {}".format(filename))


@task
def update_packages(conn):
    """
    Update all installed packages
    """

    conn.run("pacman -Syu")
