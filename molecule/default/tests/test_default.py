import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_bind_running(host):
    assert host.service('bind9').is_running


def test_bind_enabled(host):
    assert host.service('bind9').is_enabled


def test_domain_ports_listening(host):
    assert host.socket('tcp://53').is_listening
    assert host.socket('udp://53').is_listening
