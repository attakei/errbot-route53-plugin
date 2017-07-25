# -*- coding:utf8 -*-


pytest_plugins = [
    'errbot.backends.test',
]
extra_plugin_dir = '.'


def test_installed_plugin(testbot):
    testbot.push_message('!status plugins')
    assert 'route53' in testbot.pop_message()
