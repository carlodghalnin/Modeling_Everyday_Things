from math import pi, cos, sin, sqrt

def baseball_flight(nstepmax=100000,
                    step=0.0001000,
                    g=9.810000,             #Gravitational constant
                    drag_c=0.25,            #Drag constant
                    magnus_c=0.25,          #Magnus constant
                    rho=1.29,               #Air density in kg/m^3
                    m_ball=0.268,           #Ball mass in kg
                    r_ball=0.107            #Ball radius in m
                    ):
    '''
    Simulates trajectory of a hit baseball over a maximum period of 10 seconds.
    Implements gravity, drag force, and magnus effect.
    '''

    d_ball = 3.0*m_ball/(4.0*pi*r_ball**3)  #Density of ball
    a_ball = pi*r_ball**2                   #Area of ball
    
    x = float(input('Initial horizontal position from home plate in meters: '))
    y = float(input('Initial lateral position from home plate in meters: '))
    z = float(input('Initial height from home plate in meters: '))
    xf = float(input('Final horizontal position from home plate in meters: '))

    v = float(input('Initial ball speed in meters per second: '))
    theta = float(input('Initial pitch angle above horizontal in degrees: '))
    vx=v*cos(theta*pi/180.0)                #Horizontal velocity
    vy=0.0                                  #Lateral velocity
    vz=v*sin(theta*pi/180.0)                #Vertical velocity

    bdrag = input('Enter 1 if drag present, nothing otherwise: ')
    if not bdrag:
        drag_c = 0.0
    
    bspin = input('Enter 1 if spin present, nothing otherwise: ')
    if not bspin:
        magnus_c = 0.0
        wx = 0.0                            #Forward angular velocity
        wy = 0.0                            #Lateral angular velocity
        wz = 0.0                            #Vertical angular velocity
    else:
        wx = float(input('Enter x angular velocity in revols/second: '))*2.0*pi
        wy = float(input('Enter y angular velocity in revols/second: '))*2.0*pi
        wz = float(input('Enter z angular velocity in revols/second: '))*2.0*pi

    bwrite = input('Enter 1 to write trajectory to file, nothing otherwise: ')

    for n in range(nstepmax):
        time = n*step

        #Calculate speed and acceleration
        vx_old = vx
        vy_old = vy
        vz_old = vz
        v = sqrt(vx**2 + vy**2 + vz**2)

        ax = -0.5*drag_c*rho*a_ball*v*vx \
             + 0.5*magnus_c*rho*a_ball*(wy*vz - wz*vy)
        ay = -0.5*drag_c*rho*a_ball*v*vy \
             + 0.5*magnus_c*rho*a_ball*(wz*vx - wx*vz)
        az = -0.5*drag_c*rho*a_ball*v*vz \
             + 0.5*magnus_c*rho*a_ball*(wx*vy - wy*vx) \
             + (rho*r_ball-1.00)*g

        #Update velocities and positions
        vx = vx + ax*step
        vy = vy + ay*step
        vz = vz + az*step

        x = x + 0.5*(vx_old + vx)*step
        y = y + 0.5*(vy_old + vy)*step
        z = z + 0.5*(vz_old + vz)*step

        if bwrite and time in range(10):
            with open('baseball.txt','a') as log:
                log.write(f'At {time}s, baseball was at {x,y,z}m. \n')

        if x > xf:
            with open('baseball.txt','a') as log:
                log.write(f'Final time {time}s. \n')
                log.write(f'Final position {x,y,z}m. \n')
                log.write(f'Final velocity {vx,vy,vz}m. \n')
            break

    return None

if __name__ == "__main__":
    baseball_flight()
