#!/usr/bin/python

import sys
import socket
import requests
import json
from argparse import ArgumentParser


ipify_json_endpoint = "https://api.ipify.org?format=json"


def get_my_public_ip():
    response = requests.get(ipify_json_endpoint)
    return json.loads(response.text)["ip"]


def resolve_fqdn(fqdn):
    """
    fqdn: Fully Qualified Domain Name of the server
    """
    return socket.gethostbyname(fqdn)


def echo_ip_address(ip_address):
    print("The IP Address is: %s" %(ip_address))
    
    
if __name__ == "__main__":
    args_parser = ArgumentParser()
    args_parser.add_argument("--server", action="store_true")
    args_parser.add_argument("--fqdn", help="FQDN of server")
    args = args_parser.parse_args()

    if args.server:
        if not args.fqdn:
            args_parser.error("The Fully Qualified Domain Name is required")
            sys.eixt(-1)
        ip_address = resolve_fqdn(args.fqdn)
        echo_ip_address(ip_address)
    else:
        ip_address = get_my_public_ip()
        echo_ip_address(ip_address)
