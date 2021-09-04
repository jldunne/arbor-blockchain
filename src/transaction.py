from hashlib import blake2b


class Transaction:

    def __init__(self, inpt, public_key, arb_value):
        # input is the value of a previous transaction object
        # needs to be populated after tx instantiated
        self.input = inpt
        # todo: output should be signed
        self.output = {'pub_key': public_key, 'arb': arb_value}

        self.body = {'input': self.input, 'output': self.output}
        h = blake2b()
        h.update(str(self.body).encode())

        self.header = {'tx_id': h.hexdigest()}
