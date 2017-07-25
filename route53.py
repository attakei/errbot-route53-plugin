# -*- coding:utf8 -*-
import functools
import textwrap
import boto3
from errbot import BotPlugin, botcmd


def require_iam(f):
    """Deforator for bot command required IAM user key pair
    """
    @functools.wraps(f)
    def _require_iam(bot, msg, args):
        if not bot.config \
                or not bot.config.get('access_id', None) \
                or not bot.config.get('secret_key', None):
            return bot.not_configured()
        return f(bot, msg, args)
    return _require_iam


class Route53(BotPlugin):
    """
    Control Route 53
    """

    def not_configured(self):
        message = """
            This plugin is until not configured.
            Please call `{}plugin config route53` to read format,
            And set your configurations.
            """
        return textwrap.dedent(message).format(self.bot_config.BOT_PREFIX)

    def get_configuration_template(self):
        """
        Defines the configuration structure this plugin supports.
        """
        config = {
            'access_id': None,
            'secret_key': None,
        }
        return config

    def get_client(self):
        """Return CloudFront client by boto3.
        This client is configuret by plugin configuration.
        """
        return boto3.client(
            'route53',
            aws_access_key_id=self.config['access_id'],
            aws_secret_access_key=self.config['secret_key'],
        )

    @botcmd(template='zone_list')
    @require_iam
    def route53_list(self, msg, args):
        client = self.get_client()
        result = client.list_hosted_zones()
        return {'zones': result['HostedZones']}