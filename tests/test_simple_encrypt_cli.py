from simple_encrypt.simple_encrypt_cli import cli_argument_parser


def test_cli_argument_parser_keys():
    arg_parser = cli_argument_parser()
    args = arg_parser.parse_args(['--key-file', './fake-key', '--value-file', './fake-value', 'keys'])

    assert args.which_sub == 'keys'
    assert args.key_file == './fake-key'
    assert args.value_file == './fake-value'


def test_cli_argument_parser_create():
    arg_parser = cli_argument_parser()
    args = arg_parser.parse_args(['--key-file', './fake-key', '--value-file', './fake-value',
                                  'create',
                                  '-k', 'MOO', '-u', 'fake-username', '-p', 'fake-password'])

    assert args.which_sub == 'create'
    assert args.key_file == './fake-key'
    assert args.value_file == './fake-value'
    assert args.key == 'MOO'
    assert args.username == 'fake-username'
    assert args.password == 'fake-password'


def test_cli_argument_parser_update():
    arg_parser = cli_argument_parser()
    args = arg_parser.parse_args(['--key-file', './fake-key', '--value-file', './fake-value',
                                  'update',
                                  '-k', 'MOO', '-u', 'fake-username', '-p', 'fake-password'])

    assert args.which_sub == 'update'
    assert args.key_file == './fake-key'
    assert args.value_file == './fake-value'
    assert args.key == 'MOO'
    assert args.username == 'fake-username'
    assert args.password == 'fake-password'


def test_cli_argument_parser_add():
    arg_parser = cli_argument_parser()
    args = arg_parser.parse_args(['--key-file', './fake-key', '--value-file', './fake-value',
                                  'add',
                                  '-k', 'MOO', '-u', 'fake-username', '-p', 'fake-password'])

    assert args.which_sub == 'add'
    assert args.key_file == './fake-key'
    assert args.value_file == './fake-value'
    assert args.key == 'MOO'
    assert args.username == 'fake-username'
    assert args.password == 'fake-password'
