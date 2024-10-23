import wpilib
from commands2 import CommandScheduler
from subsystems.drivetrain import Drivetrain
from commands.autonomous import AutonomousCommand
from commands.teleop import TeleopCommand

class Robot(wpilib.TimedRobot):
    
    def robotInit(self):
        """Robot-wide initialization code should go here."""
        # Instantiate subsystems
        self.drivetrain = Drivetrain()
        
        # Instantiate default commands
        self.teleopCommand = TeleopCommand(self.drivetrain)
        self.autonomousCommand = AutonomousCommand(self.drivetrain)
        
        # Start Command Scheduler
        CommandScheduler.getInstance().registerSubsystem(self.drivetrain)

    def robotPeriodic(self):
        """Periodic code for all modes goes here."""
        CommandScheduler.getInstance().run()

    def autonomousInit(self):
        """Runs once when autonomous mode is enabled."""
        if self.autonomousCommand:
            self.autonomousCommand.schedule()

    def teleopInit(self):
        """Runs once when teleop mode is enabled."""
        if self.teleopCommand:
            self.teleopCommand.schedule()

    def disabledInit(self):
        """Runs once when the robot is disabled."""
        CommandScheduler.getInstance().cancelAll()

