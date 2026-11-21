print("EMAIL RISK ANALYZER")

email = input("Enter your email message: ")

email = email.lower()

score = 0

urgent_words = ["urgent", "immediately", "act now",
                "account blocked", "verify now"]

sensitive_words = ["password", "otp", "bank details",
                   "credit card", "pin"]

for word in urgent_words:
    if word in email:
        score += 1
        print("Warning: Urgent request detected!")

for word in sensitive_words:
    if word in email:
        score += 2
        print("Warning: Sensitive information requested!")

if "http://" in email or "https://" in email:
    score += 2
    print("Warning: Link detected in email!")

print("\n--- EMAIL RISK REPORT ---")

if score >= 4:
    print("Risk Level: HIGH")
    print("This email looks suspicious!")

elif score >= 2:
    print("Risk Level: MEDIUM")
    print("Be careful before responding.")

else:
    print("Risk Level: LOW")
    print("No major warning signs detected.")

print("Risk Score:", score)
