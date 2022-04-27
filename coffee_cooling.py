#Coffee cooling simulation based on page 67 of 
#"Modeling and Simulation of Everyday Things" by Michael Roth.

def get_cream():
    flag = int(input('''
    Put 1 if no cream added.
    Put 2 if cream added first.
    Put 3 if cream added at 80°C.
    '''))
    
    assert flag in (1, 2, 3)   
    return flag

def coffee_temp(instant=0.0001,
                total_time=1000.0,
                start=100,
                ambient=20,
                stop=70,
                constant=0.0001005,
                flag=1):
    '''
    Uses 4th order Runge-Kutta integrator to simulate cooling of coffee
    over a period of 1000 minutes. Temperatures in degrees Celsius.
    '''
    if flag==2:
        temp = start-5
    else:
        temp = start

    steps = int(total_time/instant) + 1
    for i in range(steps):
        moment = i*instant
        k1 = -constant*(temp-ambient)*instant
        k2 = -constant*(temp+(k1/2.0)-ambient)*instant
        k3 = -constant*(temp+(k2/2.0)-ambient)*instant
        k4 = -constant*(temp+k3-ambient)*instant
        temp = temp+((k1+(2.0*k2)+(2.0*k3)+k4)/6.0)
        #print(f'At {moment/10000} seconds, coffee was {temp}°C.')
        if flag==3 and abs(temp-80.0)<=0.01:
            temp = temp-5.0
        if moment%100==0.0:
            print(f'At {moment/10000} minutes, coffee was {temp}°C.')
        if temp<stop:
            break
    return None

def coffee_cooling():
    initial = float(input('What is the initial coffee temperature? '))

    env = float(input('What is the environmental temperature? '))
    
    final = float(input('What is the final coffee temperature? '))
    assert initial > final
    
    cooling = float(input('What is the cooling constant? '))

    cream = get_cream()
    if cream == 3:
        assert initial >= 80.0

    coffee_temp(start=initial,
                ambient=env,
                stop=final,
                constant=cooling,
                flag=cream)
    return None

if __name__ == "__main__":
    #pass
    coffee_cooling()
