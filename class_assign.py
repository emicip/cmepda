"""
Write a program to explore the properties of a few elementary Particles.
The program must contain a Base class Particle and two Child classes, Proton and Alpha, that inherit from it.
"""
import math

c = 1

class Particle:
    """ Constructor
    """
    def __init__ (self, NAME, MASS, CHARGE, MOMENTUM = 0.):
        self._name = NAME
        if MASS < 0 :
             raise ValueError("Mass value must be greater than 0")
        else:
            self._mass = MASS
        self._charge = CHARGE
        self._momentum = MOMENTUM


    @property
    def name(self):
        return self._name
    
    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def momentum(self):
        return self._momentum
    
    @momentum.setter
    def momentum(self,new_momentum):
        if new_momentum < 0:
            print('Momentum can not inferior to zero')
        else:
            self._momentum = new_momentum
    
    @property
    def energy(self):
        return math.sqrt(self.mass**2 * c**4 + self.momentum**2 * c**2)

    @energy.setter
    def energy(self, new_energy):
        if new_energy < self.mass * c**2:
            raise ValueError('Energy must be greater than the mass')
        else:
            self.momentum = math.sqrt( new_energy**2 * c**2 - self.mass**2 * c**4 )

    def print_particle(self):
        print('The particle is a {}, has a mass of {} MeV, a charge of {}e and a momentum of {} Mev'.format(self.name,self.mass,self.charge, self.momentum))

class proton(Particle):
    """Constructor
    """
    def __init__(self,MOMENTUM):
        Particle.__init__(self, 'proton', 938.272, 1, MOMENTUM)

if __name__ == "__main__":
    v = Particle('electron', 0.511, 1, 40)
    v.print_particle()
    print(v.energy)
    v.momentum = 20
    print(v.momentum)
    p=proton(39)
    print(p.name)
    p.print_particle()
    # print(p.__dict__)

