from threading import Thread
import time
from console_tr import consol_tr
from log import log
from ml_control import ml_control




# main_fun = {"ml_control":ml_control(),
#             "log":log(),
#             "consol_tr":consol_tr(),
#             "main_tr": main_tr(),
#             }
# l

ftp_ip = "153.156.155.120"
class Main_tread(Thread):
    main_objects = {}
    val = 0

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(3)





main_tr = Main_tread()
main_tr.start()

log = log(ftp_ip)
consol_tr = consol_tr(main_tr, log)
consol_tr.start()
