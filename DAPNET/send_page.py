#!/usr/bin/env python3

import os
import sys
import dapnet
import logging


def main():
    page_text = sys.argv[1]

    dn = dapnet.DAPNET(logging.DEBUG)

    dn.set_credentials(os.getenv('DAPNET_USERNAME'), os.getenv('DAPNET_PASSWORD'))
    dn.set_tx_group(os.getenv('DAPNET_TX_GROUP'))
    dn.set_destination_callsign("kd9qzo")
    dn.set_emergency_flag(False)

    print("Sending page...")
    resp = dn.send_page("kd9qzo", page_text)
    print("Got response: %d" % (resp))


if __name__ == "__main__":
    main()
