print("Welcome to Dhruv's Cruptocurrency Converter!")
val=str(input('Enter the output cryptocurrency code:'))

if(val=='BTC'):
    USD=float(input('Enter the amount in USD:'))
    BTC=USD*0.000022
        print('%0.3f USD is equal to %0.3f bitcoin' %(USD, BTC))
elif(val=='ETH'):
    USD=float(input('Enter the amount in USD:'))
    ETH=USD*0.000321
        print('%0.3f USD is equal to %0.3f ethereum' %(USD, ETH))
elif(val=='LTC'):
    USD=float(input('Enter the amount in USD:'))
    LTC=USD*0.0064623264
        print('%0.3f USD is equal to %0.3f litecoin' %(USD, LTC))
elif(val=='ADA'):
    USD=float(input('Enter the amount in USD:'))
    ADA=USD*0.681243
        print('%0.3f USD is equal to %0.3f cardano' %(USD, ADA))
elif(val=='DOGE'):
    USD=float(input('Enter the amount in USD:'))
    DOGE=USD*4.757766
        print('%0.3f USD is equal to %0.3f dogecoin' %(USD, DOGE))
