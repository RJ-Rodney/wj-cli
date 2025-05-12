import cmd

class CLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to WARJORN CLI. Type "help" for available commands.'

    def do_hello(self, line):
        # Print Greeting
        print("Hello, World!")

    def do_quit(self, line):
        # Exit CLI
        return True

if __name__ == '__main__':
    CLI().cmdloop()