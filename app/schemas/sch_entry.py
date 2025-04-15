from pydantic import BaseModel

class EntryUploadResponse(BaseModel):
    entry_id: int
    message: str