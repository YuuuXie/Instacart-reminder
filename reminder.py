import time, sys, datetime, os
import smtplib
from selenium import webdriver

def check(account, account_pwd, email, email_pwd):
    # get driver
    url = "https://www.instacart.com"
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url)
    time.sleep(5)

    # log in
    driver.find_element_by_partial_link_text("Log in").click()
    driver.find_element_by_id("nextgen-authenticate.all.log_in_email").send_keys(account)
    driver.find_element_by_id("nextgen-authenticate.all.log_in_password").send_keys(account_pwd)
    driver.find_element_by_xpath("//button[@type='submit']").click()

    # log in email
    server = login_email(email, email_pwd)
    t0 = time.time()
    
    # check_delivery_times
    while 'Exit' not in os.listdir('./'): # create an Exit file to exit

        time.sleep(10)
        driver.find_element_by_xpath("//a[@href='/market-basket/info?tab=delivery']").click()
        time.sleep(10)

        try:
            no_delivery_times = driver.find_element_by_xpath("//img[@alt='No delivery times available']")
            print('No delivery times', flush=True)
        except:
            time_now = datetime.datetime.now()
            msg = f"Delivery available: {time_now}"
            server.sendmail(email, email, msg)
            print('Yes', time_now, flush=True)

        driver.find_element_by_xpath("//button[@aria-label='Close modal']").click()
        time.sleep(45)
        if time.time() - t0 > 600: # log in email every 10 min
            print('log in to the email')
            server = login_email(email, email_pwd)
            t0 = time.time()

        driver.refresh()

    driver.quit()
    
def login_email(email, password):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    return server


if __name__ == "__main__":
    check(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
