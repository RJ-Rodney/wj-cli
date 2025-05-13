import cmd
import socket


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

        if line == "info":
            print(net_info)
            print(f"    > Hostname: {hostname}")
            print(f"    > IP Address: {ip_address}")


if __name__ == '__main__':
    CLI().cmdloop()
