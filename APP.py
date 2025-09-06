import random, string
def pswd_gnrtor(lenght):
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
    