import discord

def tag_recycler():
    embed= discord.Embed(title="Recycle Ideas", 
                         description="Here you got an Ideas for recycle materials and reduce the contamination", 
                         color=0xBDE3C3)

    embed.add_field(name="Cristal Bowls", 
                    value="1. You can aproach the cristal bowls for so many things, even like a flowerpot.",
                      inline=False)
    embed.set_thumbnail(url="https://i.postimg.cc/52sF0cLp/prueba-vidrio.jpg")
    
    embed.add_field(name="Ecotip 1",
                    value="2. Don't use the light when its not necessary, you can save a lot of energy.",
                      inline=False)
    embed.set_thumbnail(url="https://i.postimg.cc/02XFxjrN/meme-eco.jpg")
    
    embed.add_field(name="Ecotip 2",
                    value="3. Use bycicles instead cars, you can arrived in less time.",
                      inline=False)
    embed.set_thumbnail(url="https://imgflip.com/i/a6otxy")
    
    
    return embed