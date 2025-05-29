from web3.utils.address import to_checksum_address
from pprint import pprint as pp

SRC_PATH  = './rocketship/{}'
DEST_PATH = './rocketship/out/{}.csv'

config = [
    {
        'title': 'eco',
        'csv': [
            'Rocketship Eco OP.csv',
            'Rocketship Eco Zora.csv',
            'Rocketship Eco Mode.csv',
            'Rocketship Eco Arb.csv',
            'Rocketship Eco Nova.csv',
            'Rocketship Eco Metis.csv',
        ],
    },
    {
        'title': 'biz',
        'csv': [
            'Rocketship Biz OP.csv',
            'Rocketship Biz Zora.csv',
            'Rocketship Biz Mode.csv',
            'Rocketship Biz Arb.csv',
            'Rocketship Biz Nova.csv',
            'Rocketship Biz Metis.csv',
        ],
    },
    {
        'title': 'first',
        'csv': [
            'Rocketship First.csv',
        ],
    },
]

for cfg in config:
    chunk = {}
    for src in cfg['csv']:
        src = SRC_PATH.format(src)
        #print('>', src)

        with open(src, 'r') as file:
            for line in file:
                [ addr, qty ] = line.strip().split(',')
                addr = addr.lower()
                qty = int(qty)
                #print(addr, qty)
                chunk[addr] = chunk.get(addr, 0) + qty

    # sort by qty, addr
    chunk = sorted(list(chunk.items()), key=lambda x: (-x[1], x[0]))

    # write output
    dest = DEST_PATH.format(cfg['title'])
    sum_qty = 0
    with open(dest, "w") as f:
        for (addr, qty) in chunk:
            addr = to_checksum_address(addr)
            f.write(f"{addr},{qty}\n")
            sum_qty += qty
    print(dest, len(chunk), sum_qty)

    #print('<', dest)
    #pp(chunk)
