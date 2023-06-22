import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "vjha3003@gmail.com"
    password = "Enter password"
    receiver_email = "vjha3003@gmail.com"

    context = ssl.create_default_context()

    try: 
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.startls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendemail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit()