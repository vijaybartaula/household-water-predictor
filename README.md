# Household Water Usage Predictor

A linear regression model that predicts daily household water consumption based on the number of residents.

## Overview

This project demonstrates how to build, train, and visualize a simple linear regression model that estimates daily water usage in liters based on household size. The model can help water resource planners, environmentalists, and homeowners make data-driven decisions about water consumption.

## Features

- **Data Flexibility**: Choose between sample data or synthetic data generation
- **Linear Regression Model**: Implements scikit-learn's LinearRegression for prediction
- **Visualization**: Includes data plotting with regression line
- **Easy Prediction**: Simply input the number of residents to get estimated water usage

## Requirements

- Python 3.6+
- pandas
- numpy
- matplotlib
- scikit-learn

## Installation

```bash
# Clone the repository
git clone https://github.com/vijaybartaula/household-water-predictor.git
cd household-water-usage-predictor

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pandas numpy matplotlib scikit-learn
```

## Usage

Run the Jupyter notebook to:
1. Import necessary libraries
2. Choose your data source (sample or synthetic)
3. Train the linear regression model
4. Make predictions
5. Visualize results

### Data Options

#### Option 1: Sample Data
Uses manually specified sample data:
```python
df = df_sample  # Uncomment this line to use sample data
```

#### Option 2: Synthetic Data
Generates random data with realistic parameters:
```python
df = df_generated  # Uncomment this line to use generated data
```

### Making Predictions

```python
# Predict water usage for a given number of residents
residents_input = 8  # Example: 8 residents in the household
predicted_usage = model.predict([[residents_input]])[0]
print(f"Predicted Daily Water Usage for {residents_input} residents: {predicted_usage:.0f} liters")
```

## Example Output

When run with the provided code, you can expect:

- A trained linear regression model with equation: `Water Usage = [slope] * Residents + [intercept]`
- A scatter plot showing the relationship between household size and water usage
- A prediction line visualizing the model's estimates
- Sample predictions for specified household sizes

## Model Interpretation

The linear regression equation has the form:
```
Water Usage = [slope] * Residents + [intercept]
```

Where:
- **Slope**: Represents the average increase in water usage (in liters) for each additional resident
- **Intercept**: Baseline water usage (in liters) regardless of household size

## Customization

- Adjust the `generate_water_data()` function to change assumptions about per-person water usage
- Modify visualization parameters for different plot styles
- Add additional features beyond just household size for multivariate regression

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
