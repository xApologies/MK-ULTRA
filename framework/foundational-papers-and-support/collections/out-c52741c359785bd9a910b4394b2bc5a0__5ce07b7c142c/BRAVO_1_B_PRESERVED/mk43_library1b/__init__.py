from .library import MK43Library

def create_module():
    return MK43Library()

__all__ = ["MK43Library", "create_module"]
