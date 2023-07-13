class Physics:
    """def __init__(self, waterPressure, volume, gravity, depth):
    self.waterPressure = waterPressure
    self.volume = volume
    self.gravity = gravity
    self.depth = depth"""

    def calculate_buoyancy(density_fluid, volume):
        buoyancy = density_fluid * volume
        return buoyancy

    def will_it_float(volume, mass):
        gravityForce = mass * 9.81

        if 1000 * volume > gravityForce:
            return True
        else:
            return False

    def calculate_pressure(depth):
        waterPressure = 1000
        gravity = 9.81
        pressure = waterPressure * gravity * depth
        return pressure
