# HMAC Calculation

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hmac, hashes
import os
import base64

hmc_key = k = os.urandom(16)
hmc = hmac.HMAC(hmc_key, hashes.SHA1(), default_backend())
hmc.update(b"Cryptography2019")
hmc_sig = hmc.finalize()
print (base64.b64encode(hmc_sig))