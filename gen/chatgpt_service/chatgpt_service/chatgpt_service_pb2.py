# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chatgpt_service/chatgpt_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'chatgpt_service/chatgpt_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%chatgpt_service/chatgpt_service.proto\x12\x0f\x63hatgpt_service\"9\n\x12GetRawNotesRequest\x12\r\n\x05video\x18\x01 \x01(\x0c\x12\x14\n\x0cpresentation\x18\x02 \x01(\x0c\"(\n\x13GetRawNotesResponse\x12\x11\n\traw_notes\x18\x01 \x01(\t\"\x16\n\x14GetTimestampsRequest\"+\n\x15GetTimestampsResponse\x12\x12\n\ntimestamps\x18\x01 \x01(\t\"\x15\n\x13GetKeyFramesRequest\")\n\x14GetKeyFramesResponse\x12\x11\n\tkeyframes\x18\x01 \x03(\x0c\x32\xaf\x02\n\x0e\x43hatGPTService\x12\\\n\x0bGetRawNotes\x12#.chatgpt_service.GetRawNotesRequest\x1a$.chatgpt_service.GetRawNotesResponse(\x01\x30\x01\x12`\n\rGetTimestamps\x12%.chatgpt_service.GetTimestampsRequest\x1a&.chatgpt_service.GetTimestampsResponse0\x01\x12]\n\x0cGetKeyFrames\x12$.chatgpt_service.GetKeyFramesRequest\x1a%.chatgpt_service.GetKeyFramesResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chatgpt_service.chatgpt_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETRAWNOTESREQUEST']._serialized_start=58
  _globals['_GETRAWNOTESREQUEST']._serialized_end=115
  _globals['_GETRAWNOTESRESPONSE']._serialized_start=117
  _globals['_GETRAWNOTESRESPONSE']._serialized_end=157
  _globals['_GETTIMESTAMPSREQUEST']._serialized_start=159
  _globals['_GETTIMESTAMPSREQUEST']._serialized_end=181
  _globals['_GETTIMESTAMPSRESPONSE']._serialized_start=183
  _globals['_GETTIMESTAMPSRESPONSE']._serialized_end=226
  _globals['_GETKEYFRAMESREQUEST']._serialized_start=228
  _globals['_GETKEYFRAMESREQUEST']._serialized_end=249
  _globals['_GETKEYFRAMESRESPONSE']._serialized_start=251
  _globals['_GETKEYFRAMESRESPONSE']._serialized_end=292
  _globals['_CHATGPTSERVICE']._serialized_start=295
  _globals['_CHATGPTSERVICE']._serialized_end=598
# @@protoc_insertion_point(module_scope)
