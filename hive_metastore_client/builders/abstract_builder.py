"""Abstract Builder Class."""
from abc import ABCMeta, abstractmethod


class AbstractBuilder(metaclass=ABCMeta):
    """Abstract Builder class to define builder methods to be implemented."""

    @abstractmethod
    def build(self) -> object:
        """
        To be implemented by each subclass and build the respective object.

        :return: an instance of the object to be built
        """
        pass
