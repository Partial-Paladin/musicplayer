def on_button_pressed_a():
    global track
    music.stop_all_sounds()
    basic.clear_screen()
    track += 1
    if track == 12:
        track = 1
    basic.show_number(track)
    if track == 1:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 2:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 3:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.PRELUDE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.PRELUDE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 4:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.ODE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.ODE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 5:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.NYAN),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.NYAN),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 6:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.RINGTONE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.RINGTONE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 7:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.FUNK),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.FUNK),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 8:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.BLUES),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.BLUES),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 9:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 10:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.WEDDING),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.WEDDING),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 11:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.FUNERAL),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.FUNERAL),
                MelodyOptions.FOREVER_IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global loop
    music.stop_all_sounds()
    basic.clear_screen()
    if loop == 0:
        basic.show_leds("""
            . . . # .
                        . # . . #
                        # # # . #
                        . # . . #
                        . . # # .
        """)
        loop = 1
    else:
        basic.show_leds("""
            . . . . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . . . .
        """)
        loop = 0
    basic.show_number(track)
    if track == 1:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.DADADADUM),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 2:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.ENTERTAINER),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 3:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.PRELUDE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.PRELUDE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 4:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.ODE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.ODE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 5:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.NYAN),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.NYAN),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 6:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.RINGTONE),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.RINGTONE),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 7:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.FUNK),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.FUNK),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 8:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.BLUES),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.BLUES),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 9:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.BIRTHDAY),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 10:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.WEDDING),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.WEDDING),
                MelodyOptions.FOREVER_IN_BACKGROUND)
    elif track == 11:
        if loop == 0:
            music.start_melody(music.built_in_melody(Melodies.FUNERAL),
                MelodyOptions.ONCE_IN_BACKGROUND)
        else:
            music.start_melody(music.built_in_melody(Melodies.FUNERAL),
                MelodyOptions.FOREVER_IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)

loop = 0
track = 0
track = 0
loop = 0
basic.show_string("A")

def on_forever():
    pass
basic.forever(on_forever)
