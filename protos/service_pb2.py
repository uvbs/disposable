# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import errors_pb2 as protos_dot_errors__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/service.proto',
  package='disposable',
  syntax='proto3',
  serialized_pb=_b('\n\x14protos/service.proto\x12\ndisposable\x1a\x13protos/errors.proto\"\"\n\x11\x44isposableRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"Z\n\x12\x44isposableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x12\x12\n\nrequest_id\x18\x02 \x01(\t\x12 \n\x05\x65rror\x18\x03 \x01(\x0b\x32\x11.disposable.Error2^\n\x11\x44isposableService\x12I\n\x06Verify\x12\x1d.disposable.DisposableRequest\x1a\x1e.disposable.DisposableResponse\"\x00\x42\x35\n\x1a\x30x19.github.com.disposableZ\ndisposable\xa2\x02\nDisposableb\x06proto3')
  ,
  dependencies=[protos_dot_errors__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DISPOSABLEREQUEST = _descriptor.Descriptor(
  name='DisposableRequest',
  full_name='disposable.DisposableRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='email', full_name='disposable.DisposableRequest.email', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=91,
)


_DISPOSABLERESPONSE = _descriptor.Descriptor(
  name='DisposableResponse',
  full_name='disposable.DisposableResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='disposable.DisposableResponse.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='disposable.DisposableResponse.request_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='disposable.DisposableResponse.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=183,
)

_DISPOSABLERESPONSE.fields_by_name['error'].message_type = protos_dot_errors__pb2._ERROR
DESCRIPTOR.message_types_by_name['DisposableRequest'] = _DISPOSABLEREQUEST
DESCRIPTOR.message_types_by_name['DisposableResponse'] = _DISPOSABLERESPONSE

DisposableRequest = _reflection.GeneratedProtocolMessageType('DisposableRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISPOSABLEREQUEST,
  __module__ = 'protos.service_pb2'
  # @@protoc_insertion_point(class_scope:disposable.DisposableRequest)
  ))
_sym_db.RegisterMessage(DisposableRequest)

DisposableResponse = _reflection.GeneratedProtocolMessageType('DisposableResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISPOSABLERESPONSE,
  __module__ = 'protos.service_pb2'
  # @@protoc_insertion_point(class_scope:disposable.DisposableResponse)
  ))
_sym_db.RegisterMessage(DisposableResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\0320x19.github.com.disposableZ\ndisposable\242\002\nDisposable'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class DisposableServiceStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Verify = channel.unary_unary(
        '/disposable.DisposableService/Verify',
        request_serializer=DisposableRequest.SerializeToString,
        response_deserializer=DisposableResponse.FromString,
        )


class DisposableServiceServicer(object):

  def Verify(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DisposableServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Verify': grpc.unary_unary_rpc_method_handler(
          servicer.Verify,
          request_deserializer=DisposableRequest.FromString,
          response_serializer=DisposableResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'disposable.DisposableService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaDisposableServiceServicer(object):
  def Verify(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaDisposableServiceStub(object):
  def Verify(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  Verify.future = None


def beta_create_DisposableService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('disposable.DisposableService', 'Verify'): DisposableRequest.FromString,
  }
  response_serializers = {
    ('disposable.DisposableService', 'Verify'): DisposableResponse.SerializeToString,
  }
  method_implementations = {
    ('disposable.DisposableService', 'Verify'): face_utilities.unary_unary_inline(servicer.Verify),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_DisposableService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('disposable.DisposableService', 'Verify'): DisposableRequest.SerializeToString,
  }
  response_deserializers = {
    ('disposable.DisposableService', 'Verify'): DisposableResponse.FromString,
  }
  cardinalities = {
    'Verify': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'disposable.DisposableService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
