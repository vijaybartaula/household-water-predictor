import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ----------------------------
# Generate Synthetic Data
# ----------------------------
def generate_water_data():
    np.random.seed(42)
    residents = np.random.randint(1, 15, 100)  # Random number of residents between 1 and 15
    # Default assumption: 75 liters per person per day with variability
    usage = residents * np.random.normal(75, 10, 100)  # Use 75 liters per person with some noise (std deviation of 10)
    usage = np.clip(usage, 30, 1000)  # Ensure realistic values (clip outliers)
    return pd.DataFrame({"Residents": residents, "WaterUsage_Liters": usage})

df = generate_water_data()

# ----------------------------
# Train Linear Regression Model
# ----------------------------
X = df[["Residents"]]
y = df["WaterUsage_Liters"]
model = LinearRegression()
model.fit(X, y)

# ----------------------------
# Streamlit App Interface
# ----------------------------
st.title("Daily Household Water Usage Estimator")

st.markdown("""
This tool estimates your household's total daily water consumption based on the number of residents.  
It encourages water conservation and assists with better resource management for both households and cities.
""")

# User input
residents_input = st.slider("Number of Residents in Household", 1, 15, 4)

# Predict water usage
predicted_usage = model.predict([[residents_input]])[0]
st.subheader(f"Estimated Daily Water Usage: {predicted_usage:.0f} liters")

# ----------------------------
# Conservation Suggestions
# ----------------------------
st.markdown("### Water Conservation Recommendations")

# Check for the different ranges of residents input
if residents_input == 1 or residents_input == 2:
    st.info("With just 1 or 2 people, you’re using less water overall, but there are still great ways to reduce your footprint!")
elif residents_input >= 3 and residents_input <= 4:
    st.info("With 3 to 4 residents, you're still using a moderate amount of water. Consider these conservation tips.")
elif residents_input >= 5 and residents_input <= 6:
    st.info("A household with 5 to 6 people tends to use more water. Try some of these strategies to conserve water.")
elif residents_input >= 7 and residents_input <= 10:
    st.info("With 7 to 10 residents, water use increases. Implementing conservation methods here can have a significant impact.")
elif residents_input >= 11 and residents_input <= 12:
    st.info("For households with 11 to 12 residents, it's crucial to adopt large-scale water-saving methods.")
else:
    st.info("With more than 13 residents, conserving water becomes even more important to reduce environmental impact. Consider advanced strategies.")

# More suggestions for per-person usage
if predicted_usage / residents_input > 75:
    st.info("Per-person usage exceeds recommended limits. Consider the following strategies to reduce your water footprint:")
    st.markdown("""
    - **Shorten showers**: Reducing shower time can save gallons of water each day.
    - **Turn off the tap** when brushing teeth, washing dishes, or doing other activities.
    - **Fix leaks**: Even small drips can add up to hundreds of liters over time.
    """)
else:
    st.success("Your water usage is within a typical range. Keep practicing good water-saving habits.")

# ----------------------------
# Equation, Water Usage & Sample Data
# ----------------------------

# Show Equation
if st.checkbox("Show Equation"):
    st.markdown("#### Linear Regression Equation")
    coef = model.coef_[0]
    intercept = model.intercept_
    equation = f"Water Usage (liters) = {coef:.2f} * Residents + {intercept:.2f}"
    st.latex(f"\\text{{Water Usage}} = {coef:.2f} \\times \\text{{Residents}} + {intercept:.2f}")

# Show Water Usage
st.subheader(f"Predicted Daily Water Usage for {residents_input} Residents: {predicted_usage:.0f} liters")

# Show Sample Data
if st.checkbox("Show Sample Data"):
    st.dataframe(df.head(10))

# ----------------------------
# Show Plot of Water Usage
# ----------------------------
if st.checkbox("Show Water Usage Chart"):
    fig, ax = plt.subplots()
    ax.scatter(df["Residents"], df["WaterUsage_Liters"], alpha=0.6, label="Simulated Data")
    x_vals = np.arange(1, 16).reshape(-1, 1)
    y_vals = model.predict(x_vals)
    ax.plot(x_vals, y_vals, color='blue', linewidth=2, label="Prediction Line")
    ax.set_xlabel("Number of Residents")
    ax.set_ylabel("Estimated Water Usage (Liters per Day)")
    ax.set_title("Household Size vs. Daily Water Usage")
    ax.legend()
    st.pyplot(fig)

# ----------------------------
# Additional Tips for Water Conservation
# ----------------------------
st.markdown("### Additional Water Conservation Tips")

# Bathroom Tips
st.markdown("#### Bathroom")
st.markdown("""
- **Install a low-flow toilet**: High-efficiency toilets use 1.28 gallons per flush, compared to older models that use 3.5 to 7 gallons.
- **Install a low-flow showerhead**: Reduces water flow without sacrificing pressure.
- **Take shorter showers**: Reducing shower time by even a few minutes can save gallons of water.
- **Turn off water while brushing teeth**: This can save 3-5 gallons per minute.
""")

# Kitchen Tips
st.markdown("#### Kitchen")
st.markdown("""
- **Use a dishwasher only when full**: Dishwashers use less water than washing by hand if they are fully loaded.
- **Rinse fruits and vegetables in a bowl of water**: Instead of running the tap.
- **Use a water-saving faucet aerator**: Install aerators on kitchen faucets to reduce water flow without reducing performance.
- **Defrost food in the fridge or microwave**: Avoid running water over frozen food to defrost it.
""")

# Laundry Tips
st.markdown("#### Laundry")
st.markdown("""
- **Wash clothes in cold water**: This saves both water and energy.
- **Wash full loads**: Ensure the washing machine is full to maximize water use.
- **Use a high-efficiency washing machine**: These machines use significantly less water than traditional models.
""")

# Garden & Lawn Tips
st.markdown("#### Garden & Lawn")
st.markdown("""
- **Water plants early in the morning**: Watering in the morning minimizes evaporation.
- **Install a drip irrigation system**: Drip irrigation uses 30-50% less water than traditional sprinklers.
- **Use drought-resistant plants**: These plants require less water and are more resilient in dry conditions.
- **Mulch your garden**: Mulching helps retain soil moisture and reduces the need for frequent watering.
""")

# Home Maintenance Tips
st.markdown("#### Home Maintenance")
st.markdown("""
- **Fix leaks immediately**: A small drip from a leaking faucet can waste 20 gallons of water or more each day.
- **Install water-efficient appliances**: Consider washing machines, dishwashers, and refrigerators that are designed to use less water.
- **Insulate pipes**: Prevent water waste by ensuring water is at the right temperature immediately after turning on the faucet.
""")

# ----------------------------
# More Impactful Suggestions for Household Sizes Above 9 Residents
# ----------------------------
if residents_input > 9:
    st.markdown("### Large Household Water Conservation Strategies")
    st.warning("Households with more than 9 residents tend to have a significant impact on local water resources.")
    st.markdown("""
    With larger households, conserving water becomes even more crucial to ensure sustainable water use. Consider these impactful strategies:
    
    - **Efficient Water Use Planning**: Large households can implement a detailed plan to monitor and reduce water usage.
      - **Example**: Use a weekly checklist to track water use, and designate one person to oversee this effort.
    
    - **Greywater Recycling**: For larger households, consider a greywater recycling system to reuse water from baths, sinks, and washing machines.
      - **Example**: Install a system that collects greywater and reuses it for toilet flushing and irrigation.
    
    - **Water-Efficient Landscaping**: Consider xeriscaping your yard (landscaping that reduces or eliminates the need for irrigation).
      - **Example**: Replace grass lawns with native plants that require minimal water.
    
    - **Educate and Encourage Family Members**: Everyone in a large household must be aware of the importance of water conservation and be motivated to participate.
      - **Example**: Set up a monthly family challenge to reduce water usage and track progress together.

    - **Water-Saving Appliances for Larger Loads**: Choose appliances that are designed to handle large families but still conserve water, like high-efficiency dishwashers and washing machines.
      - **Example**: A family of 10 using a water-efficient dishwasher can save hundreds of liters each week compared to using a less efficient model.

    **Remember**: Every small change can add up to substantial water savings over time, especially in large households.
    """)
