# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from backend_service import backend_service_pb2 as backend__service_dot_backend__service__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in backend_service/backend_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class BackendServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetNotes = channel.stream_stream(
                '/backend_service.BackendService/GetNotes',
                request_serializer=backend__service_dot_backend__service__pb2.GetNotesRequest.SerializeToString,
                response_deserializer=backend__service_dot_backend__service__pb2.GetNotesResponse.FromString,
                _registered_method=True)


class BackendServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetNotes(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BackendServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetNotes': grpc.stream_stream_rpc_method_handler(
                    servicer.GetNotes,
                    request_deserializer=backend__service_dot_backend__service__pb2.GetNotesRequest.FromString,
                    response_serializer=backend__service_dot_backend__service__pb2.GetNotesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'backend_service.BackendService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('backend_service.BackendService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class BackendService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetNotes(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/backend_service.BackendService/GetNotes',
            backend__service_dot_backend__service__pb2.GetNotesRequest.SerializeToString,
            backend__service_dot_backend__service__pb2.GetNotesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
