from typing import Annotated

from pydantic import BaseModel, StringConstraints


class chat_payload(BaseModel):
    query: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=12000)]
    session_id: Annotated[str, StringConstraints(pattern=r"^\S+$", max_length=200)]
