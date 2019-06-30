# TODO: Edit the tests and remove this line.
# Some examples are given below.

import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name,retain", [
    ('root', 'daily'),
    ('root', 'weekly'),
    ('root', 'monthly'),
    ('user', 'daily'),
])
def test_rsnapshot_config_file(host, name, retain):
    file = host.file('/etc/rsnapshot-' + name + '.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.mode == 0o644


@pytest.mark.parametrize("name,retain", [
    ('root', 'daily'),
    ('root', 'weekly'),
    ('root', 'monthly'),
    ('user', 'daily'),
])
def test_rsnapshot_systemd_timer_endabled_started(host, name, retain):
    srv = host.service("rsnapshot-" + name + "-"
                       + retain + ".timer")

    assert srv.is_running
    assert srv.is_enabled


def test_rsnapshot_package(host):
    pkg = host.package('rsnapshot')

    assert pkg.is_installed


@pytest.mark.parametrize("name,retain,time,value", [
    ('root', 'daily', '*-*-* 00:35', '7'),
    ('root', 'weekly', 'Sun *-*-* 00:00', '4'),
    ('root', 'monthly', '*-*-1 01:00', '2'),
    ('user', 'daily', '00:30', '7'),
])
def test_rsnapshot_running_timers(host, name, retain, time, value):
    cmd = host.run('systemctl list-timers')
    timers = cmd.stdout

# rsnapshot-user-daily.timer
    assert "rsnapshot-" + name + "-" + retain + ".timer" in timers
    assert "rsnapshot-" + name + "@" + retain + ".service" in timers
