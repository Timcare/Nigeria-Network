while True:
        Mtn=('0803','0806','0814','0810','0813','0814','0816','0703','0706','0903','0906')
    
        Mobile=('0809','0817','0818','0908','0909')
    
        Airtel=('0802','0808','0812','0708','0701','0902','0901','0907')
    
        Glo=('0805','0807','0811','0815','0705','0905')
        Smile=('0702')
        Ntel=('0804')
        Visafone=('07025','07026','0704')
        
        print('Enter your mobile Network')
    
        code=input()
        
        if code.isdecimal():
            print(' ')
        else:
            print('You can only use numerical digits')
            continue
            
        if len(code) <11:
            print('Your mobile network must be 11 digits')
            continue
            
        if len(code) > 11:
            print("Your mobile network can't be more than 11 digits")
            continue
                 
        if code.startswith(Mtn):
            print('Your mobile network is mtn')
                
        elif code.startswith(Airtel):
            print('Your mobile network is Airtel')
                
        elif code.startswith(Glo):
            print('Your mobile network is Glo')
                
        elif code.startswith(Smile):
            print('Your mobile network is Smile')
                
        elif code.startswith(Ntel):
            print('Your mobile network is Ntel')
                
        elif code.startswith(Visafone):
            print('Your mobile network is Visafone')
                
        else:
            print('Your mobile network is not available')
        
        print('Do you want to continue press y and any key to exit')
        check=input()
        check=check.lower()
        if check =='y':
            continue
        else:
             break