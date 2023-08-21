from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("python_anvil_encryption")
except PackageNotFoundError:
    __version__ = "(local)"

del PackageNotFoundError
del version
