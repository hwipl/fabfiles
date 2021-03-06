"""
Fabfile for makepkg related tasks
"""

from fabric import task


@task
def makepkg(conn, path=None, parameters=None, sudo=False):
    """
    Make a package with the makepkg tool
    """

    if not path:
        return

    makepkg_command = f"bash -l -c \"cd {path} && makepkg"
    if parameters:
        makepkg_command += f" {parameters}"
    makepkg_command += "\""

    if sudo:
        conn.sudo(makepkg_command)
    else:
        conn.run(makepkg_command)
