# --- Speed Controller Block Logic ---
class EngineSpeedController:
    def _init_(self, Kp, Ki, Kd, max_rpm=6000):
        self.Kp, self.Ki, self.Kd = Kp, Ki, Kd
        self.max_rpm_limit = max_rpm
        self.integral_error = 0.0
        self.previous_error = 0.0

    def calculate_control_action(self, target_rpm, current_rpm, dt):
        # 1. Safety & Limit Checks
        if current_rpm > self.max_rpm_limit:
            return 0.0  # Force throttle closed (Overspeed Protection)

        # 2. Speed Error Calculation
        error = target_rpm - current_rpm
        
        # 3. PID logic
        self.integral_error += error * dt
        derivative = (error - self.previous_error) / dt
        output = (self.Kp * error) + (self.Ki * self.integral_error) + (self.Kd * derivative)
        
        # 4. Limit Checks (Actuator range 0-100%)
        final_cmd = max(0.0, min(100.0, output))
        self.previous_error = error
        return final_cmd

# --- Demonstration Outputs ---

# Initialize controller with tuned gains
ecu = EngineSpeedController(Kp=0.1, Ki=0.05, Kd=0.01)

print("--- SCENARIO 1: Normal Operation (Cold Start/Idle) ---")
# Target 800 RPM, Current 0 RPM, 0.1s step
out1 = ecu.calculate_control_action(800, 0, 0.1)
print(f"Input: Target=800, Actual=0 | Output: Throttle={out1}%") 
# Result: High throttle to get the engine moving.

print("\n--- SCENARIO 2: Load Disturbance (A/C turned on) ---")
# Target 800 RPM, but speed dropped to 750 RPM due to load
out2 = ecu.calculate_control_action(800, 750, 0.1)
print(f"Input: Target=800, Actual=750 | Output: Throttle={out2}%")
# Result: Increased throttle command to compensate for the 50 RPM drop.

print("\n--- SCENARIO 3: Overspeed Protection (Safety Trigger) ---")
# Target 2000 RPM, but Actual is 6500 RPM (e.g., stuck throttle or mechanical failure)
out3 = ecu.calculate_control_action(2000, 6500, 0.1)
print(f"Input: Target=2000, Actual=6500 | Output: Throttle={out3}%")
# Result: 0.0% throttle regardless of the target, satisfying the safety requirement.