import re
import yaml
from disco.types.user import GameType, Status

# Emojis
GREEN_TICK_EMOJI_ID = 384876115761561601
RED_TICK_EMOJI_ID = 384875299105406977
GREEN_TICK_EMOJI_NORMAL = 'green_tick:{}'.format(GREEN_TICK_EMOJI_ID)
GREEN_TICK_EMOJI = u'\u2705'
#RED_TICK_EMOJI = u'\u2717'
RED_TICK_EMOJI = 'red_circle:{}'.format(RED_TICK_EMOJI_ID)
RED_TICK_EMOJI_REACT = u'\U0001f534'
STAR_EMOJI = u'\U00002B50'
STATUS_EMOJI = {
    Status.ONLINE: ':status_online:393590483923894292',
    Status.IDLE: ':status_away:393590483919699968',
    Status.DND: ':status_dnd:393590483915636746',
    Status.OFFLINE: ':status_offline:393590483533692930',
    GameType.STREAMING: ':status_streaming:393591106673180672',
}
SNOOZE_EMOJI = u'\U0001f4a4'


# Regexes
INVITE_LINK_RE = re.compile(r'(discordapp.com/invite|discord.me|discord.gg)(?:/#)?(?:/invite)?/([a-z0-9\-]+)', re.I)
URL_RE = re.compile(r'(https?://[^\s]+)')
EMOJI_RE = re.compile(r'<:(.+):([0-9]+)>')
USER_MENTION_RE = re.compile('<@!?([0-9]+)>')

# IDs and such
ROWBOAT_GUILD_ID = 387817296527228928
ROWBOAT_USER_ROLE_ID = 392854838158819329




# Discord Error codes
ERR_UNKNOWN_MESSAGE = 10008

# Etc
YEAR_IN_SEC = 60 * 60 * 24 * 365
CDN_URL = 'https://twemoji.maxcdn.com/2/72x72/{}.png'

# Loaded from files
with open('data/badwords.txt', 'r') as f:
    BAD_WORDS = f.readlines()

# Merge in any overrides in the config
with open('config.yaml', 'r') as f:
    loaded = yaml.load(f.read())
    locals().update(loaded.get('constants', {}))
