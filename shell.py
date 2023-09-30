import core

while True:
    text = input('Viper > ')
    result, error = core.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)