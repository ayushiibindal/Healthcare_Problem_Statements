# Healthcare Patient Risk Assessment System

print("========== Healthcare Patient Risk Assessment System ==========")

patient_name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
temperature = float(input("Enter Body Temperature (°C): "))
heart_rate = int(input("Enter Heart Rate (BPM): "))
oxygen = int(input("Enter Oxygen Saturation (SpO2): "))

# Risk Assessment
if oxygen < 90 or temperature > 40:
    risk = "Critical"
    recommendation = "Immediately transfer the patient to ICU."

elif (90 <= oxygen <= 94) or (38 <= temperature <= 40):
    risk = "High"
    recommendation = "Doctor consultation and hospital admission required."

elif heart_rate > 100 or age > 60:
    risk = "Medium"
    recommendation = "Keep the patient under observation."

else:
    risk = "Low"
    recommendation = "Patient is healthy and can go home after consultation."

# Output
print("\n========== Patient Report ==========")
print(f"Patient Name      : {patient_name}")
print(f"Patient Age       : {age}")
print(f"Temperature       : {temperature} °C")
print(f"Heart Rate        : {heart_rate} BPM")
print(f"Oxygen Level      : {oxygen}%")
print(f"Risk Level        : {risk}")
print(f"Recommendation    : {recommendation}")

# Change Request
if age >= 75:
    print(f"Senior Citizen    : Yes")
    print(f"Priority status   : Priority Consultation Required")

# Additional Enhancement
if heart_rate < 60 or heart_rate > 120:
    print(f"Health Alert      : Abnormal Heart Rate Detected")

print("\nThank you for using the Healthcare Patient Risk Assessment System!")