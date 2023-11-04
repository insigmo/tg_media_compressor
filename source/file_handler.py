from pathlib import Path

from source.compressors.audio import AudioCompressor
from source.compressors.image import ImageCompressor
from source.compressors.pdf import PDFCompressor
from source.compressors.video import VideoCompressor
from source.models.file_params import FileParams
from source.models.mime_type import FileFormats
from source.models.result import Result


class FileCompressor:
    @classmethod
    def run(cls, file_params: FileParams) -> Result:
        methods = {
            FileFormats.JPEG: cls._image_compressor,
            FileFormats.PNG: cls._image_compressor,
            FileFormats.GIF: cls._image_compressor,
            FileFormats.WEBP: cls._image_compressor,
            FileFormats.MP3: cls._audio_compressor,
            FileFormats.MP4: cls._video_compressor,
            FileFormats.QUICK_TIME: cls._video_compressor,
            FileFormats.PDF: cls._pdf_compressor,
        }
        return methods[file_params.mime_type](file_params)  # type: ignore

    @classmethod
    def _image_compressor(cls, file_params: FileParams) -> Result:
        return ImageCompressor().compress(file_params)

    @classmethod
    def _video_compressor(cls, file_params: FileParams) -> Result:
        return VideoCompressor().compress(file_params)

    @classmethod
    def _audio_compressor(cls, file_params: FileParams) -> Result:
        return AudioCompressor().compress(file_params)

    @classmethod
    def _pdf_compressor(cls, file_params: FileParams) -> Result:
        return PDFCompressor().compress(file_params)


if __name__ == '__main__':
    params = FileParams(
        file_id='BQACAgIAAxkBAAMQZUZtrCwPyguWv-2TCnO8OJY4yA8AAqA7AAIflzFKcjN5zOuK3V0zBA',
        file_name='MicrosoftTeams-image.png',
        file_size=20007,
        file_unique_id='AgADoDsAAh-XMUo',
        mime_type='image/jpeg',
    )
    FileCompressor.run(params)
