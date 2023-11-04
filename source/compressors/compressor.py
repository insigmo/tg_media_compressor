import logging
from abc import ABC, abstractmethod

from source.models.file_params import FileParams
from source.models.result import Result


class Compressor(ABC):
    @abstractmethod
    def compress(self, file_params: FileParams) -> Result:
        pass

    @property
    def _logger(self) -> logging.Logger:
        return logging.getLogger(__name__)
