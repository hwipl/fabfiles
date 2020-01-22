"""
Fabfile for os related tasks
"""

from fabric import task


@task
def reboot(conn):
    """
    Reboot the os (with sudo)
    """

    conn.sudo("reboot")


@task
def shutdown(conn):
    """
    Shutdown the os (with sudo)
    """

    conn.sudo("shutdown -h now")
