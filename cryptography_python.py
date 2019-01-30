from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64 # to produce human readable encoding of the binary bytes

for _hash in [hashes.SHA1, hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512]:
    digest = hashes.Hash(_hash(), backend=default_backend())
    digest.update(b"Cryptography 2019")
    # digest.update(b"2019")
    msg_digest = digest.finalize()
    # Notice the output size of the digest
    print(_hash.name, len(msg_digest), len(msg_digest) * 8, base64.b64encode(msg_digest))