from django import template
from social.models import Profil

register = template.Library()

@register.tag
def avatar(parser, token):
    """
    Allows to recover the avatar from User id
    :param parser: not used here
    :param token: data retrieved from tag call
    """
    # extract parameter from tag
    try:
        tag_name, Uid = token.split_contents()
    except ValueError:
        msg = '%r tag must one and only one argument.'% token.contents.split()[0]
        raise template.TemplateSyntaxError(msg)

    return AvatarNode(Uid)

class AvatarNode(template.Node):
    def __init__(self, Uid):
        self.Uid = template.Variable(Uid)

    def render(self, context):
        self.Uid = self.Uid.resolve(context)
        Prof = Profil.objects.filter(user_id = self.Uid)
        Prof = Prof[0]
        return Prof.avatar.url