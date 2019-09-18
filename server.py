from threading import Thread
import time
from console_tr import consol_tr
from log import log
ак
from ml_control import ml_control
from data_exchange import data_exchange_tr

ftp_ip = "153.156.155.120"

class main_hab():
    main_objects = []
    max_tread = 2

    def __init__(self):
        self.log = log(ftp_ip)

main_hab = main_hab()
consol_tr = consol_tr(main_hab)
data_exchange_tr = data_exchange_tr(main_hab)

consol_tr.start()
data_exchange_tr.start()
