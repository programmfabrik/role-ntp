import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_binary(File):
    f = File('/usr/sbin/ntpd')
    assert f.exists


def test_timezone(File):
    f = File('/etc/timezone')
    assert f.content_string == 'Europe/Berlin'


@pytest.mark.parametrize('upstream', [
    '0.europe.pool.ntp.org',
    '1.europe.pool.ntp.org',
    '2.europe.pool.ntp.org',
    '3.europe.pool.ntp.org',
])
def test_upstreams(File, upstream):
    f = File('/etc/ntp.conf')
    c = f.content_string

    for line in c.split():
        if line.strip() == upstream.strip():
            return True

    raise AssertionError("upstream not found in configuration file: {}".format(upstream))
