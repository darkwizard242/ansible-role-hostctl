import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/hostctl'


def test_hostctl_binary_exists(host):
    """
    Tests if hostctl binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_hostctl_binary_file(host):
    """
    Tests if hostctl binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_hostctl_binary_which(host):
    """
    Tests the output to confirm hostctl's binary location.
    """
    assert host.check_output('which hostctl') == PACKAGE_BINARY
