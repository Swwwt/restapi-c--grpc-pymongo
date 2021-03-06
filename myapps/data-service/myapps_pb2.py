# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: myapps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='myapps.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cmyapps.proto\"[\n\x0b\x41pplication\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x0f\n\x07\x63reator\x18\x05 \x01(\t\"k\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x1c\n\x06gender\x18\x04 \x01(\x0e\x32\x0c.User.Gender\"\x1e\n\x06Gender\x12\n\n\x06\x46\x45MALE\x10\x00\x12\x08\n\x04MALE\x10\x01\x32\xbe\x01\n\x0b\x44\x61taService\x12\x31\n\x11\x43reateApplication\x12\x0c.Application\x1a\x0c.Application\"\x00\x12.\n\x0eGetApplication\x12\x0c.Application\x1a\x0c.Application\"\x00\x12\x19\n\x07GetUser\x12\x05.User\x1a\x05.User\"\x00\x12\x31\n\x11\x44\x65leteApplication\x12\x0c.Application\x1a\x0c.Application\"\x00\x62\x06proto3')
)



_USER_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='User.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=186,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_USER_GENDER)


_APPLICATION = _descriptor.Descriptor(
  name='Application',
  full_name='Application',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Application.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='Application.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='Application.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='Application.date', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='Application.creator', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=107,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='User.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='User.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='User.gender', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_GENDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=216,
)

_USER.fields_by_name['gender'].enum_type = _USER_GENDER
_USER_GENDER.containing_type = _USER
DESCRIPTOR.message_types_by_name['Application'] = _APPLICATION
DESCRIPTOR.message_types_by_name['User'] = _USER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Application = _reflection.GeneratedProtocolMessageType('Application', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATION,
  '__module__' : 'myapps_pb2'
  # @@protoc_insertion_point(class_scope:Application)
  })
_sym_db.RegisterMessage(Application)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'myapps_pb2'
  # @@protoc_insertion_point(class_scope:User)
  })
_sym_db.RegisterMessage(User)



_DATASERVICE = _descriptor.ServiceDescriptor(
  name='DataService',
  full_name='DataService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=219,
  serialized_end=409,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateApplication',
    full_name='DataService.CreateApplication',
    index=0,
    containing_service=None,
    input_type=_APPLICATION,
    output_type=_APPLICATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetApplication',
    full_name='DataService.GetApplication',
    index=1,
    containing_service=None,
    input_type=_APPLICATION,
    output_type=_APPLICATION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='DataService.GetUser',
    index=2,
    containing_service=None,
    input_type=_USER,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteApplication',
    full_name='DataService.DeleteApplication',
    index=3,
    containing_service=None,
    input_type=_APPLICATION,
    output_type=_APPLICATION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DATASERVICE)

DESCRIPTOR.services_by_name['DataService'] = _DATASERVICE

# @@protoc_insertion_point(module_scope)
