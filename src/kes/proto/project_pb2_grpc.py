# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from .import project_pb2 as project__pb2


class ProjectDetailStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listProjects = channel.unary_unary(
                '/kes.ProjectDetail/listProjects',
                request_serializer=project__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=project__pb2.ListProjectsReply.FromString,
                )
        self.lookupProject = channel.unary_unary(
                '/kes.ProjectDetail/lookupProject',
                request_serializer=project__pb2.LookupProjectRequest.SerializeToString,
                response_deserializer=project__pb2.LookupProjectReply.FromString,
                )
        self.readActivities = channel.unary_unary(
                '/kes.ProjectDetail/readActivities',
                request_serializer=project__pb2.ReadActivitiesRequest.SerializeToString,
                response_deserializer=project__pb2.ReadActivitiesReply.FromString,
                )
        self.downloadReport = channel.unary_stream(
                '/kes.ProjectDetail/downloadReport',
                request_serializer=project__pb2.DownloadReportRequest.SerializeToString,
                response_deserializer=project__pb2.DownloadReportReply.FromString,
                )


class ProjectDetailServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listProjects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def lookupProject(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readActivities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def downloadReport(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectDetailServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listProjects': grpc.unary_unary_rpc_method_handler(
                    servicer.listProjects,
                    request_deserializer=project__pb2.ListProjectsRequest.FromString,
                    response_serializer=project__pb2.ListProjectsReply.SerializeToString,
            ),
            'lookupProject': grpc.unary_unary_rpc_method_handler(
                    servicer.lookupProject,
                    request_deserializer=project__pb2.LookupProjectRequest.FromString,
                    response_serializer=project__pb2.LookupProjectReply.SerializeToString,
            ),
            'readActivities': grpc.unary_unary_rpc_method_handler(
                    servicer.readActivities,
                    request_deserializer=project__pb2.ReadActivitiesRequest.FromString,
                    response_serializer=project__pb2.ReadActivitiesReply.SerializeToString,
            ),
            'downloadReport': grpc.unary_stream_rpc_method_handler(
                    servicer.downloadReport,
                    request_deserializer=project__pb2.DownloadReportRequest.FromString,
                    response_serializer=project__pb2.DownloadReportReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'kes.ProjectDetail', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectDetail(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kes.ProjectDetail/listProjects',
            project__pb2.ListProjectsRequest.SerializeToString,
            project__pb2.ListProjectsReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def lookupProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kes.ProjectDetail/lookupProject',
            project__pb2.LookupProjectRequest.SerializeToString,
            project__pb2.LookupProjectReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readActivities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/kes.ProjectDetail/readActivities',
            project__pb2.ReadActivitiesRequest.SerializeToString,
            project__pb2.ReadActivitiesReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def downloadReport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/kes.ProjectDetail/downloadReport',
            project__pb2.DownloadReportRequest.SerializeToString,
            project__pb2.DownloadReportReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
