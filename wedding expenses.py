lunch=int(input("enter the cost"))
breakfast=lunch//2
hall=lunch//3
decorations=hall//2
parking=hall//10
groom=lunch+breakfast+hall+decorations+parking
bride=50000
total=groom*2
if(bride==groom):
    print("loan not taken")
else:
    bride=groom-bride
    print(bride)
    print("loan has taken")
    