a=[310,315,275,295,260,270,290,230,255,250]
main=0
for i in range(0,len(a)-1):
    buy=a[i]
    sell=max(a[i+1:])
    profit=sell-buy
    main= max(profit,main)
if(max==0):
    print("No Profit")
else:
    print(main)
