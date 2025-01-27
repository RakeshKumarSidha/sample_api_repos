from genie.parsergen import oper
from pyats.topology import Device

def get_interface_status(device: Device, interface: str) -> str:
    """
    Retrieves the status (up/down) of the specified network interface on the device.

    Args:
    - device (Device): The pyATS device object representing the network device.
    - interface (str): The name of the network interface to check, e.g., 'GigabitEthernet0/1'.

    Returns:
    - str: The status of the interface, such as 'up' or 'down'.

    Raises:
    - ValueError: If the interface is not found on the device.
    """
    output = device.parse('show interface {0}'.format(interface))
    
    # Check if the interface exists in the output
    if interface not in output:
        raise ValueError(f"Interface {interface} not found on device.")
    
    # Get the line protocol status (up/down)
    return output[interface].get('line_protocol', 'unknown')
