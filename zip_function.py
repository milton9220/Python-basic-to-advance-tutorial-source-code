#zip function ak shate combine kore.
user_id=[1,2,3]
user_first_name=["Abrar","Adnan","Alu"]
user_last_name=["Hasan","Shariar","Potol"]

all=zip(user_id,user_first_name,user_last_name)
#uporer line print korle kisu show korbe na karon eita zip object .Otthat eita iterator kora. eita k loop r maddhome print korte pari.loop r maddhome print korle touples akare print hobe .
for i in all:
    print(i)

#abar zip function k direct list or dictionary te convert korte pari but dictionary te convert korte hole 2 ta value ak shate korte parbo
print(dict(zip(user_id,user_first_name,user_last_name)))
#tai upore dictionary function a convert hobe na
