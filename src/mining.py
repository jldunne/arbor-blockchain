from validate import validate_transaction, validate_seed_transaction


class Block:
    def __init__(self, header):
        self.header = header
        self.nonce = ''
        self.body = []

    def add_nonce(self, nonce):
        self.nonce = nonce

    def add_header(self, header):
        self.header = header

    def add_tx(self, tx):
        self.body.append(tx)

    def is_valid_block(self):
        if not self.header:
            return False
        if not self.body:
            return False
        # todo: add validation for seed and normal tx
        return True
