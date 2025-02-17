#Battle Script
#Low > Mid > High
default save_enabled_state = True

#Declaring audio
define lowsfx = "audio/battle/.mp3"
define midsfx = "audio/battle/.mp3"
define highsfx = "audio/battle/.mp3"
define punchsfx = "audio/battle/.mp3"
define lasersfx = "audio/battle/.mp3"

define audio.battlebgm = "audio/battle/.mp3"

define audio.moveSFX = ""


#Animation
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


image user hurt = "Character/[user!u]/hurt.png"
image user attack = "Character/[user!u]/attack.png"
image user biasa = "Character/[user!u]/biasa.png"
image user defense = "Character/[user!u]/defense.png"
image user senang = "Character/[user!u]/senang.png"
image user sedih = "Character/[user!u]/sedih.png"
image user diam biasa = "Character/[user!u]/diam/biasa.png"
image user diam senang = "Character/[user!u]/diam/senang.png"
image user diam sedih = "Character/[user!u]/diam/sedih.png"

image tbx c biasa = "Character/tb/common[tbType]/biasa.png"
image tbx c hurt = "Character/tb/common[tbType]/hurt.png"
image tbx c attack = "Character/tb/common[tbType]/attack.png"
image tbx c defense = "Character/tb/common[tbType]/defense.png"
image tbx c marah = "Character/tb/common[tbType]/marah.png"
image tbx c senang = "Character/tb/common[tbType]/senang.png"


#Style
style move_button:
    background Frame("images/UI/button/button 2_idle.png", 0, 0)
    hover_background Frame("images/UI/button/button 2_hover.png", 0, 0)
style button_font:
    font "fonts/rexlia rg.otf"
    size 35
    color "#eeeeee"
    hover_color "#6efc98"
    italic True
style black_font:
    color "#000000"
    font "fonts/Rounded_Elegance.ttf"
style white_font:
    color "#FFFFFF"
    font "fonts/Rounded_Elegance.ttf"

style mm_font:
    font "fonts/Rounded_Elegance.ttf"
    size 30
    hover_color "#ff0000"
    color "#000000"
    insensitive_color "#8b8b8b"
    
style mm_button:
    background Frame("images/UI/button/button 3_idle.png")
    hover_background Frame("images/UI/button/button 3_hover.png")

#Transforms
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    
transform charKanan:
    xalign 0.25
    yalign 1.0
transform charKiri:
    xalign 0.1
    yalign 1.0

#Stats
#Experience
define curexp = 0
define maxexp = 100
define lvl = 1
define expmulti = 1
define bonusap = 3
define curap = 5
define maxap = 5
define expNum = 0

#Player Stats
define playermaxhp = 200
define playercurhp = 200
define playeratk = 100
define playerdef = 100
define critdmg1 = 100
define truecrit = 1

#Enemy Stats
define tbType = "Fire"
define enemymaxhp = 200
define enemycurhp = 200
define enemyatk = 100
define enemydef = 100

#Move dmg temp
define Low = 50
define Mid = 50
define High = 50
define Punch = 50


#Calculation Variables

#Effectiveness and Crit Rates
define weak = 0.7
define effective = 1
define supereffective = 1.3
define critdmg = [1,2]
define crit = False
define crt = 0

#Elements
define movelist = ["Low", "Mid", "High","punch"]
define tempmovelist = ["Low", "Mid", "High", "punch"]
define atklist = ["Low", "Mid", "High", "punch"]
define atk = ""
define defelist = ["Low", "Mid", "High"]
define defe = ""
define enemydefe = "Fire" #["Fire", "Wind", "Earth", "Water", "Physical"]
define movename = ""

#Other
define effectivedesc = ""
define turndesc = "YOUR"
define turndesccol = "#81ee57" #"#81ee57" "#a13e3e" "#E25822"
define atkcol = ""
define grinding = False
define bgName = "portal"

#Dmg Calculations
define damage = 1
define multiplier = 1
define enemydamage = 1
define movedmg = 20

#Enemy Min and Max Move DMG
define x = 20
define y = 30
define a = 0

#Turn Switch
define turn = 1
define sibTurn = ""

#Final dmg
define dmgto = 0

#Trivia Vars
define dummy = False #Question dummy
define canAttack = False
default quizquestion = 0
default z = 0
default asks = ""
default answers = ""
default corrects = ""
default answers1 = ""
default answers2 = ""
default answers3 = ""
default answers4 = ""
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
    $renpy.random.shuffle(tempmovelist)
    $movename = tempmovelist[0]
    $movename1 = tempmovelist[1]
    $movename2 = tempmovelist[2]
    #$movename3 = tempmovelist[3]
    return

label moveElement:
    if movename == "Low Damage":
        $moveDesc0 = "Low"
        $moveDmg0 = Low
    elif movename == "Mid Damage":
        $moveDesc0 = "Mid"
        $moveDmg0 = Mid
    elif movename == "High Damage":
        $moveDesc0 = "High"
        $moveDmg0 = High
    
    if movename1 == "Low Damage":
        $moveDesc1 = "Low"
        $moveDmg1 = Low
    elif movename1 == "Mid Damage":
        $moveDesc1 = "Mid"
        $moveDmg1 = Mid
    elif movename1 == "High Damage":
        $moveDesc1 = "High"
        $moveDmg1 = High
    
    
    if movename2 == "Low Damage":
        $moveDesc2 = "Low"
        $moveDmg2 = Low
    elif movename2 == "Mid Damage":
        $moveDesc2 = "Mid"
        $moveDmg2 = Mid
    elif movename2 == "High Damage":
        $moveDesc2 = "High"
        $moveDmg2 = High

    #if movename3 == "Low Damage":
        $moveDesc3 = "Low"
        $moveDmg3 = Low
    elif movename3 == "Mid Damage":
        $moveDesc3 = "Mid"
        $moveDmg3 = Mid
    elif movename3 == "High Damage":
        $moveDesc3 = "High"
        $moveDmg3 = High

    
    return

#Screens
#Timer bar
$ time = 0 # time in ticks (eg. 800 = 8 seconds)
$ timer_range = 0
$ timer_jump = 'checkquiz1'

screen countdown:
    # text "Time Limit" xalign 0.5 yalign 0.76 style ("black_font") at alpha_dissolve
    timer 0.1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.81 xmaximum 600 at alpha_dissolve:
        left_bar Frame("images/Bar/health_full.png") right_bar Frame("images/Bar/health_empty.png")


#HP Bars Animations
screen hpbar:
    text "{b}HP{/b}" xalign 0.085 yalign 0.08 style ("white_font") at alpha_dissolve
    text "[playercurhp]/[playermaxhp]" xalign 0.33 yalign 0.12 style ("white_font") size 27 at alpha_dissolve
    bar value AnimatedValue(playercurhp, range=playermaxhp) at alpha_dissolve:
        xalign 0.15 yalign 0.08 xmaximum 500 left_bar Frame("images/Bar/HP_full.png") right_bar Frame("images/Bar/HP_empty.png")

    text "{b}EXP{/b}" xalign 0.082 yalign 0.15 style ("white_font") size 27 at alpha_dissolve
    bar value AnimatedValue(curexp, range=maxexp) at alpha_dissolve:
        xalign 0.14 yalign 0.15 xmaximum 400 ysize 25 left_bar Frame("images/Bar/XP_full.png") right_bar Frame("images/Bar/XP_empty.png")

    text "{b}HP{/b}" xalign 0.9185 yalign 0.08 style ("white_font") at alpha_dissolve
    bar value AnimatedValue(enemycurhp, range=enemymaxhp) at alpha_dissolve:
        xalign 0.85 yalign 0.08 xmaximum 500 left_bar Frame("images/Bar/HP_full.png") right_bar Frame("images/Bar/HP_empty.png")

#Screen untuk menu
screen menu_frame:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0.5
        xsize 1500
        ysize 850
        background Frame("images/UI/3.png")

#Screen Health
screen healths:
    frame at alpha_dissolve:
        xalign 0.5 yalign 0
        xsize 1980
        ysize 210
        background Frame("images/UI/3.png")
        text "{i}[user] & [sib]{/i}" xalign 0.135 yalign 0.22 font "fonts/rexlia rg.otf"
        text "{i}Lv [lvl]{/i}" xalign 0.35 yalign 0.22 font "fonts/rexlia rg.otf"
        text "{i}[tbType] Time Bandit{/i}" xalign 0.87 yalign 0.22 font "fonts/rexlia rg.otf"
        text "{color=[turndesccol]}[turndesc!u] TURN{/color}" xalign 0.5 yalign 0.5 size 50 font "fonts/rexlia rg.otf"

#Attack Menu
screen moves:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1980
        ysize 360
        background Frame("images/UI/nn.png")
        text "Skill apa yang ingin digunakan?" xalign 0.32 yalign 0.21 color "#000000" font "fonts/rexlia rg.otf" size 30
        vbox:
            xalign 0.23
            yalign 0.82
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

            hbox:
                spacing 0
                button:
                    text "[movename2]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), Hide("displayMoveText"), SetVariable("moveend", movename2), Jump("initmovevar")

                    hovered Show("displayMoveText", displayElement = "[moveDesc2] element", displayDmg = "[moveDmg2] DMG")
                    unhovered Hide("displayMoveText")
                button:
                    text "[movename3]" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("moves"), Hide("displayMoveText"), SetVariable("moveend", movename3), Jump("initmovevar")

                    hovered Show("displayMoveText", displayElement = "[moveDesc3] element", displayDmg = "[moveDmg3] DMG")
                    unhovered Hide("displayMoveText")

screen displayMoveText:
    default displayElement = ""
    default displayDmg = ""
    vbox:
        xalign 0.95
        yalign 0.975
        frame:
            xsize 550
            ysize 200
            background Frame("images/UI/5.png")
            vbox:
                xalign 0.5
                yalign 0.5
                text displayElement color "#FFFFFF"
                text displayDmg color "#FFFFFF"

label initmovevar:
    if moveend == "Low":
        $atk = "Low"
        $elementQuestion = "Low"
        $audio.moveSFX = lowsfx
        $movename = moveend
        $movedmg = Low
        $atkcol = "#e5ff00"

    elif moveend == "Mid":
        $atk = "Mid"
        $elementQuestion = "Mid"
        $audio.moveSFX = Midsfx
        $movename = moveend
        $movedmg = Mid
        $atkcol = "#ff9900"

    elif moveend == "High":
        $atk = "High"
        $elementQuestion = "High"
        $audio.moveSFX = highsfx
        $movename = moveend
        $movedmg = High
        $atkcol = "#ff1900"

    else:
        $atk = "Physical"
        $elementQuestion = "Physical"
        $audio.moveSFX = punchsfx
        $movename = moveend
        $movedmg = Punch
        $atkcol = "#cccccc"
    
    $defe = enemydefe
    jump initTriv
            
screen shield:
    frame at alpha_dissolve:
        xalign 0.5
        yalign 1.02
        xsize 1980
        ysize 360
        background Frame("images/UI/nn.png")
        text "Shield elemen apa yang ingin digunakan?" xalign 0.32 yalign 0.21 color "#000000" font "fonts/rexlia rg.otf" size 30
        vbox:
            xalign 0.23
            yalign 0.82
            spacing 0
            hbox:
                spacing 100
                button:
                    text "Low" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Fire"), SetVariable("atkcol", "#E25822"), SetVariable("defe", "Fire"), Jump("autodmg")
                button:
                    text "Mid" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Wind"), SetVariable("atkcol", "#61ffb0"), SetVariable("defe", "Wind"), Jump("autodmg")
            hbox:
                spacing 100
                button:
                    text "High" xalign 0.5 yalign 0.5 style ("button_font")
                    xysize(500,90)
                    style "move_button"
                    action Hide("shield"), SetVariable("elementQuestion", "Earth"), SetVariable("atkcol", "#b17837"), SetVariable("defe", "Earth"), Jump("autodmg")
            


########################################################################################################################
########################################################Start Here######################################################
########################################################################################################################

#Start Mechanism
#Start battle (called only once from script.rpy)
label battle:
    scene black with Fade(1, 0, 1)
    window hide dissolve
    $save_enabled_state = False
    play music battlebgm fadein 3
    $renpy.pause(2.0,hard=True)
    if bgName == "portal":
        scene bg portal with fade
    
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
        zoom 0.9

    show user biasa at charKanan:
        zoom 1.1

    show sib biasa at charKiri behind user:
        zoom 1.1
    
    with moveinleft

    $renpy.pause(0.5,hard=True)  
    show sib diam biasa with dissolve
    
    $renpy.pause(None,hard=True)   

#Attack Menu
label attackmove:
    window hide dissolve
    call moveinit from _call_moveinit_1
    call moveElement from _call_moveElement_1
    show screen moves
    $renpy.pause(None,hard=True)

label defensemove:
    window hide dissolve
    show screen shield
    $renpy.pause(None,hard=True)

#Trivia gui
label trivia1:
    $ time = 200
    $ timer_range = 200
    $ timer_jump = 'checkquiz1'
    show screen menu_frame
    show screen countdown
    menu:
        "{color=[atkcol]}{b}[elementQuestion] Trivia{/b}{/color}\n
        {color=#FFFFFF}[asks]{/color}" if dummy == True:
            "Oops. How'd you get here?"
        "[answers1]":
            $answercheck = answers1
            jump checkquiz1
        "[answers2]":
            $answercheck = answers2
            jump checkquiz1
        "[answers3]":
            $answercheck = answers3
            jump checkquiz1
        "[answers4]":
            $answercheck = answers4
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
            "Trivia benar! Serangan berhasil!"
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
            "Waktu habis! Serangan gagal menyerang!"
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
            "Trivia salah! Serangan gagal!"
        else:
            "Trivia salah! Perisai gagal digunakan!"

    #Questions Index
    $z +=1
    
    jump checkeffective1

label checkeffective1: #calculates effectiveness of an attack
    call critrate from _call_critrate #look if the attack crits or not

    if turn == False:
        if defe == "None":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"

            if crit == True:
                $truecrit = critdmg1 / 100
                $movedmg *= critdmg[1] * truecrit
                $movedmg = int(movedmg)

            jump attack

    if atk == "Low":
        if defe == "Low":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"

        elif defe == "High":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"

        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "Mid":
        if defe == "Low":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"

        elif defe == "High":
            $multiplier = weak
            $movedmg *= multiplier
            $effectivedesc = "not very effective"

        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    elif atk == "High":
        if defe == "Low":
            $multiplier = supereffective
            $movedmg *= multiplier
            $effectivedesc = "very effective"

        else:
            $multiplier = effective
            $movedmg *= multiplier
            $effectivedesc = "effective"

    
    
    #Physical
    else:
        $multiplier = effective
        $movedmg *= multiplier
        $effectivedesc = "effective"

    #Crit DMG Calculations
    if crit == True:
        $truecrit = critdmg1 / 100
        $movedmg *= critdmg[1] * truecrit
        $movedmg = int(movedmg)
    jump attack



label critrate: #calculates crit
    $crt = renpy.random.randint(1, 20) # 5% Crit rate

    if crt == 5:
        $crit = True
    else:
        $crit = False

    return

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

            play sound moveSFX
            show user attack 
            $renpy.pause(0.2,hard=True)
            show tbx common hit animated
            $renpy.pause(1.8,hard=True)
            show tbx c biasa
            show user biasa

            if dmgto > 0:
                if effectivedesc == "not very effective":
                    "Serangan kurang efektif!"

                elif effectivedesc == "very effective":
                    "Serangan sangat efektif!"

            if crit == True :
                "Serangan kritis!"
            
    
    #elif turn == 2: #sibling turn
        "[sib] membantu [user] melawan Time Bandit."

        $dmgto = playeratk + movedmg - enemydef
        $dmgto *= 0.75
        $dmgto = int(dmgto)
        $enemycurhp -= dmgto

        if enemycurhp <= 0:
            $enemycurhp = 0

        $renpy.restart_interaction()

        play sound punchsfx
        show sib attack
        $renpy.pause(0.2,hard=True)
        show tbx common hit animated
        $renpy.pause(1.8,hard=True)
        show tbx c biasa
        show sib biasa

        if crit == True :
            "Serangan kritis!"
        

    elif turn == 3: #enemy turn
        if defe != "None":
            "Kamu menggunakan perisai [defe]."
        "Time Bandit menggunakan serangan [atk]."

        $dmgto = enemyatk + movedmg - playerdef
        $dmgto = int(dmgto)
        $playercurhp -= dmgto

        if playercurhp <= 0:
            $playercurhp = 0

        $renpy.restart_interaction()
        play sound lasersfx
        show tbx c attack 
        $renpy.pause(0.2,hard=True)
        show user hit animated
        $renpy.pause(1.8,hard=True)
        show tbx c biasa
        show user biasa

        if effectivedesc == "not very effective":
            "Tangkis berhasil menahan elemen! Serangan Time Bandit dilemahkan!"

        elif effectivedesc == "very effective":
            "Tangkis gagal menahan elemen! Serangan Time Bandit lebih efektif!"

        if crit == True :
            "Serangan kritis!"
    

    $movedmg = 0 #reset the move dmg
    $canAttack = False #reset

    #Refresh HP Bar
    $renpy.restart_interaction()

    #Going back to script.rpy if either sides died
    if playercurhp <= 0:
        show sib sedih behind user
        show user sedih
        show tbx c senang
        "Kamu kalah! Time Bandit telah memenangkan pertarungan."
        $curexp -= 15

        if curexp <= 0:
            $curexp = 0
        "Kamu kehilangan 15 EXP karena telah kalah melawan Time Bandit."

        $renpy.restart_interaction()
        $renpy.pause(2.0,hard=True)

        $Hide("hpbar", transition=Dissolve(1.0))()
        $Hide("healths", transition=Dissolve(1.0))()

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
        show sib senang behind user 
        show user senang
        show tbx c marah
        
        "Kamu menang! Time Bandit berhasil dikalahkan."
        

        call xpgain from _call_xpgain

        

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
            show user biasa at charKiri behind sib
            show sib diam biasa at charKanan
            with move

            show user diam biasa
            show sib biasa
            with dissolve

            jump sibAttack

        else:
            show sib biasa at charKiri behind user
            show user diam biasa at charKanan
            with move

            show sib diam biasa 
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
    
label autodmg: #for enemy atk dmg (dmg randomized according to x min and y max range)
    $movedmg = renpy.random.randint(x, y)
    $a = renpy.random.randint(0,4)
    $atk = atklist[a]
    jump initTrivDef

label sibAttack:
    $movedmg = renpy.random.randint(30, 50)
    $atk = "Physical"
    jump checkeffective1

label switch: #switch turn
    $renpy.pause(1.0,hard=True) #for damage animation interval

    if turn == 1:
        $turn = 2
        $turndesc = sib
        $turndesccol = "#261ac2"

    elif turn == 2:
        $turn = 3
        $turndesc = "ENEMY"
        $turndesccol = "#a13e3e"
        
    
    else:
        $turn = 1
        $turndesc = "YOUR"
        $turndesccol = "#81ee57"
        $defe = enemydefe

    return

label xpgain:
    $curexp += 25 + 3*expmulti
    $curexp = int(curexp)
    $expNum = 25 + 3*expmulti
    $expNum = int(expNum)
    "Kamu mendapatkan [expNum] EXP karena telah memenangkan pertarungan."
    if curexp >= maxexp:
        $curexp = maxexp
        $lvl += 1
        $curexp = 0
        $renpy.restart_interaction()
        $maxexp *= 1.2
        $maxexp = int(maxexp)
        call apgain from _call_apgain
        "Kamu telah naik ke level [lvl]! Kamu mendapat [bonusap] AP."
    return

label apgain:
    if lvl % 5 == 0:
        $bonusap +=1
    $curap += bonusap
    $maxap = curap
    return