# TODO: Edit the tests and remove this line.
# Some examples are given below.

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rsnapshot_package(host):
    pkg = host.package('rsnapshot')

    assert pkg.is_installed
