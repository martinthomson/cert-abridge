

class NullCompressor:
    def __init__(self):
        pass

    def name(self):
        return "Null"

    def compress(self, certList):
        return b"".join(certList)

    def decompress(self, compressed_data):
        return compressed_data


class IntermediateSuppression:
    def __init__(self):
        pass

    def name(self):
        return "Intermediate Suppression"

    def compress(self, certList):
        return certList[0]

    def decompress(self, compressed_data):
        return compressed_data

import zlib
class TLSCertCompression:
    def __init__(self):
        pass

    def name(self):
        return "TLS Cert Compression"

    def compress(self, certList):
        data = b"".join(certList)
        compressed_data = zlib.compress(data, level=9)
        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data


class ICAAndTLS:
    def __init__(self):
        self.tls = TLSCertCompression()
        self.ica = IntermediateSuppression()
        pass

    def name(self):
        return "Intermediate Suppression and TLS Cert Compression"

    def compress(self, certList):
        return self.tls.compress([self.ica.compress(certList)])

    def decompress(self, compressed_data):
        return self.ica.decompress(self.tls.decompress(compressed_data))