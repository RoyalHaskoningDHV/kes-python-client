
from dataclasses import dataclass
from functools import cached_property
from typing import Collection
from uuid import UUID

import grpc
from kes.table import RowType, Table, TableDef
from kes.proto.project_pb2 import ReadActivitiesReply, ReadActivitiesRequest
from kes.proto.project_pb2_grpc import ProjectStub
from kes.proto.table_pb2_grpc import TableStub

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
    _table_stub: TableStub
    _project_stub: ProjectStub

    def __init__(self, project_id: UUID, table_stub: TableStub, project_stub: ProjectStub):
        self._project_id = project_id
        self._table_stub = table_stub
        self._project_stub = project_stub
        self._inspections = None

    @cached_property
    def activities(self) -> Collection[Activity]:
        request = ReadActivitiesRequest(projectId=str(self._project_id))
        reply: ReadActivitiesReply = self._project_stub.readActivities(request)

        activities: Collection[Activity] = []
        for pb_activity in reply.activities:
            activity = Activity(self._table_stub, UUID(pb_activity.id), pb_activity.description)
            activities.append(activity)

        return activities
