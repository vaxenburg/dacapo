from .datasets import DataSet

from abc import ABC, abstractmethod


class DataSplit(ABC):

    @property
    @abstractmethod
    def train(self) -> DataSet:
        """The Dataset to train on."""
        pass

    @property
    @abstractmethod
    def validate(self) -> DataSet:
        """The Dataset to validate on."""
        pass