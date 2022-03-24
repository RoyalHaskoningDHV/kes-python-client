
from dataclasses import dataclass
from uuid import UUID

import grpc

from kes.proto.table_pb2_grpc import TableStub

from kes.proto.project_pb2_grpc import ProjectStub

from kes.project import Project
from kes.proto.project_pb2 import LookupProjectRequest


class ProjectNotFound(Exception):
    ...


@dataclass
class ClientConfig:
    kes_service_address: str


class Client:
    _channel: grpc.Channel
    _table_stub: TableStub
    _project_stub: ProjectStub

    def __init__(self, config: ClientConfig):
        self._channel = grpc.insecure_channel(config.kes_service_address)
        self._table_stub = TableStub(self._channel)
        self._project_stub = ProjectStub(self._channel)

    def openProject(self, project_name: str) -> Project:
        try:
            request = LookupProjectRequest(projectName=project_name)
            reply = self._project_stub.lookupProject(request)
            projectId = UUID(reply.projectId)
            return Project(projectId, self._table_stub, self._project_stub)
        except grpc.RpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise ProjectNotFound
            else:
                raise
