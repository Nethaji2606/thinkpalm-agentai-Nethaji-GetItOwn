import pandas as pd
import math

def calculate_emi(p, r, n):
    # p = principal, r = monthly interest rate, n = months
    r = r / (12 * 100) # Convert annual % to monthly decimal
    emi = p * r * (math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)
    return round(emi)

def bike_assistant():
    # Simulated data - In a real scenario, you'd use a scraper or API here
    bikes = {
        "Royal Enfield Classic 350": {"price": 193000, "cc": 349, "mileage": 35},
        "Yamaha R15 V4": {"price": 182000, "cc": 155, "mileage": 45},
        "KTM Duke 390": {"price": 311000, "cc": 399, "mileage": 28},
        "Yamaha RX100": {"price": 225000, "cc": 100, "mileage": 25},
        "Bajaj Pulsar NS200": {"price": 250000, "cc": 200, "mileage": 45},
        "TVS Apache RR310": {"price": 360000, "cc": 310, "mileage": 32}
    }

    print("Available Bikes:", list(bikes.keys()))
    name = input("\nEnter Bike Name: ")

    if name in bikes:
        details = bikes[name]
        price = details['price']
        print(f"\n--- {name} Specifications ---")
        print(f"Ex-Showroom Price: ₹{price:,}")
        print(f"Engine: {details['cc']}cc | Mileage: {details['mileage']} kmpl")

        down_payment = float(input("\nEnter Down Payment Amount (₹): "))
        loan_amount = price - down_payment
        interest_rate = 10.0 # Default as requested

        tenures = [3, 6, 9, 12, 36, 60]
        emi_results = []

        for months in tenures:
            monthly_payment = calculate_emi(loan_amount, interest_rate, months)
            total_payable = monthly_payment * months
            emi_results.append({
                "Tenure (Months)": months,
                "Monthly EMI": f"₹{monthly_payment:,}",
                "Total Interest": f"₹{round(total_payable - loan_amount):,}",
                "Total Amount": f"₹{round(total_payable):,}"
            })

        df = pd.DataFrame(emi_results)
        print(f"\nEMI Breakdown (Interest Rate: {interest_rate}%):")
        return df
    else:
        print("Bike details not found.")

# Run the assistant
bike_assistant()
