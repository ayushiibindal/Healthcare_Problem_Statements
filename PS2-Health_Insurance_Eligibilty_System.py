# Hospital Health Insurance Eligibility System

print("========== Hospital Health Insurance Eligibility System ==========")

patient_name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
insurance_status = input("Insurance Status (yes/no): ").lower()
policy_status = input("Policy Status (active/expired): ").lower()
treatment_cost = float(input("Enter Estimated Treatment Cost (₹): "))
emergency = input("Is it an Emergency Case? (yes/no): ").lower()

# Insurance Decision
if insurance_status == "yes" and policy_status == "active" and treatment_cost <= 500000:
    approval = "Approved"
    decision = "Patient is eligible for Cashless Treatment."

elif insurance_status == "yes" and policy_status == "active" and treatment_cost <= 1000000:
    approval = "Pending Approval"
    decision = "Additional approval from the insurance company is required."

elif insurance_status == "yes" and policy_status == "expired":
    approval = "Rejected"
    decision = "Insurance policy has expired. Cashless treatment is not available."

elif insurance_status == "no":
    approval = "Not Available"
    decision = "Patient must pay the treatment cost."

else:
    approval = "Invalid"
    decision = "Invalid patient information entered."

# Output
print("\n========== Insurance Report ==========")
print(f"Patient Name      : {patient_name}")
print(f"Insurance Status  : {approval}")
print(f"Approval Status     : {approval}")
print(f"Final Decision    : {decision}")

# Change Request
if age >= 65 and approval == "Approved":
    print(f"Senior Citizen Benefit : Applied")
    print(f"Hospital Discount      : 5% Discount on Hospital Service Charges")

# Additional Enhancement
if emergency == "yes":
    print(f"Emergency Priority : Immediate Processing")

print("\nThank you for using the Hospital Health Insurance Eligibility System!")