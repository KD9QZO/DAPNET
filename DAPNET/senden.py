#!/usr/bin/env python3

################################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
import dapnet
import logging # -> Logging vom Fehlermeldenung
import sys


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])


###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

login = os.getenv('DAPNET_username')       #  DAPNET Benutzername aus Umgebungsvariablen in Pysharm os.getenv oder config datei yaml / json
passwd = os.getenv('DAPNET_password')      #  DAPNET Passwort aus Umgebungsvariablen config.py
login2 = os.getenv('DAPNET_USERNAME')
passwd2 = os.getenv('DAPNET_PASSWORD')


url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

#text = "test test GPN"  #  Nachrichte ntext bis 80 Zeichen  eingeben

text = sys.argv[1]

callsign_list = ["kd9qzo"]  # eins oder mehrere Emfaenger Rufzeichen

txgroup = "us-il"           #  Sendergruppe zB. DL-all für alle Sender in Deutschland
txgroup2 = os.getenv('DAPNET_TXGROUP')


##############################################################################
# Hauptprogramm
##############################################################################


dapnet.send(text, callsign_list, login2, passwd2, url, txgroup2)
