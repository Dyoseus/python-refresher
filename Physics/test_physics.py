import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_calculate_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(3, 4), 12)
        self.assertNotEqual(physics.calculate_buoyancy(3, 4), 10)

    def test_calculate_float(self):
        self.assertEqual(physics.will_it_float(3, 4), True)
        self.assertNotEqual(physics.will_it_float(3, 4), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(50), 490500)
        self.assertNotEqual(physics.calculate_pressure(50), 500000)
    
    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(10, 20), 200)
        self.assertNotEqual(physics.calculate_acceleration(10, 20), 201)
    def calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(3,4), 12)
        self.assertEqual(physics.calculate_angular_acceleration(3,4), 14)
    def calculate_torque(self):
        self.assertEqual(physics.calculate_torque(3, 45, 10), 10)
        self.assertNotEqual()
    def calculate_moment_of_inertia(self):



if __name__ == "__main__":
    unittest.main()
