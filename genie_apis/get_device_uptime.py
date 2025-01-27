from pyats.topology import Device

def get_device_uptime(device: Device) -> str:
    """
    Retrieves the uptime of the network device.

    Args:
    - device (Device): The pyATS device object representing the network device.

    Returns:
    - str: The uptime of the device in the format 'dd:hh:mm:ss'.
    """
    output = device.parse('show version')
    uptime = output.get('uptime', 'N/A')
    return uptime
