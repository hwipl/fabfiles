"""
Fabline that imports subdirectories and presents subdirectories as namespaces
"""

from invoke import Collection
import archlinux
import qemu
import net

namespace = Collection(archlinux, qemu, net)
