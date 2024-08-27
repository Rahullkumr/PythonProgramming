
# 12.wap to pair values of both dictionary

d={"apple":45,"mango":67,"cherry":90,"berry":23}

p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}

for i in zip(d.values(), p.values()):
    print(i)