import base64
from Crypto.Hash import HMAC, SHA256
import json


LENDBOX_API_KEY="0L6C6d27i4V9G2CVZezsvsBe9yjdsxRctqhTi+XikLMby35Ou94DjnIbvTGkovqFczZRyCs6kPpwHs9nxa8FvupibODwMaUvedCOq6XGBh37eOFChip6oMJ3SZ82BQR1kGblwA=="

h = HMAC.new(bytes(LENDBOX_API_KEY, 'utf-8'), digestmod=SHA256)


body = {
    "lbUserId": "2909394",
    "amount": 5964,
    "principal": 5600,
    "interest": 364,
    "partnerRefId": "2488322909394169529916251771757",
    "lbTxId": "24883229093941695299162517",
    "type": "REINVESTMENT",
    "transferDate": "2023-12-31",
    "newEndDate": "2024-04-16"
}

h.update(bytes(json.dumps(body, separators=(',', ':')), 'utf-8'))

calc_header = base64.b64encode(h.digest()).decode()

print("header: ", calc_header)

