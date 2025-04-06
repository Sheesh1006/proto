from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetNotesRequest(_message.Message):
    __slots__ = ("video", "presentation")
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    video: bytes
    presentation: bytes
    def __init__(self, video: _Optional[bytes] = ..., presentation: _Optional[bytes] = ...) -> None: ...

class GetNotesResponse(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: bytes
    def __init__(self, notes: _Optional[bytes] = ...) -> None: ...
