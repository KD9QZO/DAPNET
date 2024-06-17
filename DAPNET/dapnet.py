import os
import sys

import requests
from requests.auth import HTTPBasicAuth
import json
import logging
import pprint


###############################################################################
# Funktionen definieren
###############################################################################

def send(text, callsign, login, passwd, url, txgroup="us-all"): # mit json modul machen
    """
    Sendet JASON-String zur Funkruf senden
    """

    json_string = json.dumps({"text": text, "callSignNames": callsign, "transmitterGroupNames": [txgroup], "emergency": False})

    pprint.pprint(json_string)

    response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling einbauen

    return response.status_code


def single_callsign(callsign_list): #  Rufzeichen vereinzelt und ruft mit jedem Rufzeichen die Send Funktion auf.
    """
    Zerlegt die callsign_list in einzelne callsign
    """
    for callsign in callsign_list:
        send(text, callsign, login, passwd, url)
    return


class DAPNET():
    def __init__(self, loglevel=logging.NONE):
        """
        Initializes the DAPNET class.

        :param loglevel: Set the log level to use
        """
        self.dapnet_auth = None
        self.dapnet_pass = None
        self.dapnet_user = None
        self.dapnet_dest_callsign = None
        self.dapnet_logging_level = loglevel
        self.dapnet_emergency = False
        self.dapnet_url = 'http://www.hampager.de:8080/calls'
        self.dapnet_txgroup = "us-all"
        logging.basicConfig(level=self.dapnet_logging_level, format="%(asctime)s;%(levelname)s;%(message)s")
        logger = logging.getLogger(sys.argv[0])

    def set_credentials(self, user: str, passwd: str):
        """
        Set the DAPNET credentials

        :param user: The usename used to log into the DAPNET server
        :param passwd: The password used to access the DAPNET API
        :return: The DAPNET credentials, as an HTTPBasicAuth object
        """
        self.dapnet_user = user
        self.dapnet_pass = passwd
        self.dapnet_auth = HTTPBasicAuth(self.dapnet_user, self.dapnet_pass)

        return self.dapnet_auth

    def set_credentials_from_env(self):
        self.dapnet_user = os.getenv('DAPNET_USERNAME')
        self.dapnet_pass = os.getenv('DAPNET_PASSWORD')
        self.dapnet_auth = HTTPBasicAuth(self.dapnet_user, self.dapnet_pass)

        return self.dapnet_auth

    def set_tx_group(self, txgroup: str):
        self.dapnet_txgroup = txgroup

    def set_tx_group_from_env(self):
        self.dapnet_txgroup = os.getenv('DAPNET_TXGROUP')

    def set_destination_callsign(self, callsign):
        self.dapnet_dest_callsign = callsign

    def set_emergency_flag(self, is_emergency: bool):
        self.dapnet_emergency = is_emergency

    def send_page(self, callsign: str, contents: str):
        """
        Send a single page over the DAPNET network, using the HTTP API

        :param callsign: The callsign that should receive the page
        :param contents: The contents of the page
        :return: The response from the DAPNET API
        """
        self.dapnet_dest_callsign = callsign
        json_string = json.dumps(
            {
                "text": contents,
                "callSignNames": self.dapnet_dest_callsign,
                "transmitterGroupNames": [
                    self.dapnet_txgroup
                ],
                "emergency": self.dapnet_emergency
            }
        )
        pprint.pprint(json_string)

        response = requests.post(self.dapnet_url, data=json_string, auth=self.dapnet_auth)  # Exception handling einbauen

        return response.status_code

    def send_multiple_pages(self, callsign_list, contents: str):
        for cs in callsign_list:
            self.send_page(cs, contents)
