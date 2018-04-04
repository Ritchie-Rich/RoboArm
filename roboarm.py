from roboarm import Arm

arm = Arm()
arm.led.on(timeout=2)
arm.base.rotate_clock(timeout=2)
arm.base.rotate_counter(timeout=2)
arm.shoulder.down(timeout=2)
arm.shoulder.up(timeout=2)
arm.elbow.down(timeout=2)
arm.elbow.up(timeout=2)
arm.wrist.down(timeout=2)
arm.wrist.up(timeout=2)
arm.grips.open(timeout=1)
arm.grips.close(timeout=1)

arm.led.off(timeout=2)
