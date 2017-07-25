# -*- coding:utf8 -*-


pytest_plugins = [
    'errbot.backends.test',
]
extra_plugin_dir = '.'


def inject_dummy_conf(bot):
    bot.push_message('!plugin config route53 '\
        '{"access_id":"1","secret_key":"1"}')
    bot.pop_message()


def test_installed_plugin(testbot):
    testbot.push_message('!status plugins')
    assert 'route53' in testbot.pop_message()


def test_not_configured(testbot):
    testbot.push_message('!route53 list')
    assert 'This plugin is until not configured' \
        in testbot.pop_message()


def test_list_configured(testbot):
    inject_dummy_conf(testbot)
    testbot.push_message('!route53 list')
    assert 'This plugin is until not configured' \
        not in testbot.pop_message()
