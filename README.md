# SmartAdvisorMT5

Advisory application for analyzing financial markets that provides 
clear transaction signals based on expert systems, data aggregation methods 
and fuzzy logic. Historical financial data used by the application comes from 
the MetaTrader 5 trading platform.

# Table of content

- [Used technologies and applications](#used-technologies-and-applications)
- [Project setup](#project-setup)
- [Application appearance](#application-appearance)
- [Manual](#manual)

# Used technologies and applications

1. Programing language:
    - Python 3.12


2. Main libraries:
    - PyQt6 - used to create a graphical interface.
    - NumPy - used for numerical calculations and optimization.
    - Pandas - used to work with stock market data.
    - Matplotlib - used to create static charts.
    - Plotly - used to create an interactive candlestick chart.
    - SQLite3 - used to work with the database.
    - Argon2 - used to hash passwords in the database.
    - PyOTP - used to generate one-time identification codes.


3. Used programs:
    - Qt Designer - program was used when creating the graphical interface.
    - GIMP - program used to create application graphics.
    - DB Browser - program used when working with the database.
    - Google Authenticator - program used to store two-factor login keys.
    - MetaTrade 5 - investment platform used to download data and open trading positions.

# Project setup

1. Download and install interpreter for `Python 3.12` from: `https://www.python.org/downloads/`.

2. Clone git repository using following command:

```bash
  https://github.com/gabrielkomor/SmartAdvisorMT5.git
```

3. Enter into `.\SmartAdvisorMT5\` directory.

4. Create virtual environment for Python using command below:

```bash
  py -3.12 -m venv .venv
```

5. Install required libraries (after virtual venv activation):

```bash
  pip install -r .\requirements.txt
```

6. Run application:

```bash
  python main.py
```

or

- Using IDE (for PyCharm you can use `Shift + F10` keyboard shortcut)

## Tips

- If you want to run only the main application window without logging in first, 
uncomment the following line in the main.py file: `run_app()`.

- If you want to run the entire application, including its login system, 
uncomment the following program line in the main.py file: `run_main()`. Additionally, 
this operation requires the correct creation of an environment file, instructions on how to do it correctly are below:

### How to correctly fill environment file:

1. Create `.env` file in `.\SmartAdvisorMT5` directory next to `./env-example` file.
2. Copy the contents of the file `.env-example` into `.env` file.
3. Replace the sample values with real data.

# Application appearance
# Manual
