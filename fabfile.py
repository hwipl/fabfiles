"""
Fabline that imports subdirectories and presents subdirectories as namespaces
"""

from invoke import Collection
import archlinux
import net
import qemu
import run
import shutdown

namespace = Collection(archlinux, net, qemu, run, shutdown)
