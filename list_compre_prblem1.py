def to_string(li):
    return[str(l) for l in li if (type(l)==int or type(l)==float  )  ]

print(to_string([1,1.4,5,True]))