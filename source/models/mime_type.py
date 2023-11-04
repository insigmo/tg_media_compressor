from enum import StrEnum


class FileFormats(StrEnum):
    JPEG = "image/jpeg"
    GIF = "image/gif"
    PNG = "image/png"
    PDF = "application/pdf"
    MP3 = "audio/mpeg"
    QUICK_TIME = "video/quicktime"
    MP4 = "video/mp4"
    WEBP = "image/webp"
