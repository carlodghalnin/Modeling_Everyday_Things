#Car collision simulation based on page 138 of 
#"Modeling and Simulation of Everyday Things" by Michael Roth.

def car_collision(n_steps=10000000,
                  n_every=1000000,  #Number of steps for new file log entry
                  t_skid=2.0,       #Duration of skidding in s
                  g=9.8,            #Gravitational constant
                  length1=4.0,      #Length of car 1 in m
                  length2=4.5,      #Length of car 2 in m
                  m1=1000.0,        #Mass of car 1 in kg
                  m2=100.0,         #Mass of car 2 in kg
                  dt=0.0001,        #Step time proportion in s
                  m_uk=0.1,
                  m_us=0.6,
                  cores=1.0,
                  x10=50.0,         #Initial position of car 1 in m
                  x20=100.0,        #Initial position of car 2 in m
                  vx10=20.0,        #Initial velocity of car 1 in m/s
                  vx20=4.0,         #Initial velocity of car 2 in m/s
                  ax1=0.0,          #Initial acceleration of car 1 in m/s^2
                  ax2=0.0           #Initial acceleration of car 2 in m/s^2
                  ):
    
    '''
    '''
    
    #Initialize
    x1 = x10
    vx1 = vx10
    x2 = x20
    vx2 = vx20    

    for step in range(n_steps):
        #Pre-collision motion updates
        if (x2 - x1) > (0.5*(length1 + length2)):
            time = step*dt
            x1 = x1 + vx1*dt + 0.5*ax1*dt*dt
            vx1 = vx1 + ax1*dt
            x2 = x2 + vx2*dt + 0.5*ax2*dt*dt
            vx2 = vx2 + ax2*dt
            if float(step/n_every) == (float(step)/float(n_every)):
                with open('collision.txt','a') as log:
                    log.write(f'{time}s {x1}m {x2}m {vx1}m/s {vx2}m/s \n')
        #Collision occurs
        else:
            t_coll = time
            with open('collision.txt','a') as log:
                log.write(' \n')
                log.write(f'Collision time: {t_coll}s. \n')
            
            dummy1 = vx1
            dummy2 = vx2
            rat1 = (1.0 + cores)*m2/(m1 + m2)
            rat2 = (1.0 + cores)*m1/(m1 + m2)
            vx1 = dummy1 + rat1*(dummy2 - dummy1)
            vx2 = dummy2 - rat2*(dummy2 - dummy1)

            dummy1 = ax1
            dummy2 = ax2            
            break

    #for step in range(n_steps):
    return None

if __name__ == "__main__":
    car_collision()
