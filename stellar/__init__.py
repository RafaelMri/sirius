# -*- coding: utf-8 -*-

from .keys import random_keypair, account_from_secret
from .api import setup_test_network, setup_public_network, setup_custom_network, get_current_network
from .api import account, transaction, ledger, operation
from .api import transactions, ledgers, effects, operations, payments
from .api import find_payment_path, assets, trades, orderbook
from .api import new_transaction


import logging
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
