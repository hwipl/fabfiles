"""
Fabline that imports subdirectories and presents subdirectories as namespaces
"""

from invoke import Collection
import archlinux
import net

namespace = Collection(archlinux, net)
