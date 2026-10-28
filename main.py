# Stage 1: F1 Lap Time Tracker

def calculate_average(lap_times: list) -> float:
    # Prevent a division by zero error if the user exits without entering any laps
    if len(lap_times) == 0:
        return 0.0
    return sum(lap_times) / len(lap_times)

def main():
    print("--- F1 Lap Time Tracker ---")
    laps = []
    
    # Use an infinite loop to continually prompt the user until they type 'done'
    while True:
        user_input = input("Enter lap time in seconds (or 'done' to finish): ").strip()
        
        # Check for the exit condition before attempting any math operations
        if user_input.lower() == 'done':
            break
        
        # Convert the text input into a decimal number for calculations
        lap_time = float(user_input)
        laps.append(lap_time)
        print(f"Recorded: {lap_time}s")
    
    # Display the final analytics only if data was actually collected
    if len(laps) > 0:
        print("\n--- Session Summary ---")
        print(f"Total Laps: {len(laps)}")
        print(f"Fastest Lap: {min(laps):.2f}s")
        print(f"Average Lap: {calculate_average(laps):.2f}s")
    else:
        print("No laps recorded.")

if __name__ == "__main__":
    main()