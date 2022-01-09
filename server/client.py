
from __future__ import print_function

import logging

import grpc
import demo_pb2
import demo_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = demo_pb2_grpc.GreeterStub(channel)
        response1 = stub.SayHello(demo_pb2.HelloRequest(name='you'))
        response2 = stub.SayHelloAgain(demo_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response1.message)
    print("Greeter client received: " + response2.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()