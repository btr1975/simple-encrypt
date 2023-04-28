"""
CLI for simple_encrypt
"""
from argparse import ArgumentParser


def cli() -> None:
    """Function to run the command line
    :rtype: None
    :returns: Nothing it is the CLI
    """
    arg_parser = ArgumentParser(description='simple-encrypt-cli')
    subparsers = arg_parser.add_subparsers(title='commands', description='Valid commands: a single command is required',
                                           help='CLI Help', dest='a single command please see the -h option')
    subparsers.required = True

    # This is the sub parser to print hello
    arg_parser_hello = subparsers.add_parser('hello', help='Say Hello')
    arg_parser_hello.set_defaults(which_sub='hello')
    arg_parser_hello.add_argument('-n', '--name', required=True, help='Your name')

    # This is the sub parser to print goodbye
    arg_parser_goodbye = subparsers.add_parser('goodbye', help='Say Goodbye')
    arg_parser_goodbye.set_defaults(which_sub='goodbye')
    arg_parser_goodbye.add_argument('-n', '--name', required=True, help='Your name')

    args = arg_parser.parse_args()

    try:
        print(args)

    except AttributeError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except FileNotFoundError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except FileExistsError as error:
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()

    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f'\n !!! {error} !!! \n')
        arg_parser.print_help()
