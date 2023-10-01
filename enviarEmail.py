# E-mail: grupo6compiladores@gmail.com
# Senha do e-mail: Grupo@6CC
# Senha do App: drcggvikgvubuawl

import smtplib
import email.message

def enviar_email():

    #É possível alterar o corpo do email com tags HTML
    corpo_email = """
    <p>Isso é apenas um <b>teste de envio</b>, não há necessidade de responder este e-mail.</p>
    <p>Grupo 6: Lara Vitória, Maria Beatiriz Motta, Sarah Domingos, Emmanuel Araujo, Allanderson.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Grupo 6 - Trabalho de Compiladores"
    msg['From'] = 'grupo6compiladores@gmail.com'
    msg['To'] = 'arturohd@ic.ufal.br' #Esse é o e-mail do professor, lembre de alterar caso queira testar com o seu
    senha = 'drcggvikgvubuawl'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()