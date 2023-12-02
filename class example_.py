class exampleElement:
    def __init__(self, atomic, mass):
        self.atomic = atomic  
        self.mass = mass  

    def exampleCalc(atomic, mass):
        return mass - atomic

example = exampleElement(atomic=20, mass=40)

neutron = example.example(exampleElement.atomic, exampleElement.mass)

print(f"Number of neutrons: {neutron}")
