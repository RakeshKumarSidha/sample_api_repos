from pyats.topology import Device
import subprocess

def check_interface_status(device: Device, interface: str) -> str:
    """
    Checks the status of a specified network interface on the device.

    Args:
    - device (Device): The pyATS device object representing the network device.
    - interface (str): The name of the network interface to check, e.g., 'GigabitEthernet0/1'.

    Returns:
    - str: The status of the interface, such as 'up' or 'down'.
    
    Raises:
    - ValueError: If the interface is not found on the device.
    """
    interface_status = device.parse('show interface {0}'.format(interface))
    if interface not in interface_status:
        raise ValueError(f"Interface {interface} not found on device.")
    
    return interface_status[interface]['line_protocol']


def get_device_uptime(device: Device) -> str:
    """
    Retrieves the uptime of the network device.

    Args:
    - device (Device): The pyATS device object representing the network device.

    Returns:
    - str: The uptime of the device in the format 'dd:hh:mm:ss'.
    """
    uptime = device.parse('show version')['uptime']
    return uptime


def check_device_reachability(ip_address: str) -> bool:
    """
    Checks if a device is reachable via ping.

    Args:
    - ip_address (str): The IP address of the device to ping.

    Returns:
    - bool: True if the device is reachable, False otherwise.
    """
    try:
        response = subprocess.run(['ping', '-c', '4', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if response.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error while pinging device: {e}")
        return False


def get_routing_table(device: Device) -> dict:
    """
    Retrieves the routing table of a network device.

    Args:
    - device (Device): The pyATS device object representing the network device.

    Returns:
    - dict: The routing table parsed into a dictionary format.
    """
    routing_table = device.parse('show ip route')
    return routing_table


def verify_interface_config(device: Device, interface: str, ip_address: str) -> bool:
    """
    Verifies if the specified interface is configured with the given IP address.

    Args:
    - device (Device): The pyATS device object representing the network device.
    - interface (str): The name of the interface to check (e.g., 'GigabitEthernet0/1').
    - ip_address (str): The expected IP address for the interface.

    Returns:
    - bool: True if the interface has the specified IP address, False otherwise.
    
    Raises:
    - ValueError: If the interface is not found on the device.
    """
    interface_config = device.parse(f'show running-config interface {interface}')
    if interface not in interface_config:
        raise ValueError(f"Interface {interface} not found on device.")
    
    configured_ip = interface_config[interface].get('ip address', '')
    return configured_ip == ip_address
