import hashlib

from transaction import Transaction
from random import randint
from mining import Block
from mempool import Mempool
from validate import validate_seed_transaction, validate_transaction

BLOCK_SIZE = 10


def test_blockchain():
    # Generate transactions and add to mempool
    pub_key = 'sample_public_key'

    print('Generating seed transaction...')
    seed_tx = Transaction('', pub_key, 100)
    mempool = Mempool()
    mempool.add(seed_tx)
    tx = seed_tx
    print('Validating seed transaction')
    print(f'Is seed transaction valid?: {validate_seed_transaction(seed_tx)}')

    print('Seed transaction added to mempool')

    print('Generating other transactions...')
    for i in range(0, 100):
        new_tx = Transaction(tx.body['output'], pub_key, randint(0,10))
        tx_id = new_tx.header['tx_id']
        print(f'Validating transaction {tx_id}')
        valid = validate_transaction(new_tx)
        if valid:
            print(f'Transaction with tx_id {tx_id} is valid and has been added to mempool!')
            mempool.add(new_tx)
        else:
            print(f'Transaction is invalid - discarded')
        tx = new_tx

    print('Finished generating transactions')
    count = str(len(mempool.mempool))
    print(f'{count} items in mempool')

    # Construct genesis block
    genesis = Block('00000000')
    genesis.add_tx(seed_tx)
    tx = seed_tx
    while len(genesis.body) < BLOCK_SIZE and len(mempool.mempool) > 0:
        #print('1')
        #print(str(genesis.body))
        if tx.header['tx_id'] in mempool.mempool:
            genesis.add_tx(tx)
            mempool.remove(tx)
        for key in mempool.mempool:
            #print('2')
            output = tx.output
            print(str(mempool.mempool[key].body['output']))
            print(output)
            if mempool.mempool[key].body['output'] == output:
                #print('3')
                tx = mempool.mempool[key]
                break

    block = genesis
    print('Validating genesis block...')
    is_valid = block.is_valid_block()
    print(f'Is block valid? {is_valid}')
    blockchain = [genesis]

    # Mine!
    while len(mempool.mempool) > 0:
        m = hashlib.sha256()
        m.update(block.header)
        new_block = Block(m.digest())
        tx_id = list(mempool.mempool.keys())[0]
        while len(new_block.body) < BLOCK_SIZE:
            if tx_id in mempool:
                new_block.add_tx(mempool.mempool[tx_id])
                mempool.remove(mempool.mempool[tx_id])
            # pick next tx
            for key in mempool.mempool:
                output = tx.output
                if mempool.mempool[key].body['output'] == output:
                    tx = mempool.mempool[key]
                    break
        if new_block.is_valid_block():
            print(f'Block is valid - appending')
            blockchain.append(new_block)
        block = new_block

    print("Finished generating blockchain - print")
    for entry in blockchain:
        print(f'Valid block with header {str(entry.header)}')

    print('Finished!')


if __name__ == "__main__":
    test_blockchain()