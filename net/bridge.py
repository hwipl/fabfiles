"""
Fabfile for bridge related tasks
"""

from fabric import task


def _is_bridge(conn, bridge):
    result = conn.run("ip link show {} type bridge".format(bridge),
                      hide="both", warn=True)
    if result.failed or not result.stdout:
        return False
    return True


@task
def is_bridge(conn, bridge=None):
    """
    Check if bridge with given name exists
    """

    if not bridge or not _is_bridge(conn, bridge):
        print(False)
        return False

    # device exists
    print(True)
    return True


@task
def add_bridge(conn, bridge=None):
    """
    Add bridge interface with given name
    """

    if not bridge:
        return

    if not _is_bridge(conn, bridge):
        conn.run("ip link add name {} type bridge".format(bridge))
    conn.run("ip link set {} up".format(bridge))


@task
def del_bridge(conn, bridge=None):
    """
    Delete bridge interface with given name
    """

    if not bridge:
        return

    conn.run("ip link delete name {} type bridge".format(bridge))


def _is_bridge_if(conn, bridge, iface):
    result = conn.run("bridge link show dev {}".format(iface),
                      hide="both", warn=True)
    parts = result.stdout.split()
    if len(parts) < 7:
        return False

    # parts[6] is device's master, i.e., the bridge name
    if parts[6] == bridge:
        return True
    return False


@task
def is_bridge_if(conn, bridge=None, iface=None):
    """
    Check if interface is port of bridge
    """

    if not bridge or not iface or not _is_bridge_if(conn, bridge, iface):
        print(False)
        return False

    print(True)
    return True


@task
def add_bridge_if(conn, bridge=None, iface=None):
    """
    Add interface to bridge
    """

    if not bridge or not iface:
        return

    conn.run("ip link set {} up".format(iface))
    conn.run("ip link set {} master {}".format(iface, bridge))


@task
def del_bridge_if(conn, bridge=None, iface=None):
    """
    Add interface to bridge
    """

    if not bridge or not iface:
        return

    if not _is_bridge_if(conn, bridge, iface):
        return

    conn.run("ip link set {} nomaster".format(iface))
    conn.run("ip link set {} down".format(iface))
