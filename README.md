# Golf ball trajectory generator

__Guillaume Marmorat__

Electron app to provide a simple interface to simulate golf ball trajectory through time.

Require __node__ and __npm__

Just install by :

```bash
  npm install
```

And tentatively run with :

```bash
  npm run
```
---

### Source

[Wolfram Demonstration](http://demonstrations.wolfram.com/FlightOfAGolfBall/)
[Flight Trajectory of a Golf Ball for a Realistic Game](http://www.ijimt.org/papers/419-D0260.pdf)
[A Comparative Study of Golf Ball Aerodynamics ](https://people.eng.unimelb.edu.au/imarusic/proceedings/17/176_Paper.pdf)

### Form

Calculate at time t coordinate, where :
* Cl : lift coefficient
* Cd : drag coefficient
* {wx,wy,wz} spin on axis
* p : 1.205 , air density
* g : 9.81 , gravity
* m : 0.0458 mass of a golf ball
* A : pi * (d/2)^2 area of a golf ball
* v : initial velocity
* d : 1.62 * 0.0254

\
*Coordinate through time*

    m y''(t) = -Cl(wx * z'(t) - wy * x'(t)) - 0.5 * A * Cd * p * y'(t)^2 + g * (-m)  
    m x''(t) = Cl(wz * y'(t) - wy * z'(t)) - 0.5 * A * Cd * p * x'(t)^2  
    m z''(t) = Cl(wx * y'(t) - wy * x'(t)) - 0.5 * A * Cd * p * z'(t)^2  

> Where x', y' and z' previous values of each

*Lift Force*

    Fl = 1/2 * Cl * p * A * v^2

*Drag Force*

    Fd = 1/2 * Cd * p * A * v^2
