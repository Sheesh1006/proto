from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetRawNotesRequest(_message.Message):
    __slots__ = ("video", "presentation")
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    video: bytes
    presentation: bytes
    def __init__(self, video: _Optional[bytes] = ..., presentation: _Optional[bytes] = ...) -> None: ...

class GetRawNotesResponse(_message.Message):
    __slots__ = ("raw_notes",)
    RAW_NOTES_FIELD_NUMBER: _ClassVar[int]
    raw_notes: str
    def __init__(self, raw_notes: _Optional[str] = ...) -> None: ...

class GetTimestampsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetTimestampsResponse(_message.Message):
    __slots__ = ("timestamps",)
    TIMESTAMPS_FIELD_NUMBER: _ClassVar[int]
    timestamps: str
    def __init__(self, timestamps: _Optional[str] = ...) -> None: ...

class GetKeyFramesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetKeyFramesResponse(_message.Message):
    __slots__ = ("keyframes",)
    KEYFRAMES_FIELD_NUMBER: _ClassVar[int]
    keyframes: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, keyframes: _Optional[_Iterable[bytes]] = ...) -> None: ...
