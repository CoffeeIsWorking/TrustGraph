u = int(input("How many squares you want:"))
z = u%2
j = (2*u)-1
larper=""
while z== 0:
    print("Please enter an odd number of squares.")
    u = int(input("How many squares you want:"))
    if z == u%2:
        continue
    else:
        break
for k in range (0,u+1):
    if k!=(u-1) and k!=(u):
        for h in range (u,abs(u-k-1),-1):
            larper+=str(h)
            larper+=" "
        for y in range (abs(((2*u)-(2*k)-3))):
            larper+=str(u-k)
            larper+=" "
        for h in range (abs(u-k),u+1):
            larper+=str(h)
            larper+=" "
        larper += "\n"
    elif k==(u-1):
        for h in range (u,abs(u-k-1),-1):
            larper+=str(h)
            larper+=" "
        for y in range (abs(((2*u)-(2*k)-2))):
            larper+=str(u-k)
            larper+=" "
        for h in range (abs(u-k+1),u+1):
            larper+=str(h)
            larper+=" "
        larper += "\n"
for k in range (u,-1,-1):
    if k!=(u-1) and k!=(u):
        for h in range (u,abs(u-k-1),-1):
            larper+=str(h )
            larper+=" "
        for y in range (abs(((2*u)-(2*k)-3))):
            larper+=str(u-k)
            larper+=" "
        for h in range (abs(u-k),u+1):
            larper+=str(h)
            larper+=" "
        larper += "\n"

        
print(larper)
