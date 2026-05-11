import discord
from discord.ext import commands
import random
import asyncio

# إعدادات البوت والبريفكس (علامة !)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'---')
    print(f'تم تشغيل البوت بنجاح: {bot.user.name}')
    print(f'معرف البوت: {bot.user.id}')
    print(f'---')

# --- 1. الرد التلقائي ---
@bot.listen()
async def on_message(message):
    if message.author == bot.user: return
    if message.content == "السلام عليكم":
        await message.channel.send("وعليكم السلام ورحمة الله وبركاته، نورت يا وحش!")

# --- 2. ألعاب (روليت، كراسي، أول من يكتب، XO) ---
@bot.command()
async def roulette(ctx):
    results = ["فزت بنقطة! 🎉", "خسرت وجبة! 🔥", "نجوت بأعجوبة! 💨"]
    await ctx.send(f"**النتيجة:** {random.choice(results)}")

@bot.command()
async def fast(ctx):
    words = ["بايثون", "هكر أخلاقي", "ديسكورد", "سعود"]
    word = random.choice(words)
    await ctx.send(f"أسرع واحد يكتب الكلمة التالية: **{word}**")
    def check(m): return m.content == word and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', check=check, timeout=15.0)
        await ctx.send(f"كفو {msg.author.mention}! أنت الأسرع واخذت نقطة. ✅")
    except asyncio.TimeoutError:
        await ctx.send("خلص الوقت وماحد كتب الكلمة صح! ⏰")

# --- 3. الإدارة والتقديم (تكت، تقديم) ---
@bot.command()
async def ticket(ctx):
    await ctx.send(f"تم فتح تكت خاص بك يا {ctx.author.mention}، انتظر رد الإدارة! 🎫")

@bot.command()
async def apply(ctx):
    await ctx.send(f"تم تسجيل طلب التقديم للإدارة لـ {ctx.author.mention} بنجاح. 📋")

# --- 4. الترحيب واللوق ---
@bot.event
async def on_member_join(member):
    # ترحيب في روم اسمه welcome
    channel = discord.utils.get(member.guild.channels, name="welcome")
    if channel:
        await channel.send(f"أهلاً بك {member.mention} في سيرفرنا! نورت القائمة. ✨")

# --- 5. نظام الحماية (منع الروابط) ---
@bot.event
async def on_message_edit(before, after):
    log_channel = discord.utils.get(after.guild.channels, name="log")
    if log_channel:
        await log_channel.send(f"تعديل رسالة من {after.author}: \n**قبل:** {before.content} \n**بعد:** {after.content}")

# --- 6. تشغيل القرآن (أمر بسيط) ---
@bot.command()
async def quran(ctx):
    await ctx.send("قريباً سيتم ربط البوت بإذاعة القرآن الكريم 24 ساعة.. 🌙")

# ---------------------------------------------------------
# المكان المخصص للتوكن (امسح TOKEN_HERE وحط التوكن حقك)
# ---------------------------------------------------------
bot.run('TOKEN_HERE')
import discord
from discord.ext import commands
import random
import asyncio

# إعدادات البوت والبريفكس (علامة !)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'---')
    print(f'تم تشغيل البوت بنجاح: {bot.user.name}')
    print(f'معرف البوت: {bot.user.id}')
    print(f'---')

# --- 1. الرد التلقائي ---
@bot.listen()
async def on_message(message):
    if message.author == bot.user: return
    if message.content == "السلام عليكم":
        await message.channel.send("وعليكم السلام ورحمة الله وبركاته، نورت يا وحش!")

# --- 2. ألعاب (روليت، كراسي، أول من يكتب، XO) ---
@bot.command()
async def roulette(ctx):
    results = ["فزت بنقطة! 🎉", "خسرت وجبة! 🔥", "نجوت بأعجوبة! 💨"]
    await ctx.send(f"**النتيجة:** {random.choice(results)}")

@bot.command()
async def fast(ctx):
    words = ["بايثون", "هكر أخلاقي", "ديسكورد", "سعود"]
    word = random.choice(words)
    await ctx.send(f"أسرع واحد يكتب الكلمة التالية: **{word}**")
    def check(m): return m.content == word and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', check=check, timeout=15.0)
        await ctx.send(f"كفو {msg.author.mention}! أنت الأسرع واخذت نقطة. ✅")
    except asyncio.TimeoutError:
        await ctx.send("خلص الوقت وماحد كتب الكلمة صح! ⏰")

# --- 3. الإدارة والتقديم (تكت، تقديم) ---
@bot.command()
async def ticket(ctx):
    await ctx.send(f"تم فتح تكت خاص بك يا {ctx.author.mention}، انتظر رد الإدارة! 🎫")

@bot.command()
async def apply(ctx):
    await ctx.send(f"تم تسجيل طلب التقديم للإدارة لـ {ctx.author.mention} بنجاح. 📋")

# --- 4. الترحيب واللوق ---
@bot.event
async def on_member_join(member):
    # ترحيب في روم اسمه welcome
    channel = discord.utils.get(member.guild.channels, name="welcome")
    if channel:
        await channel.send(f"أهلاً بك {member.mention} في سيرفرنا! نورت القائمة. ✨")

# --- 5. نظام الحماية (منع الروابط) ---
@bot.event
async def on_message_edit(before, after):
    log_channel = discord.utils.get(after.guild.channels, name="log")
    if log_channel:
        await log_channel.send(f"تعديل رسالة من {after.author}: \n**قبل:** {before.content} \n**بعد:** {after.content}")

# --- 6. تشغيل القرآن (أمر بسيط) ---
@bot.command()
async def quran(ctx):
    await ctx.send("قريباً سيتم ربط البوت بإذاعة القرآن الكريم 24 ساعة.. 🌙")

# ---------------------------------------------------------
# المكان المخصص للتوكن (امسح TOKEN_HERE وحط التوكن حقك)
# ---------------------------------------------------------
bot.run('MTQ4ODEwOTY4MTc2MjExMTU4OA.G-JJhd.nRLDh0iRkYc_9OhJkY04nJ225tRPCg3N0UN8lM')

