"""
Fabline that imports subdirectories and presents subdirectories as namespaces
"""

from invoke import Collection
import archlinux
import net
import qemu
import shutdown

namespace = Collection(archlinux, net, qemu, shutdown)
