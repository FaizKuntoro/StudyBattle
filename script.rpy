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
image arisa biasa = "Character/MIKO/biasa.png"
image arisa senang = "Character/MIKO/senang.png"
image arisa lesu = "Character/MIKO/marah.png"

image arisa diam biasa = "Character/MIKO/biasa.png"
image arisa diam senang = "Character/MIKO/senang.png"
image arisa diam lesu = "Character/MIKO/marah.png"

# image azizah
image azizah biasa = "Character/MIKO/biasa.png"
image azizah senang = "Character/MIKO/senang.png"
image azizah lesu = "Character/MIKO/marah.png"

image azizah diam biasa = "Character/MIKO/biasa.png"
image azizah diam senang = "Character/MIKO/senang.png"
image azizah diam lesu = "Character/MIKO/marah.png"

#flip
image arisa biasa flip= im.Flip("Character/MIKA/biasa.png", horizontal=True)
image arisa senang flip= im.Flip("Character/MIKA/senang.png", horizontal=True)
image arisa lesu flip= im.Flip("Character/MIKA/marah.png", horizontal=True)


image arisa diam biasa flip= im.Flip("Character/MIKA/diam/biasa.png", horizontal=True)
image arisa diam senang flip= im.Flip("Character/MIKA/diam/senang.png", horizontal=True)
image arisa diam marah lesu= im.Flip("Character/MIKA/diam/marah.png", horizontal=True)


image splashStudyBattle = ".png"
image splashPMGD = ".png"

label splashscreen:
    scene black
    $renpy.pause(1.0,hard=True)
    scene splashPMGD with Dissolve(2.0)
    $renpy.pause(2.0,hard=True)
    scene black with dissolve
    $renpy.pause(1.0,hard=True)
    scene splashStudyBattle with Dissolve(2.0)
    $renpy.pause(2.0,hard=True)
    scene black with dissolve
    $renpy.pause(1.0,hard=True)
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
    show screen noDismiss
    intro "Setelah Melewati\nBerbagai Tantangan "
   
# shot no 2
    show screen noDismiss
    intro "Akhirnya\nArisa melaju ke final Study Battle"

# shot no 3
    scene bg aula with fade
    show arisa biasa
    with dissolve
    show screen noDismiss
    arisa "Akhirnya, Aku telah sampai di Final Study Battle"
    $ renpy.pause(0.5, hard=True)

# shot no 4
    scene bg lab with dissolve
    show arisa senang flip:
        xalign 0.95
        yalign 1.0

    show arisa senang
    with dissolve
    show screen noDismiss
    arisa "Saatnya Beraksi!!!"

# shot no 5
label battle_start:
    scene bg battle_arena
    label battle_start:
    # Memulai mekanisme battle
    call battle_mechanism

    # Periksa hasil battle
    if player_hp > 0 and enemy_hp <= 0:
        jump win_scene
    elif player_hp <= 0:
        jump lose_scene
    return

label win_scene:
    scene bg victory
    show arisa senang
    "Congratulations! You have defeated the enemy and won the game!"
    return

label lose_scene:
    scene bg defeat
    show arisa lesu
    "You have been defeated. Do you want to try again?"
    menu:
        "Retry":
            # Reset status dan kembali ke battle
            $ player_hp = 100
            $ enemy_hp = 100
            jump battle_start
        "Quit":
            return
   
    return
