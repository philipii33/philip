from flask import Flask, render_template, request
from netmiko import ConnectHandler

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    results = {}
    error = None

    if request.method == "POST":

        # Cisco Router Configuration
        router_device = {
            'device_type': 'cisco_ios_telnet',
            'ip': '192.168.10.40',
            'port': 32770,
            'username': 'admin',
            'password': 'eve123',
            'secret': 'eve123',
        }

        # Commands to Execute
        commands_to_run = [
            "show version",
            "show ip interface brief",
            "show running-config"
        ]

        net_connect = None

        try:
            print("Connecting to router...")

            # Establish Connection
            net_connect = ConnectHandler(**router_device)

            # Enter Enable Mode
            net_connect.enable()

            print("Connected successfully!")

            # Execute Commands
            for cmd in commands_to_run:

                print(f"Executing: {cmd}")

                output = net_connect.send_command(cmd)

                results[cmd] = output

            print("All commands executed successfully.")

        except Exception as e:

            error = f"Connection failed: {e}"

            print(error)

        finally:

            # Disconnect from Router
            if net_connect:
                net_connect.disconnect()
                print("Disconnected from router.")

    # Display HTML Dashboard
    return render_template(
        "index.html",
        results=results,
        error=error
    )


if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
