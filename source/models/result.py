from pathlib import Path

from pydantic import BaseModel


class Result(BaseModel):
    file_path: Path
    file_size_raw: int
    file_size_compressed: int
