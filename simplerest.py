#!/usr/bin/env python3
import json
import sys
import requests
import os

from argparse import ArgumentParser
from pprint import pprint


def get_message(json_results, options):
    if 'vendorDetails' not in json_results:
        return 'Error: Something failed. Use --env="DEBUG=true" for more info!'

    company_details = json_results['vendorDetails']

    if options.verbose or options.debug:
        print(json.dumps(company_details, indent=4, sort_keys=True))

    company_name = company_details['companyName']

    if options.output == 'text':
        return "Company: %s" % company_name
    if options.output == 'json':
        company_obj = {}
        company_obj['Company'] = company_name
        return json.dumps(company_obj)


def main():
    parser = ArgumentParser(description="MacAddress API - Get Company")
    parser.add_argument("--token",
                        help="Must provide token",
                        required=True)
    parser.add_argument("--endpoint",
                        help="Must provide endpoint",
                        required=True)
    parser.add_argument("--macaddress",
                        help="Must provide macaddress",
                        required=True)
    parser.add_argument('--output',
                        choices=['text', 'json'],
                        default='text',
                        help="Ouput format: json or text"
                        )
    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        default=False,
                        help="More info than you want"
                        )
    parser.add_argument('--debug', '-d',
                        action='store_true',
                        default=False,
                        help='More info than is useful'
                        )
    options = parser.parse_args()

    urlrequest = "%s?output=json&search=%s" % (
        options.endpoint, options.macaddress)

    if options.verbose or options.debug:
        print("Endpoint: " + options.endpoint, file=sys.stderr)
        print("Request: " + urlrequest, file=sys.stderr)

    r = requests.get(
        urlrequest,
        headers={'X-Authentication-Token': options.token}
    )

    if options.verbose or options.debug:
        print("HTTP{}".format(r.status_code))
        print(r.text, file=sys.stderr)

    json_results = r.json()

    message = get_message(json_results, options)

    print(message)


if __name__ == '__main__':
    main()
