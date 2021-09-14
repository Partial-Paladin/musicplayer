input.onButtonPressed(Button.A, function () {
    music.stopAllSounds()
    basic.clearScreen()
    track += 1
    if (track == 13) {
        track = 1
    }
    basic.showNumber(track)
    if (track == 1) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 2) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 3) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 4) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Ode), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Ode), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 5) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 6) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 7) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 8) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 9) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 10) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Wedding), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Wedding), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 11) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.ForeverInBackground)
        }
    }
})
input.onButtonPressed(Button.B, function () {
    music.stopAllSounds()
    basic.clearScreen()
    if (loop == 0) {
        basic.showLeds(`
            . . . # .
            . # . . #
            # # # . #
            . # . . #
            . . # # .
            `)
        loop = 1
    } else {
        basic.showLeds(`
            . . . . .
            . . . # .
            # # # # #
            . . . # .
            . . . . .
            `)
        loop = 0
    }
    basic.showNumber(track)
    if (track == 1) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 2) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Entertainer), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 3) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Prelude), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 4) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Ode), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Ode), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 5) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Nyan), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 6) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 7) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Funk), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 8) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Blues), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 9) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Birthday), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 10) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Wedding), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Wedding), MelodyOptions.ForeverInBackground)
        }
    } else if (track == 11) {
        if (loop == 0) {
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.OnceInBackground)
        } else {
            music.startMelody(music.builtInMelody(Melodies.Funeral), MelodyOptions.ForeverInBackground)
        }
    } else {
    	
    }
})
let loop = 0
let track = 0
track = 0
loop = 0
basic.showString("A")
basic.forever(function () {
	
})
