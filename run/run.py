"""
Fabfile for tasks that allow running other executables
"""

import pathlib
from fabric import task


@task
def bash(conn, exe=None, sudo=False):
    """
    Run another executable using bash -l -c
    """

    if not exe:
        return

    # TODO: file copying parts taken from archlinux.install_package_file
    #       combine somehow?
    # get filename
    path = pathlib.PurePath(exe)
    filename = path.name
    if not filename:
        return

    # check if exe file is in PATH or current dir
    result = conn.run(f"bash -l -c \"which {filename}\"", hide="both",
                      warn=True)
    inpath = result.ok

    if not inpath:
        result = conn.run(f"ls {filename}", hide="both", warn=True)
    copy = result.failed

    # TODO: check this when running locally
    # copy file to remote host if not already there
    if copy:
        conn.put(f"{exe}")

    # run the command
    cmd = f"bash -l -c \"./{exe}\""
    if inpath:
        cmd = f"bash -l -c \"{exe}\""
    if sudo:
        conn.sudo(cmd, warn=True)
    else:
        conn.run(cmd, warn=True)

    # if we copied the exe, clean up
    if copy:
        conn.run(f"rm {filename}")
