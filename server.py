from console_tr import consol_tr
from log_obj import log
from data_exchange_tr import data_exchange_tr


class main_hab():
    main_objects = []
    max_tread = 1

    def __init__(self):
        self.log = log()
        self.console = consol_tr(self)
        self.data_exchange = data_exchange_tr(self)

    def start(self):
        self.console.start()
        self.data_exchange.start()


main_hab = main_hab()
main_hab.start()



# consol_tr = consol_tr(main_hab)
# data_exchange_tr = data_exchange_tr(main_hab)

# consol_tr.start()
# data_exchange_tr.start()
