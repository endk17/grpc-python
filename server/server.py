from concurrent import futures
import logging

import grpc
import demo_pb2
import demo_pb2_grpc


class Greeter(demo_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        return demo_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
        return demo_pb2.HelloReply(message='Hello again, %s!' % request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    demo_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
