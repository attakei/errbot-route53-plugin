# -*- coding:utf8 -*-
from unittest.mock import patch
import time


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
    testbot.push_message('!route53_list')
    assert 'This plugin is until not configured' \
        in testbot.pop_message()


def test_list_configured(testbot):
    inject_dummy_conf(testbot)
    with patch('boto3.client') as Client:
        client = Client.return_value
        client.list_hosted_zones.return_value = {
            'HostedZones': [
                {
                    'Id': 'zone-id',
                    'Name': 'example.com',
                    'Config': {
                        'Comment': 'My zone',
                        'PrivateZone': False,
                    },
                    'ResourceRecordSetCount': 123
                },
            ],
        }
        testbot.push_message('!route53 list')
        assert 'example.com' in testbot.pop_message()


def test_detail_not_found(testbot):
    import textwrap
    inject_dummy_conf(testbot)
    with patch('boto3.client') as Client:
        client = Client.return_value
        client.list_resource_record_sets.return_value = {
            'ResourceRecordSets': [
                {
                    'Name': 'a.example.com',
                    'Type': 'A',
                    'ResourceRecords': [
                        {
                            'Value': '127.0.0.1'
                        },
                    ],
                },
            ],
        }
        testbot.push_message('!route53 zone ABCDEF')
        expect = """
            - a.example.com : A
                - 127.0.0.1
            """
        assert testbot.bot.md.convert(textwrap.dedent(expect)) \
            in testbot.pop_message()
