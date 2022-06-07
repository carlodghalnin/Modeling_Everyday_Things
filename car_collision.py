#Car collision simulation based on page 138 of 
#"Modeling and Simulation of Everyday Things" by Michael Roth.

def car_collision(n_steps=10000000, #Number of steps in simulation
                  n_every=10000,    #Number of steps for new file log entry
                  t_skid=2.0,       #Duration of skidding in s
                  min_v=0.001,      #Minimum velocity for stopping simulation
                  g=9.8,            #Gravitational constant
                  length1=4.0,      #Length of car 1 in m
                  length2=4.5,      #Length of car 2 in m
                  m1=1000.0,        #Mass of car 1 in kg
                  m2=100.0,         #Mass of car 2 in kg
                  dt=0.0001,        #Step time proportion in s
                  m_uk=0.1,         #Coefficient of kinetic friction
                  m_us=0.6,         #Coefficient of static friction
                  cores=1.0,        #Collision objects minus 1
                  x10=50.0,         #Initial position of car 1 in m
                  x20=100.0,        #Initial position of car 2 in m
                  vx10=20.0,        #Initial velocity of car 1 in m/s
                  vx20=4.0,         #Initial velocity of car 2 in m/s
                  ax1=0.0,          #Initial acceleration of car 1 in m/s^2
                  ax2=0.0           #Initial acceleration of car 2 in m/s^2
                  ):
    
    '''
    Simulates rear-end collision between two automobiles incorporating
    friction and akidding.
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
            if (step % n_every) == 0:
                with open('collision.txt','a') as log:
                    log.write(f'''{time}s {x1:.2f}m {x2:.2f}m {vx1:.2f}m/s
                                {vx2:.2f}m/s \n''')
        #Collision occurs
        else:
            t_coll = time
            with open('collision.txt','a') as log:
                log.write(' \n')
                log.write(f'Collision time: {t_coll:.2f}s. \n')
            
            dummy1 = vx1
            dummy2 = vx2
            rat1 = (1.0 + cores)*m2/(m1 + m2)
            rat2 = (1.0 + cores)*m1/(m1 + m2)
            vx1 = dummy1 + rat1*(dummy2 - dummy1)
            vx2 = dummy2 - rat2*(dummy2 - dummy1)

            dummy1 = ax1
            dummy2 = ax2            
            break

    #Post-collision motion updates
    for step in range(n_steps):
        time = t_coll + step*dt
        if time < t_coll + t_skid:
            ax1 = dummy1 - m_uk*g*vx1/abs(vx1)
            ax2 = dummy2 - m_uk*g*vx1/abs(vx2)
        else:
            ax1 = dummy1 - m_us*g*vx1/abs(vx1)
            ax2 = dummy2 - m_us*g*vx1/abs(vx2)

        x1 = x1 + vx1*dt + 0.5*ax1*dt*dt
        vx1 = vx1 + ax1*dt
        x2 = x2 + vx2*dt + 0.5*ax2*dt*dt
        vx2 = vx2 + ax2*dt

        #Terminating simulation below minimum velocity
        if (abs(vx1) <= min_v) or (abs(vx2) <= min_v):
            with open('collision.txt','a') as log:
                log.write(' \n')
                log.write(f'End of skid {time:.2f}s')
            break

        #Logging of post-collision distances and velocities
        if (step % n_every) == 0:
            if time < t_coll + t_skid:
                with open('collision.txt','a') as log:
                    log.write(f'''{time}s {x1:.2f}m {x2:.2f}m {vx1:.2f}m/s
                            {vx2:.2f}m/s coasting \n''')
            else:
                with open('collision.txt','a') as log:
                    log.write(f'''{time}s {x1:.2f}m {x2:.2f}m {vx1:.2f}m/s
                            {vx2:.2f}m/s skidding \n''')
    return None

if __name__ == "__main__":
    car_collision()
