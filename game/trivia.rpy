# Trivia Bank

define question = 1
define PLdamage = []
define PMdamage = []
define PHdamage = []
define PLdefense = []
define PMdefense = []
define PHdefense = []
define Triv =""
# define fireTriv = trivListEl[0]
# define windTriv = trivListEl[1]
# define earthTriv = trivListEl[2]
# define waterTriv = trivListEl[3]
# define physTriv = trivListPhys[0]
define typeQuestion = ""
define foundQuestion = False
define ind = -1 #index
define indPhys = 0

define color0 = ""
define color1 = ""
define color2 = ""
define color3 = ""

label randomtriv:
    $renpy.random.shuffle(PLdamage)
    $renpy.random.shuffle(PMdamage)
    $renpy.random.shuffle(PHdamage)
    $renpy.random.shuffle(PLdefense)
    $renpy.random.shuffle(PMdefense)
    $renpy.random.shuffle(PHdefense)
    return

label initTriv:
    

    # Pastikan indeks mulai dari awal jika sudah melebihi panjang daftar
    if atk == "Ldamage":
        if ind >= len(PLdamage):
            $ ind = 0
        $ Triv = PLdamage[ind]
        $ foundQuestion = True
    elif atk == "Mdamage":
        if ind >= len(PMdamage):
            $ ind = 0
        $ Triv = PMdamage[ind]
        $ foundQuestion = True
    elif atk == "Hdamage":
        if ind >= len(PHdamage):
            $ ind = 0
        $ Triv = PHdamage[ind]
        $ foundQuestion = True

    $ ind += 1  # Pindah ke soal berikutnya di daftar acak
    $ foundQuestion = False
    jump trivia

label initTrivDef:
    
    if defe == "Ldefense":
        if ind >= len(PLdefense):
            $ ind = 0
        $ Triv = PLdefense[ind]
    elif defe == "Mdefense":
        if ind >= len(PMdefense):
            $ ind = 0
        $ Triv = PMdefense[ind]
    elif defe == "Hdefense":
        if ind >= len(PHdefense):
            $ ind = 0
        $ Triv = PHdefense[ind]
        $ foundQuestion = True

    $ ind += 1  # Pindah ke soal berikutnya
    $ foundQuestion = False
    jump trivia

label trivia:
    $ quizquestion = Triv
    $ asks = quizquestion["question"]
    $ answers = quizquestion["answer"]
    $ corrects = quizquestion["correct"]
    $ renpy.random.shuffle(answers) #reshuffle answers
    $ answers1 = answers[0]
    $ answers2 = answers[1]
    $ answers3 = answers[2]
    $ answers4 = answers[3]
    $ answercheck = ""

    if answers1 == corrects:
        $color0 = "#00FF00"
        $color1 = "#FF0000"
        $color2 = "#FF0000"
        $color3 = "#FF0000"
    elif answers2 == corrects:
        $color0 = "#FF0000"
        $color1 = "#00FF00"
        $color2 = "#FF0000"
        $color3 = "#FF0000"
    elif answers3 == corrects:
        $color0 = "#FF0000"
        $color1 = "#FF0000"
        $color2 = "#00FF00"
        $color3 = "#FF0000"
    elif answers4 == corrects:
        $color0 = "#FF0000"
        $color1 = "#FF0000"
        $color2 = "#FF0000"
        $color3 = "#00FF00"

    jump trivia1




init:
    $ timer_range = 0
    $ timer_jump = 0
    
init python:
    PLdamage=[
        # 1-10 IPA
        {"question" : "Proses yang disertai dengan pertambahan berat, besar, dan tinggi pada makhluk hidup disebut ...", 
        "answer" : ["Pertambahan", "Penggemukan", "Pertumbuhan", "Berkembang biak"], 
        "correct" : "Pertumbuhan",
        "type" : "ipa"},

        {"question" : "Alat perkembangbiakan generatif pada tumbuhan berupa ...", 
        "answer" : ["Bunga", "Batang", "Daun", "Akar"], 
        "correct" : "Bunga",
        "type" : "ips"},
        
        {"question" : "Hewan yang bekembangbiakan dengan cara bertelur adalah", 
        "answer" : ["Angsa, itik, dan bebek", "Bebek, angsa, dan kelinci", "Ayam, hiu, dan cecak", "Kera, bebek, dan ayam"], 
        "correct" : "Angsa, itik, dan bebek",
        "type" : "b indo"},
        
        {"question" : "Burung elang berkembang biak dengan cara bertelur. Berarti, burung elang mengalami perkembangbiakan secara ...", 
        "answer" : ["Vegetatif", "Membelah diri", "Spora", "Generatif"], 
        "correct" : "Generatif",
        "type" : "ipa"},

        {"question" : "Perkembangbiakan secara bertelur dan beranak disebut juga dengan perkembangbiakan ...", 
        "answer" : ["Spora", "Ovipar", "Vivipar", "Ovovivipar"], 
        "correct" : "Ovovivipar",
        "type" : "ipa"}]
    PMdamage=[
        {"question" : "Hewan yang berkembang biak secara ovipar adalah ...", 
        "answer" : ["Kadal, hiu, dan ular", "Ayam, hiu, dan lumba-lumba", "Ayam, bebek, dan angsa", "Kambing, sapi, dan kelinci"], 
        "correct" : "Ayam, bebek, dan angsa",
        "type" : "ipa"},

        {"question" : "Sel kelamin betina yang terdapat pada bunga disebut ...", 
        "answer" : ["Kelopak", "Benang sari", "Mahkota", "Putik"], 
        "correct" : "Putik",
        "type" : "ipa"},

        {"question" : "Bambu berkembang biak dengan ...", 
        "answer" : ["Spora", "Rhizoma", "Tunas", "Tunas adventif"], 
        "correct" : "Tunas",
        "type" : "ipa"},

        {"question" : "Salah satu tumbuhan yang berkembang biak dengan umbi lapis yaitu ...", 
        "answer" : ["Rumput teki", "Sukun", "Bawang Merah", "Ubi jalar"], 
        "correct" : "Bawang Merah",
        "type" : "ipa"},

        # 10 - 20
        {"question" : "Serbuk sari yang jatuh ke kepala putik yang berasal dari bunga itu sendiri disebut penyerbukan ...", 
        "answer" : ["Silang", "Sendiri", "Tetangga", "Bastar"], 
        "correct" : "Sendiri",
        "type" : "ipa"}]
    PHdamage=[
        {"question" : "Perkembangbiakan generatif pada tumbuhan hanya bisa terjadi pada tumbuhan yang memiliki ...", 
        "answer" : ["Akar", "Bunga", "Daun", "Batang"], 
        "correct" : "Bunga",
        "type" : "ipa"},

        {"question" : "Berikut ini merupakan perkembangbiakan vegetatif alami adalah ...", 
        "answer" : ["Mencangkok", "Stek", "Umbi Batang", "Okulasi"], 
        "correct" : "Umbi Batang",
        "type" : "ipa"},

        {"question" : "Berikut adalah bagian-bagian yang terdapat pada bunga, kecuali ...", 
        "answer" : ["Putik", "Mahkota bunga", "Kepala sari", "Kelopak bunga"], 
        "correct" : "Kepala sari",
        "type" : "ipa"},

        {"question" : "Alat kelamin jantan pada bunga adalah ...", 
        "answer" : ["Benang sari", "Putik", "Mahkota bunga", "Benang mahkota"], 
        "correct" : "Benang sari",
        "type" : "ipa"},

        {"question" : "Penyerbukan yang terjadi jika serbuk sari yang jatuh di atas kepala putik berasal dari tanaman yang berbeda tetapi masih satu jenis dinamakan penyebukan ...", 
        "answer" : ["Sendiri", "Tetangga", "Silang", "Bartas"], 
        "correct" : "Silang",
        "type" : "ipa"}]

    PLdefense =[
        {"question" : "Proses yang disertai dengan pertambahan berat, besar, dan tinggi pada makhluk hidup disebut ...", 
        "answer" : ["Pertambahan", "Penggemukan", "Pertumbuhan", "Berkembang biak"], 
        "correct" : "Pertumbuhan",
        "type" : "ipa"},

        {"question" : "Alat perkembangbiakan generatif pada tumbuhan berupa ...", 
        "answer" : ["Bunga", "Batang", "Daun", "Akar"], 
        "correct" : "Bunga",
        "type" : "ipa"},
        
        {"question" : "Hewan yang bekembangbiakan dengan cara bertelur adalah", 
        "answer" : ["Angsa, itik, dan bebek", "Bebek, angsa, dan kelinci", "Ayam, hiu, dan cecak", "Kera, bebek, dan ayam"], 
        "correct" : "Angsa, itik, dan bebek",
        "type" : "ipa"},
        
        {"question" : "Burung elang berkembang biak dengan cara bertelur. Berarti, burung elang mengalami perkembangbiakan secara ...", 
        "answer" : ["Vegetatif", "Membelah diri", "Spora", "Generatif"], 
        "correct" : "Generatif",
        "type" : "ipa"},

        {"question" : "Perkembangbiakan secara bertelur dan beranak disebut juga dengan perkembangbiakan ...", 
        "answer" : ["Spora", "Ovipar", "Vivipar", "Ovovivipar"], 
        "correct" : "Ovovivipar",
        "type" : "ipa"}]    
    PMdefense=[
        {"question" : "Hewan yang berkembang biak secara ovipar adalah ...", 
        "answer" : ["Kadal, hiu, dan ular", "Ayam, hiu, dan lumba-lumba", "Ayam, bebek, dan angsa", "Kambing, sapi, dan kelinci"], 
        "correct" : "Ayam, bebek, dan angsa",
        "type" : "ipa"},

        {"question" : "Sel kelamin betina yang terdapat pada bunga disebut ...", 
        "answer" : ["Kelopak", "Benang sari", "Mahkota", "Putik"], 
        "correct" : "Putik",
        "type" : "ipa"},

        {"question" : "Bambu berkembang biak dengan ...", 
        "answer" : ["Spora", "Rhizoma", "Tunas", "Tunas adventif"], 
        "correct" : "Tunas",
        "type" : "ipa"},

        {"question" : "Salah satu tumbuhan yang berkembang biak dengan umbi lapis yaitu ...", 
        "answer" : ["Rumput teki", "Sukun", "Bawang Merah", "Ubi jalar"], 
        "correct" : "Bawang Merah",
        "type" : "ipa"},

        # 10 - 20
        {"question" : "Serbuk sari yang jatuh ke kepala putik yang berasal dari bunga itu sendiri disebut penyerbukan ...", 
        "answer" : ["Silang", "Sendiri", "Tetangga", "Bastar"], 
        "correct" : "Sendiri",
        "type" : "ipa"}]

    PHdefense=[
        {"question" : "Perkembangbiakan generatif pada tumbuhan hanya bisa terjadi pada tumbuhan yang memiliki ...", 
        "answer" : ["Akar", "Bunga", "Daun", "Batang"], 
        "correct" : "Bunga",
        "type" : "ipa"},

        {"question" : "Berikut ini merupakan perkembangbiakan vegetatif alami adalah ...", 
        "answer" : ["Mencangkok", "Stek", "Umbi Batang", "Okulasi"], 
        "correct" : "Umbi Batang",
        "type" : "ipa"},

        {"question" : "Berikut adalah bagian-bagian yang terdapat pada bunga, kecuali ...", 
        "answer" : ["Putik", "Mahkota bunga", "Kepala sari", "Kelopak bunga"], 
        "correct" : "Kepala sari",
        "type" : "ipa"},

        {"question" : "Alat kelamin jantan pada bunga adalah ...", 
        "answer" : ["Benang sari", "Putik", "Mahkota bunga", "Benang mahkota"], 
        "correct" : "Benang sari",
        "type" : "ipa"},]