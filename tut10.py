d= {"me":"my","he":"his","she":"her","i":{"single":"me","plural":"we"}}
print(d)
print(d["me"])# also print(d.get("me"))
print(d["i"])
print(d["i"]["single"])
d["they"]="them"#also d.update({"they":"them"})
print(d)
del d["they"]
print(d)
d2=d.copy()#d2 is now a copy of d. Any change to d2 will not change d.
"d2=d"           # But if d2=d then any change to d2 will change d as both are the same things
print(d.keys())
print(d.values())
print(d.items())
