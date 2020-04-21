# Instacart-reminder

This code is to refresh Instacart webpage for available delivery time, during the COVID-19 period with extremely high demand of online shopping & delivery.

## What does the code do?
1. Refresh every 1 min the Instacart webpage to see if there is available delivery time
2. Send email if there is available delivery time

## Before you start
1. Make sure you have installed Chrome and [chrome webdriver](https://chromedriver.chromium.org/downloads). Put the chrome webdriver executable in the same folder as `reminder.py`
(I will make the interface more flexible, to be compatible with Firefox, etc.)
2. Presume you have python installed, we also need `selenium`
    ```
    pip install selenium
    ```

## Usage
1. Make sure you have your screen on when you run this code
2. You need to log in to the Instacart website to see available delivery times, so you need to input your account & password.
3. You also need to log in to your email (in the code it is limited to gmail, but you can change it), so the reminder will send you email everytime there is available slot.

```
python reminder.py <instacart_account> <instacart_password> <email_account> <email_password> 
```

