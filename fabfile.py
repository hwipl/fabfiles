"""
Fabline that imports subdirectories and presents subdirectories as namespaces
"""

from invoke import Collection
import archlinux

namespace = Collection(archlinux)
