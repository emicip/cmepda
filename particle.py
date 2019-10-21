import math

speed_of_light = 1.

class Particle:
    """ Class constructor """
    def __init__ (self,name,mass,charge,momentum=0.):
        self.name = name
        self._mass = mass #in MeV
        self._charge = charge #in e
        self.momentum = momentum #in MeV/c

    def print_properties(self):
        print(f'{self.name} has a mass of {self.mass} MeV, a charge of {self.charge} e and a momentum {self.momentum} MeV/c')

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
    def momentum(self,new_value):
        if (new_value<0.):
            print('Cannot set a momentum to a value inferior to 0')
        else:
            self._momentum=new_value
   
    @property
    def energy(self):
        """ Return the energy of the particle in MeV/c^2"""
        return math.sqrt(self.momentum**2*speed_of_light**2+ self._mass**2*speed_of_light**4)


if __name__ == "__main__":
    particella=Particle('Electron',0.511,1,0.1)
    particella.print_properties()
    particella.momentum=-4