# -*- coding:utf8 -*-
import functools
import textwrap
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

    @botcmd
    @require_iam
    def route53_list(self, msg, args):
        return "It is a stub"
