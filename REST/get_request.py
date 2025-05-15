from ssl import SSLError, SSLCertVerificationError

import requests


class Client(object):
    def __init__(self, url: str, ssl_verify=True, cert_path=None):
        self.url = url
        if cert_path:
            self.ssl_verify = cert_path
        else:
            self.ssl_verify = ssl_verify

    def get(self) -> str:
        return str(requests.get(self.url,verify=self.ssl_verify).content)


if __name__ == '__main__':
    print("Client with Verification Enabled and not passing cert")
    client_verify = Client('https://self-signed.badssl.com')
    try:
        print(client_verify.get())
    except Exception as e:
        print("Caught exception", e)
        print("\n")

    print("Client with Verification Enabled and passing cert")
    client_verify_cert = Client('https://self-signed.badssl.com', cert_path=str("badssl-com.pem"))
    print(client_verify_cert.get())
