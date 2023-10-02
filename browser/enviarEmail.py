# E-mail: grupo6compiladores@gmail.com
# Senha do e-mail: Grupo@6CC
# Senha do App: drcggvikgvubuawl

import smtplib
import email


def enviar_email(to_email):

    #É possível alterar o corpo do email com tags HTML
    corpo_email = """
    <p>Isso é apenas um <b>teste de envio</b>, não há necessidade de responder este e-mail.</p>
    <p>Grupo 6: Lara Vitória, Maria Beatriz Motta, Sarah Domingos, Emmanuel Araujo, Allanderson Lima.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Grupo 6 - Trabalho de Compiladores"
    msg['From'] = 'grupo6compiladores@gmail.com'
    msg['To'] = to_email
    senha = 'drcggvikgvubuawl'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    print('Email enviado')
