"""
CLI for simple_encrypt
"""
import os
from argparse import ArgumentParser
from simple_encrypt.simple_encrypt import EncryptDecrypt
from simple_encrypt.util.file_read import read_encrypted_file_data
from simple_encrypt.util.file_write import write_encrypted_file_data


def cli_argument_parser() -> ArgumentParser:
    """Function for argument parsing

    :rtype: ArgumentParser
    :returns: The argument parser
    """
    arg_parser = ArgumentParser(description='simple-encrypt-cli')
    arg_parser.add_argument('--key-file', help='Path and Name of the key file', required=True)
    arg_parser.add_argument('--value-file', help='Path and Name of the value file', required=True)
    subparsers = arg_parser.add_subparsers(title='commands', description='Valid commands: a single command is required',
                                           help='CLI Help', dest='a single command please see the -h option')
    subparsers.required = True

    # This is the sub parser to create NEW
    arg_parser_create = subparsers.add_parser('create', help='Create NEW encrypted data and key')
    arg_parser_create.set_defaults(which_sub='create')
    arg_parser_create.add_argument('-k', '--key', required=True, help='The key to store this at')
    arg_parser_create.add_argument('-u', '--username', required=True, help='The username')
    arg_parser_create.add_argument('-p', '--password', required=True, help='The password')

    # This is the sub parser to add
    arg_parser_add = subparsers.add_parser('add', help='Add encrypted data and key')
    arg_parser_add.set_defaults(which_sub='add')
    arg_parser_add.add_argument('-k', '--key', required=True, help='The key to store this at')
    arg_parser_add.add_argument('-u', '--username', required=True, help='The username')
    arg_parser_add.add_argument('-p', '--password', required=True, help='The password')

    # This is the sub parser to update
    arg_parser_update = subparsers.add_parser('update', help='Update encrypted data and key')
    arg_parser_update.set_defaults(which_sub='update')
    arg_parser_update.add_argument('-k', '--key', required=True, help='The key to store this at')
    arg_parser_update.add_argument('-u', '--username', required=True, help='The username')
    arg_parser_update.add_argument('-p', '--password', required=True, help='The password')

    # This is the sub parser to just get the keys in the encrypted data
    arg_parser_keys = subparsers.add_parser('keys', help='Get current key names')
    arg_parser_keys.set_defaults(which_sub='keys')

    return arg_parser


def cli() -> None:  # pragma: no cover
    """Function to run the command line
    :rtype: None
    :returns: Nothing it is the CLI
    """
    arg_parser = None
    try:
        arg_parser = cli_argument_parser()
        args = arg_parser.parse_args()
        if args.which_sub == 'create':
            if os.path.isfile(args.key_file):
                raise FileExistsError(f'file already exists {args.key_file}!')

            if os.path.isfile(args.value_file):
                raise FileExistsError(f'file already exists {args.value_file}!')

            obj = EncryptDecrypt()
            encrypted_key, encrypted_value = obj.\
                generate_encrypted_data({args.key: {'username': args.username, 'password': args.password}})

            write_encrypted_file_data(args.key_file, encrypted_key)
            write_encrypted_file_data(args.value_file, encrypted_value)

        elif args.which_sub == 'update':
            key = read_encrypted_file_data(args.key_file)
            value = read_encrypted_file_data(args.value_file)
            obj = EncryptDecrypt(key)
            new_value = obj.\
                update_encrypted_data(args.key, {'username': args.username, 'password': args.password}, value)

            write_encrypted_file_data(args.value_file, new_value)

        elif args.which_sub == 'keys':
            key = read_encrypted_file_data(args.key_file)
            value = read_encrypted_file_data(args.value_file)
            obj = EncryptDecrypt(key)
            print(obj.get_current_keys(value))

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
