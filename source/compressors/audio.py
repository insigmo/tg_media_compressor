from source.compressors.compressor import Compressor
from source.models.file_params import FileParams
from source.models.result import Result


class AudioCompressor(Compressor):
    def compress(self, file_params: FileParams, quality: int = 75):
        compressed_file = file_params.file_path.parent / ("compressed" + file_params.file_path.name)

        self._logger.debug(f'File {file_params.file_path} compressed to {compressed_file}')
        return Result(
            file_path=compressed_file,
            file_size_raw=file_params.file_path.stat().st_size,
            file_size_compressed=compressed_file.stat().st_size
        )
