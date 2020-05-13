even_odd={i:('even' if i%2==0 else'odd') for i in range(1,21)}

for k,v in even_odd.items():
    print(f"{k}={v}")