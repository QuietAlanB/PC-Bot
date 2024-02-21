from discord.ext import commands

class Help(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        await self.context.send("help text")

    async def send_command_help(self, command):
        await self.context.send("help text for command")

    async def send_group_help(self, group):
        pass

    async def send_cog_help(self, cog):
        pass

    async def send_error_message(self, error):
        await self.context.send("error")