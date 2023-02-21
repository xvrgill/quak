"""
Usage: create_kernel.py [options]

Install ipykernel for project poetry environment.

Options:
    -h --help                Show help.
    -u --user                Install kernel in user scope.
    -n <name> --name=<name>  Kernel name.
    -l <file> --log=<file>   Write log to output file [default: ./quak.log]
"""
from docopt import docopt
from rich.console import Console
from rich.table import Table

# initializing rich console object for displaying output
console = Console()


def show_help(args: dict) -> None:
    """Display help by showing usage patern in console.

    :param args: all available arguments and options
    :return: None
    """
    # print usage string
    console.print("\n")
    console.print("[underline]Usage[/]")
    console.print("\n")
    console.print("[green]create_kernel.py[/] [bright_white]\[options][/]")
    console.print("\n")

    # print script description
    console.print("[underline]Description[/]")
    console.print("\n")
    console.print("Install ipykernel for project poetry environment.")

    # print options header
    console.print("[underline]Options[/]\n")

    # print options and option descriptions
    grid = Table.grid()
    grid.add_column(width=28, style="yellow")
    grid.add_column(width=76, justify="left", style="bright_white")
    grid.add_row("  -h --help", "Show help.")
    grid.add_row("  -u --user", "Install kernel in user scope.")
    grid.add_row("  -n <name> --name=<name>", "Kernel name.")
    grid.add_row("  -l <file> --log=<file>", "Write log to output file [default: ./quak.log]")
    console.print(grid)


if __name__ == '__main__':
    arguments = docopt(__doc__, help=False)

    # console.print(arguments)

    if arguments["--help"]:
        show_help(arguments)
