# SkySpark
Deals with Building energy data for the UBC Vancouver Campus

## Project Summary
This repository collects and processes real-time building energy & weather data for the UBC Live project. It ingests API data from SkySpark, cleans and transforms the data, and makes it available for analysis.

## Usage Instructions

### 1. Clone this repository
```
git clone https://github.com/UBC-Live/SkySpark.git
cd SkySpark
```

### 2. Create virtual environment and install dependencies

**Create and activate virtual environment:**
```
python3 -m venv venv
source venv/bin/activate
```

**To deactivate it:**
``` 
deactivate 
```

**Installing dependencies:**
```
pip install -r requirements.txt
```

### 3. Configure environment
**Copy `.env.example` to `.env` and add your SkySpark API key**

**Important:**
- **Never** push your `.env` file
- **Ensure** it's in `.gitignore`