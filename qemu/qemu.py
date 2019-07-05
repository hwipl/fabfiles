"""
Fabfile for qemu related tasks
"""

from fabric import task

# name of qemu executable
QEMU = "qemu-system-x86_64"


@task
def run_vm(conn, options=""):
    """
    Run a VM with given options
    """

    conn.run("{} {}".format(QEMU, options))
