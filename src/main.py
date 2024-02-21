import discord
from discord.ext import commands
from discord.ext.commands import bot
import pyautogui
import re

from help import Help

pyautogui.FAILSAFE = False

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = ">", intents = intents)
bot.help_command = Help()

tokenFile = open("token", "r")
token = tokenFile.read()
tokenFile.close()

@bot.listen("on_ready")
async def on_ready():
        print("its ready")

@bot.command(name="move")
async def movemouse(ctx, x = None, y = None):
        if (x == None):
                await ctx.send(f":warning: X coordinate not specified")
                return
        if (y == None):
                await ctx.send(f":warning: Y coordinate not specified")
                return

        if (not x.isdecimal()):
                await ctx.send(f":warning: X coordinate is not an integer")
                return
        if (not y.isdecimal()):
                await ctx.send(f":warning: Y coordinate is not an integer")
                return
        
        x = int(x)
        y = int(y)

        pyautogui.moveTo(x, y)
        await ctx.send(f":white_check_mark: Moved mouse to ({x}, {y})")

@bot.command(name="moverel")
async def movemouse(ctx, x = None, y = None):
        if (x == None):
                await ctx.send(f":warning: X coordinate not specified")
                return
        if (y == None):
                await ctx.send(f":warning: Y coordinate not specified")
                return

        if (not x.isdigit()):
                await ctx.send(f":warning: X coordinate is not an integer")
                return
        if (not y.isdigit()):
                await ctx.send(f":warning: Y coordinate is not an integer")
                return
        
        x = int(x)
        y = int(y)

        pyautogui.moveRel(x, y)
        await ctx.send(f":white_check_mark: Moved mouse by ({x}, {y})")

@bot.command(name="click")
async def click(ctx, button = "left"):
        if (button.lower() in ["left", "l", "lmb"]): 
                button = "LMB"
                pyautogui.leftClick()
        elif (button.lower() in ["mid", "middle", "m", "mmb"]): 
                button = "MMB"
                pyautogui.middleClick()
        elif (button.lower() in ["right", "r", "rmb"]): 
                button = "RMB"
                pyautogui.rightClick()
        else:
                await ctx.send(f":warning: Invalid mouse button")
                return

        await ctx.send(f":white_check_mark: Clicked {button}")

@bot.command(name="press")
async def press(ctx, key = None):
        if (key == None):
                await ctx.send(f":warning: Key not specified")
                return
        
        if (key.lower() not in pyautogui.KEYBOARD_KEYS):
                await ctx.send(f":warning: Invalid key")
                return
        
        pyautogui.press(key.lower())

        await ctx.send(f":white_check_mark: Pressed '{key.lower()}'")

@bot.command(name="screen")
async def screen(ctx):
        screenshot = pyautogui.screenshot()
        screenshot.save("res/screenshot/image.png")

        screenshotImage = discord.File("res/screenshot/image.png")

        await ctx.send(file=screenshotImage)

bot.run(token)