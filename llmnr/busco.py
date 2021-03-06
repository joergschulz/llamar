#! /usr/bin/env python3
# Copyright© 2014 by Marc Culler and others.
#
# This file is part of LLamar.
#
# LLamar is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# LLamar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LLamar.  If not, see <http://www.gnu.org/licenses/>.
#
# References:
# https://tools.ietf.org/html/rfc4795
# http://msdn.microsoft.com/en-us/library/dd240328.aspx
from argparse import ArgumentParser
from . import Sender
parser = ArgumentParser(description="""
Run LLMNR queries of type A, AAAA, PTR or ANY
and print the results.  The default type is A.
""")
parser.add_argument('name_or_address')
parser.add_argument(
    '-q', '--qtype', choices=['A', 'AAAA', 'PTR', 'ANY'], default='A',
    help='the query type (default is A)')
parser.add_argument(
    '-6', '--useIPv6',
    help='use IPv6 instead of IPv4.',
    action='store_true')
parser.add_argument(
    '-i', '--interface',
    help='specify a network interface. E.g. -i eth1')
parser.add_argument(
    '-a', '--address',
    help='send the query to ADDRESS by unicast TCP')
 
def main():
    args = parser.parse_args()
    family = 'inet6' if args.useIPv6 else 'inet'
    iface = args.interface
    s = Sender(iface, family)
    qtype = args.qtype if args.qtype != 'ANY' else '*'
    answers = s.ask(args.name_or_address, qtype, args.address)
    if not answers:
        print('No response.')
    else:
        for qtype, answer, server in answers:
            print('%s: %s'%(qtype, answer))

if __name__ == '__main__':
    main()

#Local Variables:
#coding: utf-8
#mode: python
#End:
