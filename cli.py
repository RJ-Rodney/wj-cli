import cmd
import socket
import subprocess
import platform


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

    def do_network(self, line):
        """
        - network
            Displays General Information on Your Network.
        """

        net_info = "    Information on your network."

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        system = platform.system()

        if line == "info":
            print(net_info)
            print(f"    > Hostname: {hostname}")
            print(f"    > IP Address: {ip_address}")
        elif line == "flushdns":
            print(net_info)
            print(f"    > Hostname: {hostname}")
            print(f"    > IP Address: {ip_address}")
            print("\n")
            try: 
                if system == "Windows":
                    subprocess.run(["ipconfig", "/flushdns"], check=True)
                elif system == "Linux":
                    subprocess.run(["sudo", "systemd-resolve", "--flush-caches"], check=True)
                else:
                    print(f"Unsupported system type: {system}")
                    return
                print("DNS Cache Flushed Successfully.")
            except subprocess.CalledProcessorError as e:
                print(f"Error Flushing DNS: {e}")
            except FileNotFoundError:
                print("One or more commands not found. Ensure they are installed and in your system's PATH.")
            

if __name__ == '__main__':
    CLI().cmdloop()
