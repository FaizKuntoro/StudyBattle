default save_enabled_state = True
#animasi caracter
image user hit animated:
    "user hurt"
    pause 0.1
    "user defense"
    pause 0.1
    repeat 5

image tbx common hit animated:
    "tbx c hurt"
    pause 0.1
    "tbx c defense"
    pause 0.1
    repeat 5

image user happy animated:
    "user senang"
    pause 1.5
    "user biasa"

image user sad animated:
    "user sedih"
    pause 1.5
    "user biasa"

image user hurt = "Character/Arisa/sedih3.png"
image user attack = "Character/Arisa/senang3.png"
image user biasa = "Character/Arisa/datar3.png"
image user defense = "Character/Arisa/gugup3.png"  
image user senang = "Character/Arisa/senang1.png"
image user sedih = "Character/Arisa/sedih1.png"

image tbx c biasa = "Character/Cakra/datar.png"
image tbx c hurt = "Character/Cakra/sedih.png"
image tbx c attack = "Character/Cakra/marah.png"
image tbx c defense = "Character/Cakra/hah.png"
image tbx c marah = "Character/Cakra/marah.png"
image tbx c senang = "Character/Cakra/senang.png"

image winslose = "winlose.png"

#style
style move_button:
    background Frame("images/UI/button/button_idle.png", 0, 0)
    hover_background Frame("images/UI/button/button_hover.png", 0, 0)
style button_font:
    font "Font/Lato-Regular.ttf"
    size 35
    color "#eeeeee"
    hover_color "#6efc98"
    italic True
style black_font:
    color "#000000"
    font "Font/Raleway-Regular.ttf"
style white_font:
    color "#656565"
    font "Font/Nunito-Regular.ttf"

#TRANSFORM
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    

#Stats
#Experience
#Player Stats
define playermaxhp = 200
define playercurhp = 200
define playeratk = 100
define playerdef = 10

#Enemy Stats
define tbType = "Ldefense"
define enemymaxhp = 200
define enemycurhp = 200
define enemyatk = 100
define enemydef = 100

#Move dmg temp
define Ldmg= 50
define Mdmg = 50
define Hdmg = 50


#Calculation Variables

#Effectiveness and Crit Rates

#Elements
define movelist = ["Ldmg", "Mdmg","Hdmg"]
define tempmovelist = ["Ldmg", "Mdmg","Hdmg"]
define atklist = ["Ldamage", "Mdamage", "Hdamage"]
define atk = ""
define defelist = ["Ldefense", "Mdefense", "Hdefense"]
define defe = ""
define enemydefe = "Ldefense" #["Fire", "Wind", "Earth", "Water", "Physical"]
define movename = ""

#Other
define turndesc = "YOUR"
define turndesccol = "#81ee57" #"#81ee57" "#a13e3e" "#E25822"
define atkcol = ""
define grinding = False
define bgName = "portal"

#Dmg Calculations
define movedmg = 20

#Enemy Min and Max Move DMG

#Turn Switch
define turn = 1

#Final dmg
define dmgto = 0

#Trivia Vars
define dummy = False #Question dummy
define canAttack = False
default quizquestion = 0
default z = 0
default asks = "berapa 2 + 17"
default answers = "19"
default corrects = "19"
default answers1 = "1"
default answers2 = "2"
default answers3 = "15"
default answers4 = "19"
default answercheck = ""

define movename = ""
define movename1 = ""
define movename2 = ""
define movename3 = ""
define movename4 = ""
define moveend = ""
define elementQuestion = ""

define moveCounter = 0
define moveDesc0 = ""
define moveDesc1 = ""
define moveDesc2 = ""
define moveDesc3 = ""

define moveDmg0 = 0
define moveDmg1 = 0
define moveDmg2 = 0
define moveDmg3 = 0


label moveinit:

    $movename = tempmovelist[0]
    $movename1 = tempmovelist[1]
    $movename2 = tempmovelist[2]
    return

label moveElement:
    if movename == "Ldmg":
        $moveDesc0 = "Ldamage"
        $moveDmg0 = Ldmg
    elif movename == "Mdmg":
        $moveDesc0 = "Mdamage"
        $moveDmg0 = Mdmg
    elif movename == "Hdmg":
        $moveDesc0 = "Hdamage"
        $moveDmg0 = Hdmg

    if movename1 == "Ldmg":
        $moveDesc1 = "Ldamage"
        $moveDmg1 = Ldmg
    elif movename1 == "Mdmg":
        $moveDesc1 = "Mdamage"
        $moveDmg1 = Mdmg
    elif movename1 == "Hdmg":
        $moveDesc1 = "Hdamage"
        $moveDmg1 = Hdmg
    
    if movename2 == "Ldmg":
        $moveDesc2 = "Ldamage"
        $moveDmg2 = Ldmg
    elif movename2 == "Mdmg":
        $moveDesc2 = "Mdamage"
        $moveDmg2 = Mdmg
    elif movename2 == "Hdmg":
        $moveDesc2 = "Hdamage"
        $moveDmg2 = Hdmg

    if movename3 == "Ldmg":
        $moveDesc3 = "Ldamage"
        $moveDmg3 = Ldmg
    elif movename3 == "Mdmg":
        $moveDesc3 = "Mdamage"
        $moveDmg3 = Ldmg
    elif movename3 == "Hdmg":
        $moveDesc3 = "Hdamage"
        $moveDmg3 = Hdmg
    
    return

#Screens
#Timer bar
$ time = 0 # time in ticks (eg. 800 = 8 seconds)
$ timer_range = 0
$ timer_jump = 'checkquiz1'

screen countdown:
    # text "Time Limit" xalign 0.5 yalign 0.76 style ("black_font") at alpha_dissolve
    timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 1 xmaximum 600 at alpha_dissolve:
        left_bar Frame("images/Bar/timepenuh.png") right_bar Frame("images/Bar/timekosong.png")


#HP Bars Animations
screen hpbar:
    text "{b}HP{/b}" xalign 0.085 yalign 0.08 style ("black_font") at alpha_dissolve
    text "[playercurhp]/[playermaxhp]" xalign 0.33 yalign 0.12 style ("black_font") size 27 at alpha_dissolve
    bar value AnimatedValue(playercurhp, range=playermaxhp) at alpha_dissolve:
        xalign 0.15 yalign 0.08 xmaximum 500 left_bar Frame("images/Bar/hppenuh.png") right_bar Frame("images/Bar/hpkosong.png")

    text "{b}HP{/b}" xalign 0.9185 yalign 0.08 style ("black_font") at alpha_dissolve
    text "[enemycurhp]/[enemymaxhp]" xalign 0.66 yalign 0.12 style ("black_font") size 27 at alpha_dissolve
    bar value AnimatedValue(enemycurhp, range=enemymaxhp) at alpha_dissolve:
        xalign 0.85 yalign 0.08 xmaximum 500 left_bar Frame("images/Bar/hppenuh.png") right_bar Frame("images/Bar/hpkosong.png")

#Screen untuk menu
screen menu_frame:
    frame at alpha_dissolve:
        background "#00000099" 
        xalign 1.0 yalign 1.0
        

screen result_screen(result_text):
    # Display the result background image
    add "winlose.png" zoom 2 xalign 0.5 yalign 0.5

    # Overlay the result text (e.g., "You Win" or "You Lose")
    text "[result_text]" xalign 0.5 yalign 0.45 size 64 color "#000000" font "Font/Lato-Regular.ttf" bold True

    # Display an OK button to continue
    textbutton "OK" action Return() xalign 0.5 yalign 0.8

#Screen Health
screen healths:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0
        xsize 1980
        ysize 210
        background Frame("images/UI/yanto.png")
        text "{i}Arisa{/i}" xalign 0.135 yalign 0.22 color "#000000ff" font "Font/Lato-Regular.ttf"
        text "{i}Ilham{/i}" xalign 0.87 yalign 0.22 color "#000000" font "Font/Lato-Regular.ttf"

#Attack Menu
screen moves:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1800
        ysize 360
        background Frame("images/UI/yanto2.png")
        text "Pilih kesulitan" xalign 0.10 yalign 0.11 color "#656565" font "Font/Raleway-Regular.ttf" size 38
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 0
                
            hbox:
                spacing 0
                button:
                    text "[movename]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), Hide("displayMoveText"), SetVariable("moveend", movename), Jump("initmovevar")

                    hovered Show("displayMoveText", displayElement = "[moveDesc0] element", displayDmg = "[moveDmg0] DMG")
                    unhovered Hide("displayMoveText")


                button:
                    text "[movename1]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), Hide("displayMoveText"), SetVariable("moveend", movename1), Jump("initmovevar")

                    hovered Show("displayMoveText", displayElement = "[moveDesc1] element", displayDmg = "[moveDmg1] DMG")
                    unhovered Hide("displayMoveText")

                button:
                    text "[movename2]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), Hide("displayMoveText"), SetVariable("moveend", movename2), Jump("initmovevar")

                    hovered Show("displayMoveText", displayElement = "[moveDesc2] element", displayDmg = "[moveDmg2] DMG")
                    unhovered Hide("displayMoveText")
screen displayMoveText:
    default displayElement = ""
    default displayDmg = ""
    vbox:
        xalign 0.5
        yalign 0.98
        frame:
            xsize 1300
            ysize 75
            background "#00000000" 
            hbox:
                xalign 0.5
                yalign 0.5
                spacing 20
                text displayElement color "#656565"
                text displayDmg color "#656565"


label initmovevar:
    if moveend == "Ldmg":
        $atk = "Ldamage"
        $elementQuestion = "Ldamage"
        #audio.moveSFX = fireballsfx
        $movename = moveend
        $movedmg = Ldmg
        $atkcol = "#E25822"

    elif moveend == "":
        $atk = "Mdamage"
        $elementQuestion = "Mdamage"
        #audio.moveSFX = windsfx
        $movename = moveend
        $movedmg = Mdmg
        $atkcol = "#61ffb0"

    else:
        $atk = "Hdamage"
        $elementQuestion = "Ldamage"
        #audio.moveSFX = punchsfx
        $movename = moveend
        $movedmg = Ldmg
        $atkcol = "#cccccc"
    
    $defe = enemydefe
    jump initTriv
            
screen shield:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1980
        ysize 360
        background Frame("images/UI/yanto.png")
        text "gunakan pertahanan" xalign 0.10 yalign 0.11 color "#656565" font "Font/Raleway-Regular.ttf" size 38
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 0
            hbox:
                spacing 0
                button:
                    text "Ldefense" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Ldefense"), SetVariable("atkcol", "#E25822"), SetVariable("defe", "Ldefense"), Jump("initTrivDef")
                button:
                    text "Mdefense" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Mdefense"), SetVariable("atkcol", "#61ffb0"), SetVariable("defe", "Mdefense"), Jump("initTrivDef")
                button:
                    text "Hdefense" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Hdefense"), SetVariable("atkcol", "#b17837"), SetVariable("defe", "Hdefense"), Jump("initTrivDef")
                

#Start Mechanism
#Start battle (called only once from script.rpy)
label battle:
    scene black with Fade(1, 0, 1)
    window hide dissolve
    $save_enabled_state = False
    #music
    $renpy.pause(2.0,hard=True)
    if bgName == "portal":
        scene bg portal with fade
    elif bgName == "surabaya":
        scene bg jawa surabaya with fade
    elif bgName == "borobudur":
        scene bg jawa borobudur with fade
    
    $renpy.pause(1.0,hard=True)

    show screen healths
    show screen hpbar

    call moveinit from _call_moveinit
    call randomtriv from _call_randomtriv
    call moveElement from _call_moveElement

    show screen moves
    $renpy.pause(1.0,hard=True)

    show tbx c biasa with moveinright:
        xalign 0.85 #78
        yalign 1.0 #15
        zoom 0.4

    show user biasa :
        zoom 0.4
        xalign 0.15
        yalign 1.0

    
    with moveinleft

    $renpy.pause(0.5,hard=True)  
    
    $renpy.pause(None,hard=True)   

#Attack Menu
label attackmove:
    window hide dissolve
    show screen moves
    $renpy.pause(None,hard=True)

label defensemove:
    window hide dissolve
    show screen shield
    $renpy.pause(None,hard=True)

#Trivia gui
label trivia1:
    # Ensure Triv is a dictionary and contains valid keys
    $ time = 200
    $ timer_range = 200
    $ timer_jump = 'checkquiz1'
    show screen menu_frame
    show screen countdown

    # Set colors based on which answer is correct
    if answers1 == corrects:
        $ color0 = "#00FF00"  # Green for correct
        $ color1 = "#FF0000"  # Red for incorrect
        $ color2 = "#FF0000"
        $ color3 = "#FF0000"
    elif answers2 == corrects:
        $ color0 = "#FF0000"
        $ color1 = "#00FF00"
        $ color2 = "#FF0000"
        $ color3 = "#FF0000"
    elif answers3 == corrects:
        $ color0 = "#FF0000"
        $ color1 = "#FF0000"
        $ color2 = "#00FF00"
        $ color3 = "#FF0000"
    elif answers4 == corrects:
        $ color0 = "#FF0000"
        $ color1 = "#FF0000"
        $ color2 = "#FF0000"
        $ color3 = "#00FF00"

    # Show the trivia question and answers with dynamic colors
    menu:
        "{color=[color0]}{b}[asks]{/b}{/color}"
        "[answers1]":
            $ answercheck = answers1
            jump checkquiz1
        "[answers2]":
            $ answercheck = answers2
            jump checkquiz1
        "[answers3]":
            $ answercheck = answers3
            jump checkquiz1
        "[answers4]":
            $ answercheck = answers4
            jump checkquiz1


#Answer check
label checkquiz1:

    $ time = 25
    $ timer_range = 25
    $ timer_jump = 'checkquiz2'
    show screen countdown
    menu:
        "{color=[atkcol]}{b}[elementQuestion] Trivia{/b}{/color}\n
        {color=#FFFFFF}[asks]{/color}" if dummy == True:
            "Oops. How'd you get here?"
        "{color=[color0]}[answers1]" if dummy == True:
            "Oops. How'd you get here?"
        "{color=[color1]}[answers2]" if dummy == True:
            "Oops. How'd you get here?"
        "{color=[color2]}[answers3]" if dummy == True:
            "Oops. How'd you get here?"
        "{color=[color3]}[answers4]" if dummy == True:
            "Oops. How'd you get here?"

label checkquiz2:

    #If correct
    if answercheck == corrects:
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()
        
        window show dissolve

        $movedmg *= 1
        $movedmg = int(movedmg)
        $canAttack = True

        show user happy animated

        if turn == True:
            "Trivia benar! Serangan berhasil menyerang Time Bandit!"
        else:
            "Trivia benar! Perisai berhasil digunakan!"

    #If incorrect
    elif answercheck == "":
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()

        window show dissolve

        $defe = "None"
        $canAttack = False

        show user sad animated

        if turn == True:
            "Waktu habis! Serangan gagal menyerang Time Bandit!"
        else:
            "Waktu habis! Perisai gagal digunakan!"
    else:
        $Hide("countdown", transition=Dissolve(1.0))()
        $Hide("menu_frame", transition=Dissolve(1.0))()
       
        window show dissolve

        $defe = "None"
        $canAttack = False

        show user sad animated

        if turn == True:
            "Trivia salah! Serangan gagal menyerang Time Bandit!"
        else:
            "Trivia salah! Perisai gagal digunakan!"

    #Questions Index
    $z +=1

    jump attack

label attack: #damaging part
    window show dissolve
    if turn == 1: #player turn
        if canAttack == True: #decide if the player can attack or not (set from whether the trivia is correct or not
            "Kamu menggunakan [movename]."
            $dmgto = playeratk + movedmg - enemydef
            $dmgto = int(dmgto)
            $enemycurhp -= dmgto

            if enemycurhp <= 0:
                $enemycurhp = 0

            $renpy.restart_interaction()

            #play sound moveSFX
            show user attack 
            $renpy.pause(0.2,hard=True)
            show tbx common hit animated
            $renpy.pause(1.8,hard=True)
            show tbx c biasa
            show user biasa

    elif turn == 2:  # enemy turn
        if defe != "None":
            "Kamu menggunakan perisai [defe]."
        "Time Bandit menggunakan serangan [atk]."

        $dmgto = enemyatk + movedmg - playerdef
        $dmgto = int(dmgto)  # Ensure integer value for damage
        $playercurhp -= dmgto  # Decrease player's health

        if playercurhp <= 0:  # Ensure player health doesn't go below 0
            $playercurhp = 0

        $renpy.restart_interaction()

        # play sound lasersfx (add your sound effect code here if needed)
        show tbx c attack
        $renpy.pause(0.2, hard=True)
        show user hit animated
        $renpy.pause(1.8, hard=True)
        show user biasa

    $movedmg = 0 #reset the move dmg
    $canAttack = False #reset

    #Refresh HP Bar
    $renpy.restart_interaction()

    #Going back to script.rpy if either sides died
    if playercurhp <= 0:
        show user sedih
        show tbx c senang
        "Kamu kalah! Time Bandit telah memenangkan pertarungan."
        
        $renpy.restart_interaction()
        $renpy.pause(2.0,hard=True)

        $Hide("hpbar", transition=Dissolve(1.0))()
        $Hide("healths", transition=Dissolve(1.0))()
        $Hide("menu", transition=Dissolve(1.0))()

        $playercurhp = playermaxhp
        $enemycurhp = enemymaxhp
        
        call resetAll from _call_resetAll

        stop music fadeout 2
        scene black with fade
        
        $save_enabled_state = True

        if grinding == False:
            return
        else:
            $grinding = False
            window hide dissolve
            jump mapStart

    elif enemycurhp <= 0:
        $ result_text = "You Win" 
        show user senang
        show tbx c marah
        window hide dissolve
        call screen result_screen(result_text)
        hide screen moves

        
        
        "Kamu menang! Time Bandit berhasil dikalahkan."
        

        $renpy.restart_interaction()
        $renpy.pause(2.0,hard=True)

       
       
        $Hide("hpbar", transition=Dissolve(1.0))()
        $Hide("healths", transition=Dissolve(1.0))()
        
        call resetAll from _call_resetAll_1

       

        stop music fadeout 2
        scene black with fade

        $save_enabled_state = True

        if grinding == False:
            return
        else:
            $grinding = False
            window hide dissolve
            jump mapStart

    #If neither sides died yet
    else:
        call switch from _call_switch
        if turn == 1:
            jump attackmove

        elif turn == 2:
            show user biasa
            
            with move
            show user biasa
            with dissolve

            jump defensemove

label resetAll:
    $playercurhp = playermaxhp
    $enemycurhp = enemymaxhp
    $turn = 1
    $turndesc = "YOUR"
    $turndesccol = "#81ee57"
    return
    


label switch: #switch turn
    $renpy.pause(1.0, hard=True)  # untuk interval animasi damage

    if turn == 1:
        # Giliran Player
        $turn = 2  # Pindah ke giliran Enemy
        $turndesc = "YOUR"  # Deskripsi giliran Player
        $turndesccol = "#81ee57"  # Warna untuk giliran Player

    elif turn == 2:
        # Giliran Enemy
        $turn = 1  # Pindah ke giliran Player
        $turndesc = "ENEMY"  # Deskripsi giliran Enemy
        $turndesccol = "#a13e3e"  # Warna untuk giliran Enemy
        $defe = enemydefe  # Menyimpan nilai pertahanan musuh (misalnya untuk shield)

    return
