import discord
from discord.ext import commands
import random
import asyncio

# إعدادات البوت والبريفكس
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'تم تشغيل البوت: {bot.user}')

# --- 1. نظام الترحيب واللوق ---
@bot.event
async def on_member_join(member):
    # ترحيب
    welcome_channel = discord.utils.get(member.guild.channels, name="welcome")
    if welcome_channel:
        await welcome_channel.send(f"نورت السيرفر يا {member.mention}! ✨")
    
    # لوق دخول
    log_channel = discord.utils.get(member.guild.channels, name="log")
    if log_channel:
        await log_channel.send(f"📥 دخول عضو جديد: {member.name}")

# --- 2. ألعاب (روليت، كراسي، أول من يكتب، العلم) ---
@bot.command()
async def roulette(ctx):
    results = ["فزت! 🎉", "خسرت! 🔥", "نجوت! 💨"]
    await ctx.send(f"النتيجة: {random.choice(results)}")

@bot.command()
async def chairs(ctx):
    await ctx.send("بدأت لعبة الكراسي! استعدوا...")
    await asyncio.sleep(3)
    await ctx.send("جلس الجميع! وفاز أسرع واحد جلس على الكرسي الأخير 🪑")

@bot.command()
async def fast(ctx):
    words = ["مستكشف", "ديسكورد", "بايثون", "سعود"]
    word = random.choice(words)
    await ctx.send(f"أسرع واحد يكتب: **{word}**")
    def check(m): return m.content == word and m.channel == ctx.channel
    msg = await bot.wait_for('message', check=check)
    await ctx.send(f"كفو {msg.author.mention}! أنت الأسرع.")

# --- 3. أنظمة الإدارة (تكت، تقديم، حماية) ---
@bot.command()
async def ticket(ctx):
    # كود مبسط لفتح تكت
    await ctx.send("تم فتح تكت خاص بك في الدعم الفني 🎫")

@bot.command()
async def apply(ctx):
    await ctx.send("تم إرسال طلب التقديم للإدارة، انتظر الرد في الخاص 📋")

# --- 4. تفاعل (رد تلقائي، مستويات، هدايا) ---
@bot.listen()
async def on_message(message):
    if message.author == bot.user: return
    # رد تلقائي
    if message.content == "السلام عليكم":
        await message.channel.send("وعليكم السلام ورحمة الله وبركاته")

@bot.command()
async def gift(ctx):
    prizes = ["100 نقطة 💰", "رتبة مميزة 🎖️", "حظ أوفر 👻"]
    await ctx.send(f"مبروك، حصلت من عجلة الهدايا على: {random.choice(prizes)}")

# حط التوكن هنا
bot.run(MTQ4ODEwOTY4MTc2MjExMTU4OA.GakaiU.B2CRF564Q3aThUM45_wnTP4T1ZbcSDfKxVpKXo)
