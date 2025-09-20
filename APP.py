import random, string,discord, os,requests
def pswd_gnrtor(lenght= 25):
    charac_pswrd = string.ascii_letters + string.digits + string.punctuation +string.ascii_uppercase
    pswd = ""

    for i in range(lenght):
        pswd += random.choice(charac_pswrd)
    return pswd
def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "HEADS"
    else:
        return "TAILS"
def meme ():
    
    with open("img/meme 2.jpeg" ,"rb") as f:
        picture = discord.File(f)
        return picture
def memes ():
    
    lista_memes = random.choice(os.listdir("img"))
    with open(f"img/{lista_memes}" ,"rb") as f:
        picture = discord.File(f)
        return picture
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']