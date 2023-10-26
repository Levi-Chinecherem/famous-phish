Phishing Attack Simulator

![Phishing Attack Simulator Logo](images/logo.png)

The Phishing Attack Simulator is a web-based application that allows users to simulate and detect phishing attacks, smishing (SMS phishing) attempts, pharming attacks, and CEO fraud emails. This README provides detailed information about the system, its features, installation, and usage.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Custom Admin Dashboard](#custom-admin-dashboard)
- [Contributing](#contributing)
- [License](#license)

## Features

- Simulate Phishing Attacks: The system allows you to simulate phishing attacks by entering user input containing phishing keywords.
- Simulate Smishing Attacks: Simulate SMS phishing (smishing) attacks by entering SMS messages.
- Simulate Pharming Attacks: Simulate pharming attacks by checking URLs for fraudulent websites.
- Simulate CEO Fraud: Simulate CEO fraud attempts by entering email messages.

## Requirements

- Python 3.x
- Django
- pandas
- Matplotlib
- Other dependencies (check requirements.txt)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/phishing-attack-simulator.git
   ```
2. Create a virtual environment (recommended) and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations to set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser account to access the admin panel:

   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:

   ```bash
   python manage.py runserver
   ```

The system will be accessible at `http://127.0.0.1:8000/`.

## Usage

### Simulating Phishing Attacks

1. Access the Phishing Simulator by visiting `http://127.0.0.1:8000/phishing_attempt/` in your web browser.
2. Enter user input that may contain phishing keywords.
3. Submit the form to simulate a phishing attack. You'll receive a success or failure message based on the keywords entered.

![Phishing Simulator Screenshot](images/phishing_simulator.png)

### Simulating Smishing Attacks

1. Access the Smishing Simulator by visiting `http://127.0.0.1:8000/smishing/` in your web browser.
2. Enter an SMS message that may contain smishing keywords.
3. Submit the form to simulate a smishing attack and receive a success or failure message.

![Smishing Simulator Screenshot](images/smishing_simulator.png)

### Simulating Pharming Attacks

1. Access the Pharming Simulator by visiting `http://127.0.0.1:8000/pharming/` in your web browser.
2. Enter a URL that may be a fraudulent website.
3. Submit the form to simulate a pharming attack and receive a success or failure message.

![Pharming Simulator Screenshot](images/pharming_simulator.png)

### Simulating CEO Fraud

1. Access the CEO Fraud Simulator by visiting `http://127.0.0.1:8000/ceo_fraud/` in your web browser.
2. Enter an email message that may indicate CEO fraud.
3. Submit the form to simulate a CEO fraud attempt and receive a success or failure message.

![CEO Fraud Simulator Screenshot](images/ceo_fraud_simulator.png)

## Custom Admin Dashboard

The system includes a custom admin dashboard for administrators to monitor and visualize phishing attempts. It provides the following charts:

- Bar chart showing attacks by count and type.
- Bar chart showing the top 10 IP addresses with the highest attack count.
- Pie chart showing the success vs. failure ratio for all attacks.

![Custom Admin Dashboard Screenshot](images/admin_dashboard.png)

## Contributing

Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

Please ensure your code follows best practices and include test cases if applicable.

## License

This project is licensed under the [MIT License](LICENSE).

© 2023 Levi Chinecherem C.
