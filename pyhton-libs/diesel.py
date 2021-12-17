import diesel
import argparse


class EchoServer(object):
    """this is an echo server using diesel"""

    def handler(self, remote_addr):
        """for running the echo server"""

    host, port - remote_addr[0], remote_addr[1]
    print("Echo client connected from: %s: %d" % (host, port))


while True:
    try:
        message = diesel.until_eol()
        your_message = ":".join(["You said", "message"])
        diesel.send(your_message)
    except Exception as e:
        print("Exception:", e)

        def main(server_port):
            app = diesel.Application()
            server = EchoServer()
            app.add_service(diesel.Service(server.handler, server_port))
            app.run()
            if _name_ == "main_":
                parser = argparse.ArgumentParser(
                    description="Echo Server example with diesel"
                )
            parser.add.argument(
                "--port", action - "store", dest - "port", type=int, required=True
            )
            given_args = parser.parse_args()
            port = given_args.port


main(port)
