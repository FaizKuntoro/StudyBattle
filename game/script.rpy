# Study battle Alpha.

# main character.
define arisa = Character ("Arisa", color="#caeb51", who_bold=True, who_outlines=[(1, "#000")])
define intro = Character("", color="#B6AAA6", window_yalign=0.5,who_bold=True, who_outlines=[(1, "#000")])
define gui.dialogue_xpos = 0.5

# enemy
define azizah = Character("Azizah", color="#ff4800", who_bold=True, who_outlines=[(1, "#000")])

# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)
# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)
# Camera flash - quickly fades to white, then back to the scene.
define whiteflash = Fade(0.1, 0.0, 0.5, color="#fff")
define redflash = Fade(0.1, 0.0, 0.5, color="#f00")


# image arisa
image arisa biasa = "Character/arisa.png"
image arisa senang = "Character//.png"
image arisa lesu = "Character//.png"

image arisa diam biasa = "Character//.png"
image arisa diam senang = "Character//.png"
image arisa diam lesu = "Character//.png"

# image azizah
image azizah biasa = "Character/azizah.png"
image azizah senang = "Character//.png"
image azizah lesu = "Character//.png"

image azizah diam biasa = "Character//.png"
image azizah diam senang = "Character//.png"
image azizah diam lesu = "Character//.png"

#flip
image arisa biasa flip= im.Flip("Character//.png", horizontal=True)
image arisa senang flip= im.Flip("Character//.png", horizontal=True)
image arisa lesu flip= im.Flip("Character//.png", horizontal=True)


image arisa diam biasa flip= im.Flip("Character///.png", horizontal=True)
image arisa diam senang flip= im.Flip("Character///.png", horizontal=True)
image arisa diam lesu= im.Flip("Character///.png", horizontal=True)

# bg
image bg aula = "Background/aula.jpg"

image splashStudyBattle = "Studybattle.jpg"
image splashPMGD = "pmgd.jpg"

label splashscreen:
    # Menampilkan splashPMGD di layar dengan skala 16:9, ukuran lebih kecil
    scene black
    $ renpy.pause(1.0, hard=True)

    # Menampilkan splashPMGD dengan ukuran lebih kecil (zoom 0.5 atau ukuran lain yang diinginkan)
    scene splashPMGD 
    show splashPMGD:
        xalign 0.5  # Tempatkan di tengah horizontal
        yalign 0.5  # Tempatkan di tengah vertikal
        zoom 0.5    # Mengurangi ukuran gambar menjadi 50% dari ukuran asli
    $ renpy.pause(2.0, hard=True)

    # Kembali ke hitam
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)

    # Menampilkan splashStudyBattle dengan skala 16:9
    scene splashStudyBattle 
    show splashStudyBattle:
        xalign 0.5  # Tempatkan di tengah horizontal
        yalign 0.5  # Tempatkan di tengah vertikal
        zoom 1.0    # Sesuaikan gambar agar pas di layar (tanpa distorsi)
    $ renpy.pause(2.0, hard=True)

    # Kembali ke hitam
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)

    return


define dismissTime = 1
screen noDismiss:
    key 'dismiss' action NullAction()
    timer 1 repeat True action If(dismissTime > 0, true=SetVariable('dismissTime', dismissTime - 1), false=[Hide('noDismiss')])

# Game dimulai disini.
label start:
    scene expression "#000"
    with Dissolve(1.0)

# shot no 1
label shot_1:
    show screen noDismiss
    intro "Setelah Melewati Berbagai Tantangan"
    

# shot no 2
label shot_2:
    show screen noDismiss
    intro "Akhirnya, Arisa melaju ke final Study Battle"
    


# shot no 3
    scene bg aula with fade
    show arisa biasa
    with dissolve
    show screen noDismiss
    arisa "Akhirnya, Aku telah sampai di Final Study Battle"
    $ renpy.pause(0.5, hard=True)

# shot no 4
    scene bg aula with dissolve
    show arisa biasa flip:
        xalign 0.05
        yalign 1.0

    show arisa biasa
    with dissolve
    show screen noDismiss
    arisa "Saatnya Beraksi!!!"

# shot no 5
call battle from _call_battle

return
