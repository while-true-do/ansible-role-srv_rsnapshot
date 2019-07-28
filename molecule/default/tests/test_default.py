import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rsnapshot_package(host):
    pkg = host.package('rsnapshot')

    assert pkg.is_installed


@pytest.mark.parametrize("name", [
    ("daily"),
    ("weekly"),
    ("monthly"),
])
def test_rsnapshot_timer(host, name):
    timer = host.service("rsnapshot-"+name+".timer")

    assert timer.is_enabled


def test_rsansphot_exec_timer(host):
    file1 = host.file("/.snapshots/daily.0/localhost/etc/")
    file2 = host.file("/.snapshots/daily.0/localhost/home/")
    file3 = host.file("/.snapshots/daily.0/localhost/var/")

    with host.sudo():
        host.run("systemctl start rsnapshot@daily.service")

        assert file1.exists
        assert file2.exists
        assert file3.exists
