import cmd
import socket
import subprocess
import platform
import requests


def check_txt_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error checking for updates: {e}")
        return None


version = "1.0.0-BETA"


class CLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to WARJORN CLI. Type "help" for available commands.'

    def do_hello(self, line):
        """
        - hello
            Print 'Hello, World!'.
        """
        print("Hello, World!")

    def do_quit(self, line):
        """
        - quit
            Quit the CLI.
        """
        return True

    def do_exit(self, line):
        """
        - exit
            Exit the CLI.
        """
        return True

    def do_network(self, line):
        """
        - network
            Displays General Information on Your Network.
            
            - info
                Displays General Information on Your Network.
            - flushdns
                Flushes the DNS Cache on Your System.
        """

        net_info = "    Information on your network."

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system = platform.system()

        if line == "info":
            print(f"""{net_info}
            > Hostname: {hostname}
            > IP Address: {ip_address}""")
        elif line == "flushdns":
            print(f"""{net_info}
                Flushing DNS Cache on {system} System.
                > Hostname: {hostname}
                > IP Address: {ip_address}
                """)
            try:
                if system == "Windows":
                    subprocess.run(["ipconfig", "/flushdns"], check=True)
                elif system == "Linux":
                    try:
                        subprocess.run(
                            ["sudo", "systemd-resolve", "--flush-caches"],
                            check=True)
                    except:
                        print("Linux support limited.")
                        return
                else:
                    print(f"Unsupported system type: {system}")
                    return
                print("DNS Cache Flushed Successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error Flushing DNS: {e}")
            except FileNotFoundError:
                print(
                    "One or more commands not found. Ensure they are installed and in your system's PATH."
                )
        else:
            print(f"""{net_info}
            > Hostname: {hostname}
            > IP Address: {ip_address}""")

    def do_version(self, line):
        """
        - version
            Displays the current version of the CLI.
        """
        print(f"You are running version: {version}")
        print("    > Type 'update' to check for updates.")
        print("    > Type 'help' for more information.")
        print("    > Type 'quit' or 'exit' to quit the CLI.")

    def do_update(self, line):
        """
        - update
            Checks for updates to the CLI.
        """
        print("Checking for updates...")
        url = "https://raw.githubusercontent.com/RJ-Rodney/wj-cli/refs/heads/main/version.txt"
        latest_version = check_txt_file(url)
        if latest_version.strip() == version:
            print("You are up to date!")
        elif latest_version is None:
            print("Failed to check for updates.")
        else:
            print("There is a new update available!")
            print(f"    > Current Version: {version}")
            print(f"    > Latest Version: {latest_version}")


if __name__ == '__main__':
    CLI().cmdloop()

    print("Goodbye!")
