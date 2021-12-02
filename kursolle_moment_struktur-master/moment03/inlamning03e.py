loner = (1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000)

print("|{0:^15s}|{1:^15s}|{2:^15s}|{3:^15s}|{4:^15s}|{5:^15s}|{6:^15s}|{7:^15s}|{8:^15s}".format("månadslön", "Årslön", "Landstingsskat", "Kommunalskatt", "Stadsskatt", "Värnskatt", "total skatt", "Skatt(%)", "Total efter skatt"))
for i in loner:
    arslon = i * 12
    if arslon < 19247:
        land = 0
        komunal = 0
        stat = 0
        varn = 0
        tot = land + komunal + stat + varn
        totp = tot/i
        totpeng = i - tot
    if arslon < 468700:
        land = (i/100)*11.48
        komunal = (((i-land)/100)*21.36)
        stat = 0
        varn = 0
        tot = land + komunal + stat + varn
        totp = tot/i
        totpeng = i - tot
    if arslon < 675700:
        land = (i/100)*11.48
        komunal = (((i-land)/100)*21.36)
        stat = ((((i-(land+komunal))/100)*20))
        varn = 0
        tot = land + komunal + stat + varn
        totp = tot/i
        totpeng = i - tot
    if arslon > 675700:
        land = (i/100)*11.48
        komunal = (((i-land)/100)*21.36)
        stat = ((((i-(land+komunal))/100)*20))
        varn = ((((i-(land+komunal+stat))/100)*5))
        tot = land + komunal + stat + varn
        totp = tot/i
        totpeng = i - tot
    print(f"""|{i:^15f}|{arslon:^15f}|{land:^15f}|{komunal:^15f}|{stat:^15f}|{varn:^15f}|{tot:^15f}|{totp:^15f}|{totpeng:^15f}""")