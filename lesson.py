from netmiko import ConnectHandler


router_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.10.40',
    'port': 32770,
    'username': 'admin',
    'password': 'eve123',
    'secret': 'eve123',
}


try:
    print("Connecting to router...")
    net_connect = ConnectHandler(**router_device)


    net_connect.enable()


    # List
    commands_to_run = [
        "show version",
        "show ip interface brief",
        "show running-config",
        "show ip route"
    ]


    # Loop 
    for cmd in commands_to_run:
        print(f"\n--- Output for: {cmd} ---")
        output = net_connect.send_command(cmd)
        print(output)


    net_connect.disconnect()
    print("\nDisconnected successfully.")
except Exception as e:
    print(f"Connection failed: {e}")