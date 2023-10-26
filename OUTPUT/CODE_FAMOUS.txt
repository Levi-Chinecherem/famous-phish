from django.shortcuts import render
from .models import PhishingAttempt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64

def home(request):
    return render(request, 'home.html')

def phishing_attempt(request):
    if request.method == 'POST':
        # Assume you have a form that captures user input (e.g., username and password)
        user_input = request.POST.get('user_input', '')

        # Simulate a basic phishing check
        if "phishing keyword" in user_input:
            # Log the phishing attempt with the attack type "Phishing"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=True,
                attack_type="Phishing",
            )
            # Render a template indicating a successful phishing attempt
            return render(request, 'phishing_simulator/phishing_success.html')
        else:
            # Log the phishing attempt with the attack type "Not Phishing"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=False,
                attack_type="Not Phishing",
            )
            # Render a template indicating that it's not a phishing attempt
            return render(request, 'phishing_simulator/not_phishing.html')

    return render(request, 'phishing_simulator/phishing_form.html')

def smishing(request):
    if request.method == 'POST':
        # Assume you have a form that captures an SMS message
        sms_message = request.POST.get('sms_message', '')

        # Simulate a basic smishing check
        if "smishing code" in sms_message:
            # Log the successful smishing attempt with the attack type "Smishing"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=True,
                attack_type="Smishing",
            )
            # Render a template indicating a successful smishing attempt
            return render(request, 'phishing_simulator/smishing_success.html')
        else:
            # Log the failed smishing attempt with the attack type "Not Smishing"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=False,
                attack_type="Not Smishing",
            )
            # Render a template indicating that it's not a successful smishing attempt
            return render(request, 'phishing_simulator/smishing_not.html')

    return render(request, 'phishing_simulator/smishing_form.html')

def pharming(request):
    if request.method == 'POST':
        # Assume you have a form that captures a URL
        url = request.POST.get('url', '')

        # Simulate a basic pharming check
        if "fraudulent-website.com" in url:
            # Log the successful pharming attempt with the attack type "Pharming"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=True,
                attack_type="Pharming",
            )
            # Render a template indicating a successful pharming attempt
            return render(request, 'phishing_simulator/pharming_success.html')
        else:
            # Log the failed pharming attempt with the attack type "Not Pharming"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=False,
                attack_type="Not Pharming",
            )
            # Render a template indicating that it's not a successful pharming attempt
            return render(request, 'phishing_simulator/pharming_not.html')

    return render(request, 'phishing_simulator/pharming_form.html')

def ceo_fraud(request):
    if request.method == 'POST':
        # Assume you have a form that captures an email message
        email_message = request.POST.get('email_message', '')

        # Simulate a basic CEO Fraud check
        if "CEO's urgent request" in email_message:
            # Log the successful CEO Fraud attempt with the attack type "CEO Fraud"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=True,
                attack_type="CEO Fraud",
            )
            # Render a template indicating a successful CEO Fraud attempt
            return render(request, 'phishing_simulator/ceo_fraud_success.html')
        else:
            # Log the failed CEO Fraud attempt with the attack type "Not CEO Fraud"
            PhishingAttempt.objects.create(
                attacker_ip=request.META.get('REMOTE_ADDR'),
                target_url=request.build_absolute_uri(),
                success=False,
                attack_type="Not CEO Fraud",
            )
            # Render a template indicating that it's not a successful CEO Fraud attempt
            return render(request, 'phishing_simulator/ceo_fraud_not.html')

    return render(request, 'phishing_simulator/ceo_fraud_form.html')

def custom_admin_dashboard(request):
    # Retrieve data from the PhishingAttempt model
    data = PhishingAttempt.objects.all()

    # Create a DataFrame for data manipulation
    df = pd.DataFrame(data.values('attack_type', 'attacker_ip', 'success'))

    # Create the first chart: Bar chart showing attacks by count and type
    chart1_data = df['attack_type'].value_counts()
    chart1_labels = chart1_data.index
    chart1_values = chart1_data.values

    plt.figure(figsize=(10, 6))
    plt.bar(chart1_labels, chart1_values)
    plt.xlabel('Attack Type')
    plt.ylabel('Count')
    plt.title('Phishing Attempts by Type')
    plt.xticks(rotation=45)

    # Save the chart to a BytesIO object
    chart1_image = BytesIO()
    plt.savefig(chart1_image, format='png')
    chart1_image.seek(0)
    chart1_url = base64.b64encode(chart1_image.read()).decode()
    plt.close()

    # Create the second chart: Bar chart showing IP addresses and their attack count
    chart2_data = df['attacker_ip'].value_counts().nlargest(10)  # Show the top 10 IP addresses
    chart2_labels = chart2_data.index
    chart2_values = chart2_data.values

    plt.figure(figsize=(10, 6))
    plt.bar(chart2_labels, chart2_values)
    plt.xlabel('Attacker IP')
    plt.ylabel('Count')
    plt.title('Phishing Attempts by IP Address')
    plt.xticks(rotation=45)

    # Save the chart to a BytesIO object
    chart2_image = BytesIO()
    plt.savefig(chart2_image, format='png')
    chart2_image.seek(0)
    chart2_url = base64.b64encode(chart2_image.read()).decode()
    plt.close()

    # Create the third chart: Pie chart showing success vs. failure for all attacks
    chart3_data = df['success'].value_counts()
    chart3_labels = ['Successful', 'Unsuccessful']
    chart3_values = chart3_data.values

    # Ensure that chart3_values contains two values (counts of Successful and Unsuccessful)
    if len(chart3_values) != 2:
        chart3_labels = []  # Set labels to an empty list if data is not available
        chart3_values = []

    plt.figure(figsize=(6, 6))
    plt.pie(chart3_values, labels=chart3_labels, autopct='%1.1f%%', startangle=90)
    plt.title('Phishing Attempts by Success')

    # Save the chart to a BytesIO object
    chart3_image = BytesIO()
    plt.savefig(chart3_image, format='png')
    chart3_image.seek(0)
    chart3_url = base64.b64encode(chart3_image.read()).decode()
    plt.close()

    return render(request, 'admin/dashboard.html', {
        'chart1_url': chart1_url,
        'chart2_url': chart2_url,
        'chart3_url': chart3_url,
    })

# Define the success and failure views for each URL pattern
def phishing_success(request):
    return render(request, 'phishing_simulator/phishing_success.html')

def phishing_failure(request):
    return render(request, 'phishing_simulator/phishing_failure.html')

def smishing_success(request):
    return render(request, 'phishing_simulator/smishing_success.html')

def smishing_failure(request):
    return render(request, 'phishing_simulator/smishing_failure.html')

def pharming_success(request):
    return render(request, 'phishing_simulator/pharming_success.html')

def pharming_failure(request):
    return render(request, 'phishing_simulator/pharming_failure.html')

def ceo_fraud_success(request):
    return render(request, 'phishing_simulator/ceo_fraud_success.html')

def ceo_fraud_failure(request):
    return render(request, 'phishing_simulator/ceo_fraud_failure.html')
