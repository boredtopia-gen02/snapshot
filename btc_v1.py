import json
from web3.utils.address import to_checksum_address
from pprint import pprint as pp

JSON_PATH   = "./btc_v1/{}.json"
CSV_PATH    = "./btc_v1/out/{}.csv"
FROM_ID     = 1
TO_ID       = 5

# statistic
stat_total = 0

for id in range(FROM_ID, TO_ID+1):
    path = JSON_PATH.format(id)
    rows = {}
    with open(path, 'r') as file:
        data = json.load(file)
        for owner in data['items']:
            addr = owner['address']['hash'].lower()
            qty = int(owner['value'])
            rows[addr] = qty
            # update stat
            stat_total += qty

        # sort by qty, addr
        rows = sorted(list(rows.items()), key=lambda x: (-x[1], x[0]))
        #pp(rows)

        # write output
        dest = CSV_PATH.format(id)
        with open(dest, "w") as f:
            for (addr, qty) in rows:
                addr = to_checksum_address(addr)
                f.write(f"{addr},{qty}\n")
        print(dest, len(rows))

#print(stat_total) #107
