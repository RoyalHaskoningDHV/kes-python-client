# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproject.proto\x12\x03kes\"\x15\n\x13ListProjectsRequest\"3\n\x11ListProjectsReply\x12\x1e\n\x08projects\x18\x01 \x03(\x0b\x32\x0c.kes.Project\"/\n\x14LookupProjectRequest\x12\x17\n\x0fmasterProjectId\x18\x01 \x01(\t\"4\n\x12LookupProjectReply\x12\x1e\n\x08projects\x18\x01 \x03(\x0b\x32\x0c.kes.Project\"*\n\x15ReadActivitiesRequest\x12\x11\n\tprojectId\x18\x01 \x01(\t\"8\n\x13ReadActivitiesReply\x12!\n\nactivities\x18\x01 \x03(\x0b\x32\r.kes.Activity\"C\n\x08\x41\x63tivity\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x16\n\x0etableLibraryId\x18\x03 \x01(\t\"S\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x15\n\rprojectNumber\x18\x03 \x01(\t\x12\x17\n\x0fmasterProjectId\x18\x04 \x01(\t\"+\n\x15\x44ownloadReportRequest\x12\x12\n\nactivityId\x18\x01 \x01(\t\"$\n\x13\x44ownloadReportReply\x12\r\n\x05\x63hunk\x18\x01 \x01(\x0c\x32\xb0\x02\n\rProjectDetail\x12\x42\n\x0clistProjects\x12\x18.kes.ListProjectsRequest\x1a\x16.kes.ListProjectsReply\"\x00\x12\x45\n\rlookupProject\x12\x19.kes.LookupProjectRequest\x1a\x17.kes.LookupProjectReply\"\x00\x12H\n\x0ereadActivities\x12\x1a.kes.ReadActivitiesRequest\x1a\x18.kes.ReadActivitiesReply\"\x00\x12J\n\x0e\x64ownloadReport\x12\x1a.kes.DownloadReportRequest\x1a\x18.kes.DownloadReportReply\"\x00\x30\x01\x42\x0bZ\tkes/protob\x06proto3')



_LISTPROJECTSREQUEST = DESCRIPTOR.message_types_by_name['ListProjectsRequest']
_LISTPROJECTSREPLY = DESCRIPTOR.message_types_by_name['ListProjectsReply']
_LOOKUPPROJECTREQUEST = DESCRIPTOR.message_types_by_name['LookupProjectRequest']
_LOOKUPPROJECTREPLY = DESCRIPTOR.message_types_by_name['LookupProjectReply']
_READACTIVITIESREQUEST = DESCRIPTOR.message_types_by_name['ReadActivitiesRequest']
_READACTIVITIESREPLY = DESCRIPTOR.message_types_by_name['ReadActivitiesReply']
_ACTIVITY = DESCRIPTOR.message_types_by_name['Activity']
_PROJECT = DESCRIPTOR.message_types_by_name['Project']
_DOWNLOADREPORTREQUEST = DESCRIPTOR.message_types_by_name['DownloadReportRequest']
_DOWNLOADREPORTREPLY = DESCRIPTOR.message_types_by_name['DownloadReportReply']
ListProjectsRequest = _reflection.GeneratedProtocolMessageType('ListProjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.ListProjectsRequest)
  })
_sym_db.RegisterMessage(ListProjectsRequest)

ListProjectsReply = _reflection.GeneratedProtocolMessageType('ListProjectsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTSREPLY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.ListProjectsReply)
  })
_sym_db.RegisterMessage(ListProjectsReply)

LookupProjectRequest = _reflection.GeneratedProtocolMessageType('LookupProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.LookupProjectRequest)
  })
_sym_db.RegisterMessage(LookupProjectRequest)

LookupProjectReply = _reflection.GeneratedProtocolMessageType('LookupProjectReply', (_message.Message,), {
  'DESCRIPTOR' : _LOOKUPPROJECTREPLY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.LookupProjectReply)
  })
_sym_db.RegisterMessage(LookupProjectReply)

ReadActivitiesRequest = _reflection.GeneratedProtocolMessageType('ReadActivitiesRequest', (_message.Message,), {
  'DESCRIPTOR' : _READACTIVITIESREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.ReadActivitiesRequest)
  })
_sym_db.RegisterMessage(ReadActivitiesRequest)

ReadActivitiesReply = _reflection.GeneratedProtocolMessageType('ReadActivitiesReply', (_message.Message,), {
  'DESCRIPTOR' : _READACTIVITIESREPLY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.ReadActivitiesReply)
  })
_sym_db.RegisterMessage(ReadActivitiesReply)

Activity = _reflection.GeneratedProtocolMessageType('Activity', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.Activity)
  })
_sym_db.RegisterMessage(Activity)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.Project)
  })
_sym_db.RegisterMessage(Project)

DownloadReportRequest = _reflection.GeneratedProtocolMessageType('DownloadReportRequest', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREPORTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.DownloadReportRequest)
  })
_sym_db.RegisterMessage(DownloadReportRequest)

DownloadReportReply = _reflection.GeneratedProtocolMessageType('DownloadReportReply', (_message.Message,), {
  'DESCRIPTOR' : _DOWNLOADREPORTREPLY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:kes.DownloadReportReply)
  })
_sym_db.RegisterMessage(DownloadReportReply)

_PROJECTDETAIL = DESCRIPTOR.services_by_name['ProjectDetail']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\tkes/proto'
  _LISTPROJECTSREQUEST._serialized_start=22
  _LISTPROJECTSREQUEST._serialized_end=43
  _LISTPROJECTSREPLY._serialized_start=45
  _LISTPROJECTSREPLY._serialized_end=96
  _LOOKUPPROJECTREQUEST._serialized_start=98
  _LOOKUPPROJECTREQUEST._serialized_end=145
  _LOOKUPPROJECTREPLY._serialized_start=147
  _LOOKUPPROJECTREPLY._serialized_end=199
  _READACTIVITIESREQUEST._serialized_start=201
  _READACTIVITIESREQUEST._serialized_end=243
  _READACTIVITIESREPLY._serialized_start=245
  _READACTIVITIESREPLY._serialized_end=301
  _ACTIVITY._serialized_start=303
  _ACTIVITY._serialized_end=370
  _PROJECT._serialized_start=372
  _PROJECT._serialized_end=455
  _DOWNLOADREPORTREQUEST._serialized_start=457
  _DOWNLOADREPORTREQUEST._serialized_end=500
  _DOWNLOADREPORTREPLY._serialized_start=502
  _DOWNLOADREPORTREPLY._serialized_end=538
  _PROJECTDETAIL._serialized_start=541
  _PROJECTDETAIL._serialized_end=845
# @@protoc_insertion_point(module_scope)
