import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/lab.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

from src.network_device import NetworkDevice
from src.parser_utils import parse_csv, parse_json, parse_xml, parse_yaml

def main():
    dev_data = parse_json("data/devices.json")
    int_data = parse_yaml("data/interfaces.yaml")
    inv_data = parse_csv("data/inventory.csv")
    vlan_data = parse_xml("data/vlans.xml")

    for dev in dev_data:
        device = NetworkDevice(hostname=dev.get("hostname"), ip=dev.get("ip"), type=dev.get("type"))
        device.summarize()

    for intf in int_data:
        msg = f"Interface {intf.get('name')} is {intf.get('status')}"
        print(msg)
        logging.info(f"[INTERFACE_MSG]: {msg}")

    for inv in inv_data:
        msg = f"Device {inv.get('hostname')} is a {inv.get('location')} {inv.get('role')}"
        print(msg)
        logging.info(f"[DEVICE_MSG]: {msg}")

    for vlan in vlan_data:
        msg = f"VLAN {vlan.get('id')} is the {vlan.get('name')}"
        print(msg)
        logging.info(f"[VLAN_MSG]: {msg}")

if __name__ == "__main__":
    logging.info("[LAB1-START]")
    main()
    logging.info("[LAB1-END]")