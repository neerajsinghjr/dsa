import bluetooth

def discover_devices():
    devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                         device_id=-1, lookup_oui=True,
                                         device_class=0, filter_oui=True,
                                         lookup_oui_name=True, device_name="",
                                          device_address="", device_port=0)
    return devices

def get_battery_info(device_address):
    services = bluetooth.find_service(address=device_address)
    for service in services:
        print("Service:", service)
        # Depending on the Bluetooth device and its profiles, you might find relevant battery information in the service details.

if __name__ == "__main__":
    # Discover nearby Bluetooth devices
    nearby_devices = discover_devices()

    # Print discovered devices
    print("Discovered Devices:")
    for addr, name, _ in nearby_devices:
        print(f"{name} ({addr})")

    # Choose a device (replace with the actual address of your Bluetooth device)
    chosen_device_address = "00:11:22:33:44:55"

    # Get battery information for the chosen device
    get_battery_info(chosen_device_address)
