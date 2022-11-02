import dns.name
import dns.message
import socket
import logging

__all__ = ["Resolver"]


class Resolver:
    # https://www.iana.org/domains/root/servers
    ROOT_IPV4 = (
        "198.41.0.4",  # Verisign, Inc.
        "199.9.14.201",  # University of Southern California
        "192.33.4.12",  # Cogent Communications
        "199.7.91.13",  # University of Maryland
        "192.203.230.10",  # NASA (Ames Research Center)
        "192.5.5.241",  # Internet Systems Consortium, Inc.
        "192.112.36.4",  # US Department of Defense (NIC)
        "198.97.190.53",  # US Army (Research Lab)
        "192.36.148.17",  # Netnod
        "192.58.128.30",  # Verisign, Inc.
        "193.0.14.129",  # RIPE NCC
        "199.7.83.42",  # ICANN
        "202.12.27.33",  # WIDE Project
    )

    def __init__(self):
        self.client_socket = dns.query._make_socket(
            af=socket.AF_INET, type=socket.SOCK_DGRAM, source=("localhost", 53)
        )
        self.cache = {}

    def resolve(self, request):
        query = str(request.question[0]).split()[0]
        if query in self.cache:
            logging.warning(";; used cache")
            return self.__form_answer(request, self.cache[query])

        query_msg = dns.message.make_query(
            qname=query, rdtype=dns.rdatatype.A, rdclass=dns.rdataclass.IN
        )

        for root_server in self.ROOT_IPV4:
            response = self.__resolve_helper(query_msg, root_server)

            if response:
                self.cache[query] = response
                return self.__form_answer(request, response)

    def __resolve_helper(self, query, ip_address):
        response = dns.query.udp(q=query, where=ip_address)

        if response:
            if response.answer:
                return response
            elif response.additional:
                for additional in response.additional:
                    if additional.rdtype != dns.rdatatype.A:
                        continue
                    for add in additional:
                        new_response = self.__resolve_helper(query, str(add))
                        if new_response:
                            return new_response
        return response

    def __form_answer(self, query, response):
        answer = query
        answer.answer = response.answer
        answer.flags |= dns.flags.QR | dns.flags.RA
        return answer
