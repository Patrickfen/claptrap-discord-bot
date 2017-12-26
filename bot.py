import plugins
import importlib
import re
import traceback

class Bot(object):
    def __init__(self, client):
        self.client = client
        self.setup_plugins()

    def reload(self):
        plugins.reload()
        importlib.reload(plugins)
        self.setup_plugins()

    def setup_plugins(self):
        self.plugins = {
            'ping':plugins.ping.Ping(self.client),
            'warnme':plugins.warnme.WarnMe(self.client)
        }

    async def handle(self, message):
        match = re.match('(![a-zA-Z0-9]+)(.+)?', message.content)
        if match:
            command = match.group(1)[1:]
            params = match.group(2)
            if params:
                params = params.strip()
            try:
                await self.plugins[command](message, params)
            except KeyError:
                await self.client.send_message(message.channel, 'Nope, not found.')
            except Exception as e:
                await self.client.send_message(message.channel, 'Erk! you dun goofed: {}'.format(e))
                traceback.print_exc()
                print('============')
