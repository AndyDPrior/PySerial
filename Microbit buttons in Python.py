def Write(text: str):
    basic.show_string(text)
    serial.write_line(text)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)

def on_button_pressed_a():
    if Exit == 0:
        Write("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if Exit == 0:
        Write("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if Exit == 0:
        Write("S")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_data_received():
    global Exit
    Exit = 1
    basic.show_string(serial.read_until(serial.delimiters(Delimiters.HASH)))
    basic.pause(100)
    Exit = 0
    basic.clear_screen()
serial.on_data_received(serial.delimiters(Delimiters.HASH), on_data_received)

def on_logo_touched():
    if Exit == 0:
        Write("T")
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

Exit = 0
Exit = 0
serial.redirect(SerialPin.USB_TX, SerialPin.USB_RX, BaudRate.BAUD_RATE115200)