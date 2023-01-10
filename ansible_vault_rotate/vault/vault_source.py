from abc import ABC, abstractmethod


class VaultSource(ABC):
    """
    Implement this method to enable a different source for vault secrets
    """
    def __init__(self, source: str):
        self.source = source

    @abstractmethod
    def read(self) -> str:
        pass


class FileVaultSource(VaultSource):
    """
    Implementation of VaultSource to load secret from file
    """
    def read(self) -> str:
        with open(self.source.replace("file://", ""), "r") as f:
            return f.read().rstrip()


class TextVaultSource(VaultSource):
    """
    Implementation of VaultSource to load secret from given text
    """
    def read(self) -> str:
        return self.source


def build_vault_source(raw: str) -> VaultSource:
    """
    Construct correct VaultSource based on input provided
    :param raw: Raw text
    """
    if raw.startswith("file://"):
        return FileVaultSource(raw)
    else:
        return TextVaultSource(raw)