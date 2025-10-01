import discord
import aiohttp
import asyncio

TOKEN = "MTQyMjc2Mjc4Mzk4Nzk5MDY4OQ.G4NTQ0.a_-qBiDEZZe2u4rSi7OPnYZ8uupBY2bFHlMpjs"
CHANNEL_ID = 1422762603331194964  # ID-ul canalului unde să trimită alerta
BUNDLE_ID = 201

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def check_headless():
    url = f"https://catalog.roblox.com/v1/bundles/{BUNDLE_ID}/details"
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        if data.get("product", {}).get("isForSale", False):
                            channel = client.get_channel(CHANNEL_ID)
                            if channel:
                                await channel.send("⚠️ Headless Horseman este disponibil pe Roblox! 🔥 https://www.roblox.com/bundles/201")
                            return  # după alertă oprim (sau scoate asta dacă vrei să continue)
                    else:
                        print("Eroare la request:", resp.status)
            except Exception as e:
                print("Eroare:", e)
            
            await asyncio.sleep(60)  # verifică la fiecare 60 secunde

@client.event
async def on_ready():
    print(f"{client.user} este online!")
    client.loop.create_task(check_headless())

client.run(TOKEN)
