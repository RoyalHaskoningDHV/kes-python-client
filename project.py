
from functools import cached_property
from typing import Collection
from uuid import UUID

import grpc
from kes import RowType, Table, TableDef
from proto.project_pb2 import ReadActivitiesReply, ReadActivitiesRequest
from proto.project_pb2_grpc import ProjectStub
from proto.table_pb2_grpc import TableStub


class Activity:
    _id: UUID
    _description: str
    _stub: TableStub

    def __init__(self, stub: TableStub, id: UUID, description: str):
        self._id = id
        self._stub = stub
        self._description = description

    def build_table(self, tableDef: TableDef[RowType]) -> Table[RowType]:
        return Table[RowType](
            self._stub,
            self._id,
            tableDef.row_type,
            tableDef.asset_type_id,
            tableDef.property_map
        )

    @property
    def id(self):
        return self._id


class Project:
    _project_id: UUID
    _channel: grpc.Channel
    _table_stub: TableStub
    _project_stub: ProjectStub

    def __init__(self, project_id: UUID):
        self._project_id = project_id
        self._channel = grpc.insecure_channel('localhost:50051')
        self._table_stub = TableStub(self._channel)
        self._project_stub = ProjectStub(self._channel)
        self._inspections = None

    @cached_property
    def inspections(self) -> Collection[Activity]:
        request = ReadActivitiesRequest(projectId=str(self._project_id))
        reply: ReadActivitiesReply = self._project_stub.readActivities(request)

        activities: Collection[Activity] = []
        for pb_activity in reply.activities:
            activity = Activity(self._table_stub, UUID(pb_activity.id), pb_activity.description)
            activities.append(activity)

        return activities
