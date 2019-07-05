"""
Fabfile for qemu image (qemu-img) related tasks
"""

from fabric import task


@task
def create_image(conn, file_name=None, file_size=None, file_format="qcow2"):
    """
    Create disk image with given file name, size, and format
    """

    if not file_name or not file_size:
        return

    conn.run("qemu-img create -f {} {} {}".format(file_format, file_name,
                                                  file_size))
