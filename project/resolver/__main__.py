import dns.rdatatype
import dns.query
import logging

from .Resolver import Resolver


def main():
    logging.warning(";; Started DNS server on localhost:53")
    resolver = Resolver()

    while True:
        query, _, from_address = dns.query.receive_udp(resolver.client_socket)
        response = resolver.resolve(query)
        dns.query.send_udp(resolver.client_socket, response, from_address)


if __name__ == "__main__":
    main()
