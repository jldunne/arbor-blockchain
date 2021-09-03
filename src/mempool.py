class Mempool:
    def __init__(self):
        self.mempool = {}

    def add(self, tx):
        self.mempool[tx.header['tx_id']] = tx

    def remove(self, tx):
        del self.mempool[tx.header['tx_id']]
