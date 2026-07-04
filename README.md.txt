# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified trading bot built in Python for the Binance Futures Testnet (USDT-M). It allows users to place **Market** and **Limit** orders through a lightweight Streamlit interface while following a clean, modular project structure.

The application validates user input, communicates with the Binance Futures Testnet API, logs all trading activity, and displays detailed order responses.

---

## Features

* Place **Market Orders**
* Place **Limit Orders**
* Support for both **BUY** and **SELL** orders
* Input validation before submitting orders
* Modular code structure
* API request and response logging
* Error handling for invalid inputs, API errors, and network failures
* Lightweight Streamlit user interface

---

## Project Structure

```text
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── logs/
│   └── trading.log
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.10 or later
* Binance Futures Testnet Account
* Binance Testnet API Key
* Binance Testnet Secret Key

---

## Installation

Clone the repository:

```bash
git clone <repository_url>
cd trading_bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key
```

---

## Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## Using the Application

1. Enter the trading symbol (example: `BTCUSDT`).
2. Select the order side (`BUY` or `SELL`).
3. Select the order type (`MARKET` or `LIMIT`).
4. Enter the quantity.
5. If placing a LIMIT order, enter the price.
6. Click **Place Order**.
7. View the order summary and Binance response.

---

## Logging

All API requests, responses, and errors are recorded in:

```text
logs/trading.log
```

The log file includes:

* Timestamp
* Order request details
* Binance API response
* Error messages (if any)

---

## Technologies Used

* Python 3
* Streamlit
* python-binance
* python-dotenv
* Binance Futures Testnet API

---

## Assumptions

* The user has a valid Binance Futures Testnet account.
* Valid API credentials are stored in the `.env` file.
* Internet connectivity is available during execution.
* Orders are placed only on the Binance Futures Testnet and do not involve real funds.

---

## Future Improvements

* Support for additional order types (Stop-Limit, OCO, etc.)
* Display account balance and open positions
* Order history page
* Real-time market price updates
* Improved UI with charts and notifications

---

## Author

Developed as part of a Python Trading Bot assessment using the Binance Futures Testnet.
