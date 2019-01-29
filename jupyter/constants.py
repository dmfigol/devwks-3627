import re
CDP_COMMAND = "show cdp neighbors detail"
HOSTS_FILE = "hosts.yml"
TOPOLOGY_FILE = "topology.csv"

DEVICE_USERNAME = "cisco"
DEVICE_PASSWORD = "cisco"
DEVICE_TYPE = "cisco_ios"
# connection timeout in seconds
CONNECTION_TIMEOUT = 80
NETMIKO_GLOBAL_DELAY_FACTOR = 1.5

NORMALIZED_INTERFACES = (
    "FastEthernet",
    "GigabitEthernet",
    "TenGigabitEthernet",
    "FortyGigabitEthernet",
    "Ethernet",
    "Loopback",
    "Serial",
    "Vlan",
    "Tunnel",
    "Portchannel",
    "Management",
)

INTERFACE_NAME_RE = re.compile(
    r"(?P<interface_type>[a-zA-Z\-_ ]*)(?P<interface_num>[\d.\/]*)"
)

NEIGHBOR_SPLIT_RE = re.compile(r"\n\n-{6,}\n")

CDP_NEIGHBOR_RE = re.compile(
    r"^Device ID: (?P<remote_fqdn>\S+).+?"
    r"^Interface: (?P<local_interface>\S+),\s+"
    r"Port ID \(outgoing port\): (?P<remote_interface>\b[\w \-/.]+\b)",
    re.M | re.S,
)
