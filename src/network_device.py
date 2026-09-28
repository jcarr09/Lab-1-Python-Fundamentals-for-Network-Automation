import logging

class NetworkDevice:
    def __init__(self, hostname, ip, type):
        self.hostname = hostname
        self.ip = ip
        self.type = type

    def summarize(self):
        netinfo = f"{self.hostname} ({self.type}) - {self.ip}"
        print(netinfo)
        logging.info(f"[DEVICE_SUMMARY]: {netinfo}")
        return netinfo