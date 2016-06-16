from sys import argv, exit
from grpc.beta import implementations
from helloclient.protos.hello_pb2 import \
    beta_create_Greeter_stub, HelloRequest

TIMEOUT_SECS = 120
DEFAULT_NAME = "world"


def say_hello(host, port, name, timeout=TIMEOUT_SECS):
    channel = implementations.insecure_channel(host, port)
    client = beta_create_Greeter_stub(channel)
    req = HelloRequest(name=name)
    return client.SayHello(req, timeout).message


if __name__ == '__main__':
    if len(argv) < 3:
        print("arguments: host port [name]")
        exit(1)

    host = argv[1]
    port = int(argv[2])
    try:
        name = argv[3]
    except IndexError:
        name = DEFAULT_NAME

    print("saying hello...")
    response = say_hello(host, port, name)
    print("response: {}".format(response))