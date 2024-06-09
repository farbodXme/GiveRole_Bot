import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to keep track of roles to remove
roles_to_remove = {}

# Set the specific role ID that the bot should respond to
ROLE_ID = 1246329336600989726  # Replace with your specific role ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    check_roles.start()  # Start the task to check roles periodically

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if the member has the specific role
    role = discord.utils.get(message.guild.roles, id=ROLE_ID)
    if role in message.author.roles:
        if message.content == "سلام":
            await message.channel.send("سلام")
    await bot.process_commands(message)  # Ensure commands are processed

@bot.command()
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, role: discord.Role, days: int):
    await member.add_roles(role)
    end_time = datetime.utcnow() + timedelta(days=days)
    roles_to_remove[(member.id, role.id)] = end_time
    expiry_date = (datetime.utcnow() + timedelta(days=days)).strftime("%Y-%m-%d")
    await ctx.send(f'**Role {role.name} added to `{member.name}` for {days} days. \n Expires on {expiry_date}.**')

@tasks.loop(minutes=1)
async def check_roles():
    current_time = datetime.utcnow()
    to_remove = []
    for (member_id, role_id), end_time in roles_to_remove.items():
        if current_time >= end_time:
            guild = bot.guilds[0]  # Assuming the bot is only in one server
            member = guild.get_member(member_id)
            role = guild.get_role(role_id)
            if member and role:
                await member.remove_roles(role)
                to_remove.append((member_id, role_id))

    for key in to_remove:
        del roles_to_remove[key]

@bot.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f'Role {role.name} removed from {member.name}.')
    roles_to_remove.pop((member.id, role.id), None)

bot.run('YOUR_BOT_TOKEN')
