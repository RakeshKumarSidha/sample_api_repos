from pyats.topology import Device

def get_routing_table(device: Device) -> dict:
    """
    Retrieves the routing table of the network device.

    Args:
    - device (Device): The pyATS device object representing the network device.

    Returns:
    - dict: The routing table parsed into a dictionary format.
    """
    output = device.parse('show ip route')
    return output
