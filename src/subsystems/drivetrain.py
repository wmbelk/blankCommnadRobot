import wpilib
from commands2 import Subsystem
...

class Drivetrain(Subsystem):
    
    def __init__(self):
        super().__init__()
        # Initialize drivetrain motors here
        self.left_motor = wpilib.Talon(0)
        self.right_motor = wpilib.Talon(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        
    def drive(self, speed, rotation):
        self.drive.arcadeDrive(speed, rotation)
