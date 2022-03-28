""" Client module.

This module is the starting point for wrting a KES Python script.
Scripts typically start by configuring and creating a client instance, after which the client can be used to open projects.

    Typical usage example:

    config = Config(kes_service_address='localhost:50051')
    client = Client(config)
    project = client.openProject("Preview Python client example")
"""

from dataclasses import dataclass
from uuid import UUID

import grpc

from kes.proto.table_pb2_grpc import TableStub

from kes.proto.project_pb2_grpc import ProjectStub

from kes.project import Project
from kes.proto.project_pb2 import LookupProjectRequest


class ProjectNotFound(Exception):
    """ Exception indicating when a project could not be found."""
    ...


@dataclass
class Config:
    """Holds configuration of the client.

    Attributes:
        kes_service_address:
            Address of the service which interacts with the Kes database.
            Example: 'https://kes-table-service-pr-staging.bluebush-b51cfb01.westeurope.azurecontainerapps.io:50051'

    """
    kes_service_address: str


class Client:
    """Kes client.

    Starting point of a kes script. After creating a client instance, kes projects can be opened using open_project.
    """

    _channel: grpc.Channel
    _table_stub: TableStub
    _project_stub: ProjectStub

    def __init__(self, config: Config):
        """Constructs a client.

        Args:
            config (Config): The client configuration
        """
        self._channel = grpc.insecure_channel(config.kes_service_address)
        self._table_stub = TableStub(self._channel)
        self._project_stub = ProjectStub(self._channel)

        """Open a Kes project

        Opens a Kes project by name.

        Args:
            project_name (str): Name of the project to open.

        Returns:
            An instance representing the requested Kes project.

        Raises:
            ProjectNotFound: The requested project could not be found.
        """

    def open_project(self, project_name: str) -> Project:
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
