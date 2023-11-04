from pathlib import Path

from pydantic import BaseModel

from source.models.mime_type import FileFormats


class FileParams(BaseModel):
    file_id: str
    file_path: Path
    file_size: int
    file_unique_id: str
    mime_type: FileFormats
