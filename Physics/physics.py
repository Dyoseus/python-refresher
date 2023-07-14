import numpy as np
gravity = 9.81
waterPressure = 1000
pressureAtSurface = 101325

def calculate_buoyancy(density_fluid, volume):
    """Buoyancy is calculated from multiplying density and volume"""
    buoyancy = density_fluid * volume
    return buoyancy

def will_it_float(volume, mass):
    """Mass is multiplied by gravity constant"""
    gravityForce = mass * gravity

    if 1000 * volume > gravityForce:
        return True
    else:
        return False

def calculate_pressure(depth):
    pressure = waterPressure * gravity * depth + pressureAtSurface
    return pressure

def calculate_acceleration(force, mass):
    acceleration = force * mass
    return mass

def calculate_angular_acceleration(tau, I):
    angularAcceleration = tau * I
    return angularAcceleration

def calculate_torque(F_magnitude, F_direction, r):
    torque = F_magnitude * r * np.sin(F_direction)
    return torque

def calculate_moment_of_inertia(mass, r):
    inertia = mass * r**2
    return inertia

def calculate_auv_acceleration(F_magnitude, F_angle, mass):
    F_x = (F_magnitude * np.cos(F_angle)) / mass
    F_y = (F_magnitude * np.sin(F_angle)) / mass
    acceleration = np.sqrt(F_x**2 + F_y**2)
    return acceleration

def calculate_auv_angular_acceleration(F_magnitude, F_angle, inertia = 1, thruster_distance = 0.5):
    F_magnitude * thruster_distance * math.sin(F_angle) / inertia

