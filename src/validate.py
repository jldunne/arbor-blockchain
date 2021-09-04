from hashlib import blake2b


def validate_seed_transaction(transaction):
    tx_hash = transaction.header['tx_id']
    body = transaction.body

    h = blake2b()
    h.update(str(body).encode())

    if h.hexdigest() == tx_hash:
        return True
    return False


def validate_transaction(transaction):
    tx_hash = transaction.header['tx_id']
    body = transaction.body

    h = blake2b()
    h.update(str(body).encode())

    if h.hexdigest() != tx_hash:
        return False

    # todo: check public keys and signatures
    # if body['input']['arb'] < body['output']['arb']:
    #    return False
    return True
