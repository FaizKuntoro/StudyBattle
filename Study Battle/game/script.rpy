# Study battle Alpha.

# main character.
define arisa = Character ("Arisa", color="#f6ff00", who_bold=True, who_outlines=[(1, "#000")])
define intro = Character("", color="#B6AAA6", window_yalign=0.5,who_bold=True, who_outlines=[(1, "#000")])


# enemy
define cakra = Character("Cakra", color="#ff4800", who_bold=True, who_outlines=[(1, "#000")])
define brian = Character("Brian", color="#ff4800", who_bold=True, who_outlines=[(1, "#000")])
define azizah = Character("Azizah", color="#ff4800", who_bold=True, who_outlines=[(1, "#000")])

#npc
define dosen = Character("Ibu Ratna", color="#be8c02", who_bold=True, who_outlines=[(1, "#000")])
define ilham = Character("Ilham", color="#00fae9", who_bold=True, who_outlines=[(1, "#000")])


# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)
# Hold at black for a bit.
define fadehold = Fade(0.5, 1.0, 0.5)
# Camera flash - quickly fades to white, then back to the scene.
define whiteflash = Fade(0.1, 0.0, 0.5, color="#fff")
define redflash = Fade(0.1, 0.0, 0.5, color="#f00")


# image arisa
image arisa datar = im.FactorScale("Character/Arisa/datar1.png",0.40)
image arisa senang = im.FactorScale("Character/Arisa/senang1.png",0.40)
image arisa sedih = im.FactorScale("Character/Arisa/sedih1.png",0.40)
image arisa marah = im.FactorScale("Character/Arisa/marah1.png",0.40)
image arisa gugup = im.FactorScale("Character/Arisa/gugup1.png",0.40)
image arisa senang2 = im.FactorScale("Character/Arisa/senang2.png",0.40)
image arisa marah2 = im.FactorScale("Character/Arisa/marah2.png",0.40)
image arisa datar2 = im.FactorScale("Character/Arisa/datar2.png",0.40)
image arisa datar3 = im.FactorScale("Character/Arisa/datar3.png",0.40)
image arisa senang3 = im.FactorScale("Character/Arisa/senang3.png",0.40)
image arisa sedih3 = im.FactorScale("Character/Arisa/sedih3.png",0.40)
image arisa marah3 = im.FactorScale("Character/Arisa/marah3.png",0.40)
image arisa gugup3 = im.FactorScale("Character/Arisa/gugup3.png",0.40)

image arisa diam datar = im.FactorScale("Character/Arisa/Diam/datar.png",0.40)
image arisa diam senang = im.FactorScale("Character/Arisa/Diam/senang.png",0.40)
image arisa diam sedih = im.FactorScale("Character/Arisa/Diam/sedih.png",0.40)
image arisa diam marah = im.FactorScale("Character/Arisa/Diam/marah.png",0.40)
image arisa diam gugup = im.FactorScale("Character/Arisa/Diam/gugup.png",0.40)
image arisa diam senang2 = im.FactorScale("Character/Arisa/Diam/senang2.png",0.40)
image arisa diam marah2 = im.FactorScale("Character/Arisa/Diam/marah2.png",0.40)
image arisa diam datar2 = im.FactorScale("Character/Arisa/Diam/datar2.png",0.40)
image arisa diam datar3 = im.FactorScale("Character/Arisa/Diam/datar3.png",0.40)
image arisa diam senang3 = im.FactorScale("Character/Arisa/Diam/senang3.png",0.40)
image arisa diam sedih3 = im.FactorScale("Character/Arisa/Diam/sedih3.png",0.40)
image arisa diam marah3 = im.FactorScale("Character/Arisa/Diam/marah3.png",0.40)
image arisa diam gugup3 = im.FactorScale("Character/Arisa/Diam/gugup3.png",0.40)

# image ilham
image ilham datar = im.FactorScale("Character/Ilham/datar.png",0.40)
image ilham senang = im.FactorScale("Character/Ilham/senang.png",0.40)
image ilham sedih = im.FactorScale("Character/Ilham/sedih.png",0.40)
image ilham marah = im.FactorScale("Character/Ilham/marah.png",0.40)
image ilham hah = im.FactorScale("Character/Ilham/hah.png",0.40)
image ilham gugup = im.FactorScale("Character/Ilham/gugup.png",0.40)

image ilham diam datar = im.FactorScale("Character/Ilham/Diam/datar.png",0.40)
image ilham diam senang = im.FactorScale("Character/Ilham/Diam/senang.png",0.40)
image ilham diam sedih = im.FactorScale("Character/Ilham/Diam/sedih.png",0.40)
image ilham diam marah = im.FactorScale("Character/Ilham/Diam/marah.png",0.40)
image ilham diam hah = im.FactorScale("Character/Ilham/Diam/hah.png",0.40)
image ilham diam gugup = im.FactorScale("Character/Ilham/Diam/gugup.png",0.40)


# image Dosen
image dosen datar = im.FactorScale("Character/Dosen/datar.png",0.40)
image dosen senang = im.FactorScale("Character/Dosen/senang.png",0.40)
image dosen sedih = im.FactorScale("Character/Dosen/sedih.png",0.40)
image dosen gugup = im.FactorScale("Character/Dosen/gugup.png",0.40)

image dosen diam biasa = im.FactorScale("Character/Dosen/Diam/datar.png",0.40)
image dosen diam senang = im.FactorScale("Character/Dosen/Diam/senang.png",0.40)
image dosen diam sedih = im.FactorScale("Character/Dosen/Diam/sedih.png",0.40)
image dosen diam gugup = im.FactorScale("Character/Dosen/Diam/gugup.png",0.40)

# image cakra
image cakra datar = im.FactorScale("Character/Cakra/datar.png",0.40)
image cakra senang = im.FactorScale("Character/Cakra/senang.png",0.40)
image cakra sedih = im.FactorScale("Character/Cakra/sedih.png",0.40)
image cakra marah = im.FactorScale("Character/Cakra/marah.png",0.40)
image cakra hah = im.FactorScale("Character/Cakra/hah.png",0.40)
image cakra gugup = im.FactorScale("Character/Cakra/gugup.png",0.40)

image cakra diam datar = im.FactorScale("Character/Cakra/Diam/datar.png",0.40)
image cakra diam senang = im.FactorScale("Character/Cakra/Diam/senang.png",0.40)
image cakra diam sedih = im.FactorScale("Character/Cakra/Diam/sedih.png",0.40)
image cakra diam marah = im.FactorScale("Character/Cakra/Diam/marah.png",0.40)
image cakra diam hah = im.FactorScale("Character/Cakra/Diam/hah.png",0.40)
image cakra diam gugup = im.FactorScale("Character/Cakra/Diam/gugup.png",0.40)


# image brian
image brian datar = im.FactorScale("Character/Brian/datar.png",0.40)
image brian senang = im.FactorScale("Character/Brian/senang.png",0.40)
image brian sedih = im.FactorScale("Character/Brian/sedih.png",0.40)
image brian marah = im.FactorScale("Character/Brian/marah.png",0.40)
image brian hah = im.FactorScale("Character/Brian/hah.png",0.40)
image brian gugup = im.FactorScale("Character/Brian/gugup.png",0.40)

image brian diam datar = im.FactorScale("Character/Brian/Diam/datar.png",0.40)
image brian diam senang = im.FactorScale("Character/Brian/Diam/senang.png",0.40)
image brian diam sedih = im.FactorScale("Character/Brian/Diam/sedih.png",0.40)
image brian diam marah = im.FactorScale("Character/Brian/Diam/marah.png",0.40)
image brian diam hah = im.FactorScale("Character/Brian/Diam/hah.png",0.40)
image brian diam gugup = im.FactorScale("Character/Brian/Diam/gugup.png",0.40)


# image azizah
image azizah datar = im.FactorScale("Character/Azizah/datar.png",0.40)
image azizah senang = im.FactorScale("Character/Azizah/senang.png",0.40)
image azizah sedih = im.FactorScale("Character/Azizah/sedih.png",0.40)
image azizah marah = im.FactorScale("Character/Azizah/marah.png",0.40)
image azizah hah = im.FactorScale("Character/Azizah/hah.png",0.40)
image azizah gugup = im.FactorScale("Character/Azizah/gugup.png",0.40)

image azizah diam datar = im.FactorScale("Character/Azizah/Diam/datar.png",0.40)
image azizah diam senang = im.FactorScale("Character/Azizah/Diam/senang.png",0.40)
image azizah diam sedih = im.FactorScale("Character/Azizah/Diam/sedih.png",0.40)
image azizah diam marah = im.FactorScale("Character/Azizah/Diam/marah.png",0.40)
image azizah diam hah = im.FactorScale("Character/Azizah/Diam/hah.png",0.40)
image azizah diam gugup = im.FactorScale("Character/Azizah/Diam/gugup.png",0.40)


#flip
image arisa biasa flip= im.Flip("Character/Arisa/biasa.png", horizontal=True)
image arisa senang flip= im.Flip("Character/Arisa/senang.png", horizontal=True)
image arisa lesu flip= im.Flip("Character/Arisa/lesu.png", horizontal=True)


image arisa diam biasa flip= im.Flip("Character/Arisa/Diam/biasa.png", horizontal=True)
image arisa diam senang flip= im.Flip("Character/Arisa/Diam/senang.png", horizontal=True)
image arisa diam lesu= im.Flip("Character/Arisa/Diam/lesu.png", horizontal=True)

# bg
image bg menu = im.FactorScale("Background/menu.png",0.30)
image bg kantor = im.FactorScale("Background/kantor.png",0.30)
image bg kelas = im.FactorScale("Background/kelas.png",0.30)
image bg perpus = im.FactorScale("Background/perpus.png",0.30)
image bg panggung = im.FactorScale("Background/panggung.png",0.30)
image bg aula = im.FactorScale("Background/aula.png",0.30)

image splashStudyBattle = "Studybattle.jpg"
image splashPMGD = im.FactorScale("pmgd.jpg",0.60)

# audio
define audio.santai="audio/santai.mp3"
define audio.panik="audio/panik.mp3"
define audio.menang="audio/menang.mp3"
define audio.kalah="audio/kalah.mp3"
define audio.battle="audio/battle.mp3"

#style game_tb:
    ##hover_background Frame("images/button_hover.png")

####zoom 0.75

label splashscreen:
    scene black
    $renpy.pause(1.0, hard=True)
    scene splashStudyBattle with Dissolve(2.0)
    $renpy.pause(2.0, hard=True)
    scene black with dissolve
    $renpy.pause(1.0, hard=True)
    scene splashPMGD with Dissolve(2.0)
    $renpy.pause(2.0, hard=True)
    scene black with dissolve
    $renpy.pause(1.0, hard=True)
    return

define dismissTime = 1
screen noDismiss:
    key 'dismiss' action NullAction()
    timer 1 repeat True action If(dismissTime > 0, true=SetVariable('dismissTime', dismissTime - 1), false=[Hide('noDismiss')])

# Game dimulai disini.
label start:
    scene expression "#000"
    with Dissolve(1.0)
    # action Preference("auto-forward", "disable")
#################################################################################
# SEQUENCE 01 - PROLOG
#################################################################################
label scene_1:
    scene bg kantor with fade
    play music "audio/ambient_office.mp3" fadein 2.0

    show arisa datar at left
    arisa "(Ekspresi datar) Selamat siang, Bu. Ini tentang nilai saya ya?"
    intro "Arisa menutup pintu di belakangnya sambil menatap ruangan di depannya."
    intro "Beberapa kali ia telah dipanggil ke kantor dosen saat ini, apalagi karena sudah mendekati akhir semester."

    show dosen datar at right
    dosen "(Ekspresi datar) Iya, silahkan duduk."
    intro "Arisa duduk di depan meja, menghadap langsung Ibu Ratna."
    intro "Entah kenapa kali ini terasa berbeda dengan suasana di ruangan dosen lain, padahal kursinya sama."
    intro "Nyaman dan empuk."
    intro "Itu membuatnya gugup."

    dosen "Seperti yang mungkin sudah kamu tau, nilaimu di kelas saya itu…"
    show arisa gugup at left
    arisa "(Ekspresi penasaran) Gak bagus ya, Bu?"
    show dosen senang at right
    dosen "(Ekspresi senang) Kita anggap aja bukan yang terbaik, ya."
    show arisa sedih at left
    arisa "(Ekspresi kecewa) Nilai saya C ya?"
    show dosen datar at right
    dosen "(Ekspresi datar) Iya, kamu dapat C."
    show arisa sedih at left 
    arisa "(Ekspresi sedih) Yah."
    dosen "Tapi, saya ada caranya kok agar kamu bisa dapat nilai ekstra di kelas saya."
    arisa "Gimana, Bu?"

    show dosen senang at right
    dosen "Nah, kamu itu kan, mahasiswa yang cerdas, Arisa."
    dosen "Dan saya tahu kamu itu tidak terlalu aktif di kelas dan kadang-kadang juga alfa."
    dosen "Itu gapapa. Saya ngerti kok kalau kamu itu cuma–"
    show arisa marah at left
    arisa "(Ekspresi frustasi) Gak ada motivasi, burnt out, capek, Bu."
    show dosen datar at right
    dosen "(Ekspresi datar) Iya."
    show dosen senang at right
    dosen "(Ekspresi senang) Tapi kamu itu tetap mahasiswa yang cerdas, dan saya tahu kamu bisa lebih baik lagi."

    show arisa datar
    arisa "Bu, maaf tapi bisa to the point aja, gak?"
    dosen "Ya sudah, ini kan ada kompetisi pengetahuan umum di kampus sebelah, dan kalau kamu menang, atau bahkan mendapat juara ketiga aja, saya akan memberi kamu nilai tambahan."
    show arisa gugup
    arisa "(Ekspresi terkejut) Itu aja, Bu?"
    dosen "Iya, kamu punya waktu setidaknya dua minggu untuk belajar."
    show arisa senang
    arisa "(Ekspresi senang) Oh, oke. Makasih, Bu."

    intro "Arisa menggeser kursinya agar ia dapat bangkit, siap dan bersemangat untuk keluar dari ruangan sempit itu."

    dosen "Tunggu dulu, saya belum selesai ini."
    show arisa gugup
    arisa "(Ekspresi bingung) Oh, um, kenapa lagi, Bu?"
    dosen "Saya sudah menghubungi teman sekelasmu, Ilham Yudhistira Prayoga, yang rajin itu, untuk membantu kamu belajar untuk kompetisi ini."
    arisa "Lah, kenapa, Bu? Saya kan, bisa belajar sendiri."
    dosen "Akan lebih baik kalau kamu punya teman yang bisa mendukung kamu."
    show dosen senang
    dosen "(Ekspresi senang) Dan saya sudah bilang ke dia buat mengawasi kamu, hanya untuk memastikan kalau kamu betul-betul niat buat melakukan ini."
    show dosen datar
    dosen "(Ekspresi datar) Saya tidak akan memberikan nilai ekstra jika kamu itu cuma setengah-setengah."
    show arisa datar
    arisa "Baiklah kalau begitu, Bu, Saya ngerti."
    show dosen senang
    dosen "Oke, ini kontaknya, kamu bisa tanya langsung ke Ilham tentang kompetisinya."
    dosen "Ya sudah, itu aja, kamu boleh pergi sekarang. Belajar dengan giat dan semangat, ya."
    arisa "Iya, saya pamit dulu. Terima kasih, Bu."

    intro "Arisa keluar dari kantor yang dingin itu, mendengus kesal sambil menatap nama kontak Ilham Yudhistira Prayoga di ponselnya."
    intro "Dongkol, dia mematikan ponselnya dan berjalan pergi, berniat untuk tidak berkomunikasi dengan orang yang seharusnya menjadi teman belajarnya."


label scene2_library:
    scene bg perpus with dissolve
    with fade

    # Narasi pembukaan
    intro "Anggreani mengambil buku cetak pertama yang menarik perhatiannya dari ratusan buku yang tersusun rapi dalam rak-rak di sekitarnya."
    intro "Pelan-pelan, dia membuka lembaran pertama, membaca sekilas daftar isinya sebelum jarinya bergerak ke bab satu."
    intro "Topik pertama: teks eksposisi."

    # Dialog Anggreani
    show arisa datar at center
    arisa "Oke, gampang ini."

    # Narasi
    intro "Meskipun berkata seperti itu, Anggreani berkali-kali mengulang bacaannya."
    intro "Paragraf satu. Paragraf dua. Paragraf satu lagi. Paragraf tiga. Paragraf dua lagi."
    intro "Sampai dia frustrasi dan lelah sendiri."

    show arisa marah at center
    arisa "Duh, ini gimana sih?"

    intro "Anggreani menekan kepalanya ke halaman buku sambil merintih."
    intro "Dia sudah lama tidak duduk dan belajar, terlihat dari perjuangan tak bersuaranya untuk tetap fokus ke kata-kata di depannya."
    intro "Putus asa, dia beranjak berdiri untuk mengambil buku lain, tetapi seseorang menghampirinya dan membuatnya berhenti."

    # Kemunculan Ilham
    show ilham datar at center
    ilham "Permisi, Anggreani."

    show arisa bingung at center
    arisa "Kamu siapa ya?"

    intro "Anggreani sebenarnya sudah tahu dia siapa."
    intro "Pastinya si teman belajarnya yang tidak pernah berhenti menelepon dan mengirim teks."

    show ilham senang at center
    ilham "Masa sekelas kamu gak tahu? Pelupa ya?"

    show arisa datar at center
    arisa "Enggak kok."

    show ilham senang at center
    ilham "Anyway, aku Ilham, yang disuruh Bu Ratna temenin kamu belajar."

    arisa "Oh, Ilham itu kamu ya."

    show ilham datar at center
    ilham "Iya. Eh, kamu lagi belajar?"
    show ilham senang at center
    ilham "Aku join juga kalau gitu."

    # Ilham duduk dan mulai belajar
    intro "Ilham duduk di kursi sebelah Anggreani dengan antusias, membuka tasnya untuk mengambil buku catatan dan pulpennya."
    intro "Anggreani belum pernah melihat seseorang begitu bersemangat untuk menuntut ilmu."
    intro "Itu membuatnya penasaran."

    show arisa bingung at center
    arisa "Kamu… suka belajar ya? Kenapa?"

    show ilham datar at center
    ilham "Ya, karena menurutku belajar itu simpel."
    ilham "It’s a one-way street dan lebih gampang untuk diduga-duga."
    show ilham sedih at center
    ilham "Gak kayak bersosialisasi."
    show ilham datar at center
    ilham "Tapi memang sih kalau pertama kali rasanya itu susah, apalagi kalau kamu gak tahu tipe pembelajaran mana yang kamu lebih suka."
    ilham "Aku itu untungnya fleksibel jadi gapapa kalau baca buku, dengerin penjelasan dosen, atau nonton video pembelajaran."
    ilham "Tapi pada akhirnya belajar itu cuma kegiatan untuk menyerap informasi, apapun itu."
    show ilham senang at center
    ilham "Kamu dengerin aku bicara aja bisa dibilang belajar."

    show arisa datar at center
    arisa "Oh ya? Belajar bahasa ya?"

    ilham "Bukan, belajar mendengar."

    # Narasi tambahan
    intro "Anggreani malah tambah jengkel, tetapi dia masih berusaha untuk sabar."
    intro "Kalau Ilham bisa sabar saat panggilan telepon dan pesannya diabaikan, Anggreani pastinya bisa sabar menghadapinya dan kecanggungan candaannya juga."

    arisa "Ya udah, ini belajarnya gimana?"

    show ilham datar at center
    ilham "Bagaimana kalau kita pre-test dulu? Supaya aku tahu kamu itu dasarnya di mana sekarang dan belajarnya gak ngulang-ngulang."

    arisa "Okelah. Bisa, bisa."

    # Panggil tutorial stage atau quis
    #return tutorial_stage

label scene3_library:
    # Background perpustakaan
    scene bg perpus with dissolve

    # Percakapan awal
    show ilham senang at center
    ilham "Hm, lumayan sih."
    show arisa datar at center
    arisa "Lumayan apaan?"
    show ilham senang at center
    ilham "Lumayan aja."
    show arisa datar at center
    arisa "Gak jelas."

    # Narasi
    intro "Arisa menatap Ilham dengan tajam, seolah-olah mencoba memahaminya dan tujuannya."
    intro "Dia tampaknya sangat bersikeras untuk menjadi teman belajarnya, meskipun Arisa sudah mengabaikan panggilan dan pesannya berkali-kali."
    intro "Entah mengapa."

    # Dialog tentang metode belajar
    show arisa datar at center
    arisa "Kamu biasanya belajar gimana sih?"
    show ilham datar at center
    ilham "Kan tadi udah bilang, proses belajar aku tuh fleksibel."
    ilham "Kalau kamu gimana? Lebih suka mendengar, membaca, bergerak, atau bicara?"

    # Pilihan metode belajar
    menu:
        "Mendengar":
            $ learning_type = "mendengar"
            show arisa senang at center
            arisa "Aku sukanya mendengar."
            ilham "Oh, okeh. Kalau begitu coba deh cari podcast atau video pembelajaran yang sesuai dengan topikmu."
        "Membaca":
            $ learning_type = "membaca"
            show arisa senang at center
            arisa "Aku sukanya membaca."
            ilham "Oh, okeh. Kalau begitu fokus aja ke buku-buku referensi. Cari yang bahasanya kamu ngerti."
        "Bergerak":
            $ learning_type = "bergerak"
            show arisa senang at center
            arisa "Aku sukanya bergerak."
            ilham "Oh, okeh. Coba deh belajar sambil praktek langsung atau pakai metode mind-mapping."
        "Bicara":
            $ learning_type = "bicara"
            show arisa senang at center
            arisa "Aku sukanya bicara."
            ilham "Oh, okeh. Kalau begitu coba belajar sambil diskusi sama teman atau presentasiin materi."

    # Lanjutan percakapan
    show arisa datar at center
    arisa "Hm, gitu ya, menarik."
    show ilham senang at center
    ilham "Iya, kan?"
    intro "Arisa mengangguk setuju, meskipun nada bicaranya datar, masih sibuk menerka-nerka kenapa Ilham masih meladeninya."

    show arisa datar at center
    arisa "Kamu kenapa ngotot banget buat belajar sama-sama?"
    show ilham datar at center
    ilham "Aku disuruh Ibu Ratna."
    show arisa datar at center
    arisa "Iya, aku tau, Ibu Ratna udah bilang."
    arisa "Tapi kenapa peduli banget gitu? Sampai menelpon berkali-kali?"
    ilham "Kalo itu…"
    arisa "Ikut lomba juga, ya?"
    ilham "Enggak. Aku enggak berani ikut lomba-lombaan."
    arisa "Oh, ini buat baikin nilai kamu ya?"
    ilham "Bukan, nilaiku itu masih oke-oke aja."
    arisa "Lah, terus?"

    # Pengakuan Ilham
    intro "Arisa diam saat melihat Ilham menghela napas dengan ekspresi gusar, tangannya bergetar saat dia meletakkannya di atas buku yang terbuka di depannya."
    show ilham marah at center
    ilham "Aku ini… sebenarnya…"
    ilham "Gak pinter bersosialisasi."
    show arisa datar at center
    arisa "Hah?"
    intro "Entah mengapa Arisa memprediksi hal yang jauh lebih rumit daripada hal itu."
    intro "Tapi jawaban Ilham tetap membuatnya bingung."

    # Penjelasan lebih lanjut
    show arisa datar at center
    arisa "Itu apa hubungannya sama aku?"
    ilham "Jadi gini, Ibu Ratna milih aku buat belajar sama kamu itu karena dia pikir kita bisa sama-sama memanfaatkan situasi ini."
    ilham "Kamu dapat nilai tambah."
    ilham "Terus aku belajar gimana caranya socialize dengan lebih baik."
    show arisa datar at center
    arisa "Oh, gitu ya."

    # Penutup dan transisi
    intro "Keingintahuan Arisa malah semakin menjadi-jadi."
    intro "Namun rasanya tidak sopan untuk memintanya menjelaskan lebih lanjut."
    intro "Apalagi setelah Arisa sebelumnya sudah mengabaikan upayanya untuk berkomunikasi."

    show arisa datar at center
    arisa "Jadi, kita bikin jadwal aja? Buat belajar bareng?"
    intro "Arisa memandang bahu Ilham yang seketika tegang mulai rileks setelah dia melontarkan pertanyaan tersebut."
    intro "Itu membuatnya merasa sedikit lebih lega."
    show ilham datar at center
    ilham "Aku bebas sih setiap hari."
    show arisa datar at center
    arisa "Oke, kalo gitu kita belajar disini aja sesudah kelas, gimana?"
    show ilham senang at center
    ilham "Iya, bisa-bisa."
    show arisa senang at center
    arisa "Ya udah, sepakat ya."
    show ilham senang at center
    ilham "Iya, sepakat."

    intro "Dengan canggung, Arisa menyodorkan buku cetak bahasa Indonesia ke arah Ilham."
    arisa "Dari tadi aku enggak selesai baca halaman ini."
    ilham "Mungkin lebih baik langsung ke soal-soalnya aja, lebih efektif."
    intro "Arisa mengangguk sebelum membuka daftar isi buku itu lagi."
    intro "Kali ini dia tau apa yang harus dia cari."
    intro "Mungkin situasi teman belajar ini tidak akan seburuk yang dia pikirkan."

    # Transisi ke adegan berikutnya
    scene black with fade

label scene_4:
    scene bg aula with fade
    play music "audio/competition_ambient.mp3" fadein 2.0

    intro "Arisa merapikan almamaternya sambil melihat sekelilingnya, matanya mengarah pada panggung besar di bagian belakang aula."
    intro "Tiga podium berdiri di tengah panggung, terlihat kaku dan agak menakutkan."
    intro "Dia memegang kalungnya dengan cemas."

    show ilham datar at left
    ilham "(Ekspresi datar) Nervous ya?"

    show arisa gugup at right
    arisa "(Ekspresi gugup) Ya iyalah aku nervous."
    arisa "Satu jam lagi aku bakal berdiri di atas sana, jawab soal-soal tentang mitokondria dan jamur-jamuran."

    show dosen senang at right
    dosen "(Ekspresi senang) Tenang, Nak, pasti tidak seburuk itu."

    arisa "(Ekspresi datar) Bu bilang gitu seolah-olah Ibu yang ngikut lomba."

    intro "Arisa mendengus masam, berusaha untuk menahan kecemasannya dengan mengeluarkan lembaran catatannya dan mulai membaca tentang kaidah kebahasaan."
    intro "Dia mengabaikan Ilham yang berdiri di sebelahnya dengan ekspresi panik, tangannya meraba-raba saku celananya."

    show ilham gugup at left
    ilham "(Ekspresi gugup) Eh, kamu liat handphone ku, enggak?"

    arisa "Ketinggalan di mobil kali."

    intro "Di sudut matanya, Arisa bisa melihat Dosen dengan sigap menyerahkan kunci mobilnya kepada Ilham."

    show dosen datar at right
    dosen "(Ekspresi datar) Ini, jangan lupa dikunci lagi ya."

    show ilham senang at left
    ilham "(Ekspresi senang) Siap, Bu."

    intro "Dengan begitu, Ilham pun menghilang dari persepsi Arisa yang masih sibuk membaca catatannya."
    intro "Sementara itu, Dosen berjalan mendekatinya, dengan senyum lembut di wajahnya."

    show dosen senang at right
    dosen "(Ekspresi senang) Ibu ke sana dulu ya, ada teman dari SMA."
    dosen "Kamu disini aja. Sekaligus jaga barang."

    arisa "Oke, Bu, sip."

    intro "Arisa mengangguk, akhirnya mengalihkan pandangannya dari catatan di tangannya dan matanya mengikuti Dosen yang berjalan menuju seorang dosen di seberang ruangan."
    intro "Dia memutuskan untuk mengambil tempat di kursi penonton untuk Ilham dan Dosen, memilih dua kursi yang tidak terisi dengan meletakkan tas mereka di atasnya."
    intro "Bosan, Arisa kemudian duduk di sebelah kiri dua kursi tersebut, tepat di samping seorang lelaki yang memiliki mata panda paling gelap yang pernah dia lihat."

    show cakra datar at left
    cakra "(Ekspresi datar) Kalungmu cantik."

    arisa "Oh, um…"

    menu:
        "Balas pujian":
            $ shield = 2
            $ renpy.notify("Hello!")
            arisa "(Terima kasih, antingmu keren.)"
            jump after_reply
        "Ucapkan terima kasih":
            $ shield = 1
            arisa "(Makasih.)"
            jump after_reply
        "Diam":
            $ shield = -1
            arisa "(...)"
            jump after_reply

    label after_reply:
        intro "Pop-up kecil tentang efek pilihan yang dipilih (+ 2 shield, + 1 shield, - 1 shield)"
    
    cakra "Pendant anemone itu melambangkan banyak hal, you know?"

    intro "Walaupun sebenarnya merasa canggung, kebosanan Arisa membuatnya ingin tetap mendengarkan apapun yang dikatakan oleh pemuda di sampingnya."

    cakra "Awal baru, antisipasi, perlindungan..."
    cakra "Seolah-olah itu bisa menjelaskan mengapa kamu di sini, ya kan?"

    arisa "(Ekspresi senang) Kamu serius?"
    arisa "(Ekspresi datar) Emang beneran bunga ini punya arti lain selain cantik?"

    cakra "Semua hal di dunia ini bisa melambangkan sesuatu."
    cakra "Tentu saja, mungkin aku terlalu bersemangat mencari makna lain dari hal yang sesimpel aksesoris."
    cakra "(Ekspresi senang) Tapi sejujurnya, aku lebih suka untuk berpikir terbuka."

    intro "Arisa terdiam sejenak mendengar kata-kata itu."
    intro "Ketika dia akhirnya bisa memikirkan sebuah respon, itu hanyalah pertanyaan yang sederhana."

    arisa "Kalau kamu? Ngapain kesini?"

    cakra "(Ekspresi datar) Untuk menang."

    intro "Mendengar itu, Arisa tertegun."
    intro "Sepertinya dia sudah bertemu dengan salah satu lawan lombanya."

    arisa "(Ekspresi senang) Kalau begitu aku tidak akan kalah."

    intro "Arisa berpaling untuk menatap pemuda itu."
    intro "Ada api yang berkobar di balik mata lelahnya kali ini."
    intro "Melihat itu membuat Arisa semakin penasaran."

    cakra "(Ekspresi senang) Baiklah, best of luck kalau begitu…?"
    arisa "Arisa."

    cakra "Okeh, Arisa, aku Cakra."
    cakra "Good luck."
    arisa "Kamu juga."

    intro "Bagi para peserta, dimohon untuk berkumpul di belakang panggung secepatnya, kompetisi akan segera dimulai."
    intro "Arisa segera beranjak dari tempat duduknya, mengalihkan fokusnya ke Ilham yang telah kembali setelah melihat pemuda yang tadi sedang berjalan ke arah panggung."

    arisa "(Ekspresi datar) Kenapa lama banget tadi?"
    
    ilham "(Ekspresi datar) Tadi handphone ku tersangut di sela-sela tempat minum dan kursi mobil."
    ilham "Dosen dimana?"
    
    arisa "Sibuk bicara sama temen SMA nya di sana."

    intro "Sambil menunjuk, Arisa menghela napas, gusar."

    arisa "(Ekspresi gugup) Aku ke belakang panggung dulu ya, udah dipanggil tadi."

    ilham "Ya udah, aku jagain tas."
    ilham "(Ekspresi senang) Semangat ya."

    arisa "(Ekspresi senang) Iya, thanks."

    intro "Arisa mengangguk sebelum berpaling dari Ilham."
    intro "Dengan jantung yang berdebar-debar, dia berjalan menuju panggung."
    intro "Sesuatu memberitahunya bahwa dia bisa melakukan ini."

    scene black with fade
    #panggil battle

    $ enemymaxhp = 200
    $ enemycurhp = 200
    $ enemyatk = 100
    $ enemydef = 10
    $ tbType = "Fire"
    call battle from _call_battel 

label scene_5:
    scene bg aula with fade
    play music "audio/competition_ambient.mp3" fadein 2.0

    intro "Arisa berpaling dan kembali menatap ke arah panggung sambil berjalan menuju Ilham yang sedang duduk di kursi yang dia pilih tadi."
    intro "Jantungnya masih berdebar-debar, dan tangannya malah semakin basah karena keringat yang dia seka dari dahinya."
    intro "Tapi ada juga sesuatu yang baru yang mengendap di hatinya."

    show arisa senang at right
    arisa "(Ekspresi senang) Eh, beneran?"

    show arisa gugup at right
    arisa "(Ekspresi gugup) Padahal aku gemetaran hebat loh, ini aja masih dikit."

    intro "Arisa menoleh ke Ilham dan memperlihatkan kedua tangannya yang bergetar tidak karuan."

    show ilham senang at left
    ilham "(Ekspresi senang) Kamu tadi keren banget!"

    show arisa datar at right
    arisa "(Ekspresi datar) Sepertinya aku harus terbiasa dengan ini kalau aku mau menang."

    show ilham datar at left
    ilham "(Ekspresi datar) That’s the spirit!"
    ilham "(Ekspresi datar) Ngomong-ngomong, bagaimana tadi rasanya? Seru, enggak?"

    show arisa senang at right
    arisa "(Ekspresi senang) Lebih banyak takut salahnya sih, dan sebagiannya juga gugup setengah mati."
    arisa "(Ekspresi senang) Tapi yah, lumayan seru juga sih."
    arisa "(Ekspresi datar) Walaupun aku di sini gara-gara dipaksa sama Bu Ratna."
    arisa "Oh, iya, Bu Ratna ke mana?"

    show ilham datar at left
    ilham "(Ekspresi datar) Di luar tadi, lagi nelpon sama anaknya."

    intro "Arisa merespon dengan anggukan singkat, mengingat foto berbingkai yang dia lihat di ruangan Bu Ratna tempo hari."

    show arisa datar at right
    arisa "(Ekspresi datar) Denger-denger, anaknya lagi di luar kota, ya?"

    show ilham datar at left
    ilham "(Ekspresi datar) Iya, lagi S2 seingatku."

    show arisa senang at right
    arisa "(Ekspresi senang) Pinter pasti."

    show ilham senang at left
    ilham "(Ekspresi senang) Ya, kita belum tentu tau."

    show arisa datar at right
    arisa "(Ekspresi datar) Jadi ini kamu bilang dia enggak pintar, gitu?"

    show ilham datar at left
    ilham "(Ekspresi datar) Itu kamu yang bilang."

    intro "Mendengar nada datar yang tidak pernah dia dengar keluar dari mulut Ilham, Arisa tidak bisa menahan tawa kecilnya."
    intro "Sebetulnya, dia terkejut karena dia lumayan menikmati kehadiran Ilham di sebelahnya selama beberapa minggu terakhir."
    intro "Mungkin itulah yang terjadi ketika seseorang memiliki orang lain yang bersedia mendukung dan bersabar dengan tingkah lakunya."

    show arisa senang at right
    arisa "(Ekspresi senang) Eh, kamu mau ikut lomba juga, enggak?"
    arisa "(Ekspresi datar) Mungkin bukan yang kayak gini."

    show ilham datar at left
    ilham "(Ekspresi datar) Aku kan udah bilang enggak mau ikut lomba."
    ilham "(Ekspresi datar) Too much pressure."

    show arisa datar at right
    arisa "(Ekspresi datar) Ya, gimana kalo lomba tim gitu? Supaya kamu gak takut sendiri?"

    show ilham datar at left
    ilham "(Ekspresi datar) Kayaknya kamu deh yang mau aku ikut lomba biar kamu gak takut sendiri."

    show arisa senang at right
    arisa "(Ekspresi senang) Iya sih, tapi seru loh."
    arisa "(Ekspresi datar) Babak selanjutnya kapan ya?"

    show brian datar at center
    brian "(Ekspresi datar) Dua puluh menit lagi."

    intro "Arisa berbalik ke belakang, menghadapi seorang lelaki dengan rambut keriting yang menjawab pertanyaannya."
    intro "Brian mengulurkan tangan untuk berjabat tangan."

    show arisa senang at right
    arisa "Oh, aku Arisa, dan ini Ilham, salam kenal juga."

    intro "Sambil menunjuk Ilham dengan jempolnya, Arisa melihat pemuda itu melambaikan tangannya kepada Brian secara singkat sebelum menatap ponselnya, tampak tidak fokus."
    intro "Pada pandangan pertama, beberapa orang mungkin melihatnya sebagai orang yang pendiam saja."
    intro "Tapi setelah mengenalnya dan mengawasi body language yang dia tampilkan, Arisa tahu apa arti diamnya."

    show arisa senang at right
    arisa "Anyway, kamu ikut lomba?"

    show brian senang at center
    brian "(Ekspresi senang) Iya, sebenarnya cuma coba-coba sih."
    brian "(Ekspresi senang) Tapi kalo menang lumayan sih, kapan lagi menang lomba dapat beasiswa?"

    show arisa marah at right
    arisa "(Ekspresi marah) Hah, beasiswa? Kok aku gak tau sih?"

    show brian datar at center
    brian "(Ekspresi datar) Ya, kan aku bohong."

    show arisa marah at right
    arisa "(Ekspresi marah) Lah."

    show brian datar at center
    brian "(Ekspresi datar) Kalo menang, palingan kita dapat piala sama uang."
    brian "(Ekspresi datar) Lumayan sih, bisa beli makanan kucing."

    show arisa datar at right
    arisa "(Ekspresi datar) Apaan sih."

    intro "Merasa bingung dengan arah percakapan ini, Arisa melirik Ilham yang hanya memberinya jari jempol."
    intro "Sebuah tanda dukungan, sepertinya."
    intro "Dia memutuskan untuk mengalihkan topik ke hal lain."
    intro "Rasa keingintahuannya ingin melihat apa yang akan dia hadapi di babak berikutnya."

    show arisa datar at right
    arisa "(Ekspresi datar) Kira-kira nanti soalnya seperti apa ya?"

    show brian datar at center
    brian "(Ekspresi datar) Mungkin sesuatu yang mudah seperti 'apa itu hak asasi manusia?'"

    show arisa senang at right
    arisa "(Ekspresi senang) Itu kayaknya kelebihan mudah deh."

    show brian senang at center
    brian "(Ekspresi senang) Oh, ngomong-ngomong, kamu mau tahu fakta menarik?"

    menu:
        "Menerima":
            $ shield = 2
            arisa "(Iya, mau.)"
            jump after_fakta
        "Menolak":
            $ shield = -1
            arisa "(Enggak, sih.)"
            jump after_fakta
        "Diam":
            $ shield = 1
            arisa "(...)"
            jump after_fakta

    label after_fakta:
        intro "Pop-up kecil tentang efek pilihan yang dipilih (+ 2 shield, + 1 shield, - 1 shield)"
        brian "Kamu tau, enggak, kalo sistem sosial, misalnya norma-norma, itu sering beroperasi di bawah permukaan dan tidak disadari oleh orang-orang?"
        brian "Seolah-olah kita itu ngikut aturan tak tertulis tentang kesopanan tanpa memikirkannya secara aktif, seperti kebiasaan mengantri."
    
        show arisa senang at right
        arisa "(Ekspresi senang) Menarik."

        show brian senang at center
        brian "(Ekspresi senang) Ya kan?"

        intro "Bagi para peserta, dimohon untuk berkumpul di belakang panggung secepatnya, kompetisi akan segera dimulai."
        intro "Mendengar pengumuman itu, Arisa merasa lebih semangat dari sebelumnya."
        intro "Dia menatap Brian dengan tekad mendalam di matanya."

        show arisa senang at right
        arisa "(Ekspresi senang) Semoga yang terbaik menang, ya?"

        show brian datar at center
        brian "(Ekspresi datar) Ya, semoga yang terbaik menang."

        intro "Dengan itu, Arisa berpaling kembali ke Ilham yang masih terdiam di kursinya, mendengar langkah kaki Brian yang beranjak pergi."

        show ilham senang at left
        ilham "(Ekspresi senang) Semangat ya?"

        show arisa senang at right
        arisa "Mhm, thanks! I’ll be right back."

        intro "Bersemangat, Arisa mengangguk sebelum berpaling dan berjalan cepat ke panggung yang memanggil namanya."
        intro "Sekarang dia sudah tahu bahwa dia bisa melakukan ini."
    
    scene black with fade
    #panggil battle

label scene_6:
    scene bg aula with fade
    play music "audio/competition_ambient.mp3" fadein 2.0

    intro "Dengan bahu yang lebih ringan, Arisa berjalan mendekati dosen yang sedang duduk di samping barang-barang mereka."
    intro "Dia baru saja menyadari bahwa Ilham tidak ada di mana-mana saat mengambil buku catatannya yang berada di atas tasnya dan duduk di sebelah dosen."

    show arisa datar at right
    arisa "(Ekspresi datar) Bu, Ilham ke mana ya?"

    show dosen datar at left
    dosen "(Ekspresi datar) Dia pergi beli gado-gado tadi, sekalian beliin kamu ketoprak juga, kamu suka katanya."

    show arisa senang at right
    arisa "(Ekspresi senang) Oh, gitu ya…"

    intro "Merasa cukup senang mendengar itu, Arisa duduk di samping dosen, masih memegang bukunya yang penuh dengan soal dan catatan."

    show dosen senang at left
    dosen "Jadi, kamu gimana sekarang? Suka lombanya? Seru?"

    show arisa senang at right
    arisa "(Ekspresi senang) Seru sih, Bu."
    arisa "(Ekspresi gugup) Tapi bikin deg-degan juga."

    show dosen senang at left
    dosen "Itulah yang dimaksud dengan seru, kan? Bikin deg-degan?"

    show arisa senang at right
    arisa "(Ekspresi senang) Benar juga sih, Bu."

    intro "Pandangan Arisa kemudian beralih ke ponsel di tangan dosen, mengingat tentang percakapannya dengan Ilham puluhan menit yang lalu."
    intro "Dia tahu hal itu adalah sesuatu yang personal, bahkan terlalu personal."
    intro "Tetapi Arisa selalu kalah saat melawan keingintahuannya."

    show arisa datar at right
    arisa "(Ekspresi datar) Anak Ibu lagi S2 ya?"

    show dosen datar at left
    dosen "(Ekspresi datar) Iya, dia lagi S2 di luar kota."
    dosen "(Ekspresi senang) Kenapa? Kamu rencananya mau S2 juga?"

    show arisa datar at right
    arisa "Enggak, Bu. Aku cuma penasaran aja."

    intro "Arisa sebenarnya ingin mengakhiri pembicaraan itu di sana."
    intro "Meskipun begitu, dosen tetap berbicara, mengejutkan Arisa."

    show dosen datar at left
    dosen "(Ekspresi datar) Kamu itu sebenarnya mirip sama anak saya dulu."

    show arisa senang at right
    arisa "(Ekspresi senang) Beneran, Bu? Mirip gimana?"

    show dosen senang at left
    dosen "(Ekspresi senang) Blak-blakan dan susah buat dimotivasi."

    show arisa datar at right
    arisa "(Ekspresi datar) Yah, kirain sama-sama pinter gitu, Bu. Atau cerdas."

    show dosen datar at left
    dosen "Iya deh, sama-sama pintar juga. Tapi dia waktu itu lebih parah tentang tidak bermotivasi."
    dosen "Sampai bangun aja susah."

    intro "Arisa hanya bisa bergeming, tidak tahu harus melakukan apa tentang aura dingin yang menyelimuti konversasi ini."

    show dosen sedih at left
    dosen "Untungnya dia punya teman yang selalu mengunjungi rumah."
    dosen "Butuh waktu berminggu-minggu baginya untuk bangkit kembali."
    dosen "(Ekspresi sedih) Saat itu, saya merasa sedih mengetahui bahwa saya tidak bisa banyak membantu dia."
    dosen "Tapi sekarang saya bersyukur dia bisa memiliki seseorang yang mendukungnya di saat-saat terburuk dalam hidupnya."
    dosen "Dan walaupun itu bukan saya, ibunya, sepertinya saya bisa mengerti kenapa begitu."

    intro "Rasanya aneh mendengarkan orang dewasa berbicara tentang masalah mereka sebagai orang yang lebih muda."
    intro "Tapi itu membuka matanya sedikit lebih lebar."
    intro "Dan Arisa bisa menghargainya."

    show arisa sedih at right
    arisa "(Ekspresi sedih) Bu?"

    show dosen datar at left
    dosen "Ibu ke toilet dulu ya?"

    intro "Arisa bahkan tidak sempat memberikan reaksi, cuma bisa menatap dosen berdiri dan pergi."
    intro "Sebagian dari dirinya merasa bersalah, ingin mengikuti dan menghibur dosen."
    intro "Tetapi bagian dirinya yang lebih logis mengingatkannya bahwa dosen adalah orang dewasa dan bisa mengatasi emosinya sendiri."
    intro "Jadi Arisa tetap di sana, berusaha untuk fokus pada catatannya."

    show arisa marah at right
    arisa "(Ekspresi marah) Aduh, fisika… ini apaan lagi…"

    show aziza datar at left
    azizah "Um, permisi…"

    intro "Teralihkan oleh suara lembut, Arisa menengadah dan menatap seorang gadis dengan rambut keriting yang cantik."

    menu:
        "Bertanya ada apa":
            $ shield = 2
            arisa "(Ekspresi datar) Em, ada apa ya, Kak?"
        "Menyapa":
            $ shield = 1
            arisa "(Ekspresi datar) Halo?"
        "Diam":
            $ shield = -1
            arisa "(Ekspresi datar) ..."

    intro "Pop-up kecil tentang efek pilihan yang dipilih (+ 2 shield, + 1 shield, - 1 shield)"

    show azizah senang at left
    azizah "Eyeliner kamu rapi banget."
    azizah "(Ekspresi senang) Aku boleh tau enggak, gimana caranya supaya bisa buat yang serapi kayak kamu?"

    show arisa senang at right
    arisa "(Ekspresi senang) Oh. Aku cuma kira-kirain sih kalo panjangnya."
    arisa "Tapi aku juga suka ngerapiin pakai concealer atau micellar water di ujung cotton bud gitu."

    intro "Merasa canggung tapi tersanjung pada saat yang sama, Arisa mencoba memberinya beberapa tips berguna."
    intro "Walaupun kenyataannya dia tidak tahu apa yang benar tentang penerapan eyeliner-nya."

    show aziza datar at left
    azizah "(Ekspresi datar) Hm, gitu ya. Okeh, makasih sarannya, nanti bakal kucoba."

    show arisa senang at right
    arisa "Sama-sama. Dan aku suka rambutmu, cantik sekali."

    show aziza senang at left
    azizah "(Ekspresi senang) Terima kasih. Aku sebenarnya kesulitan menatanya pagi ini."

    intro "Entah bagaimana, komentar kecil itu berkesan bagi Arisa."
    intro "Dia tidak yakin harus berbuat apa selain mengulurkan tangannya."

    show arisa senang at right
    arisa "Aku Arisa, by the way."

    show aziza datar at left
    azizah "(Ekspresi datar) Salam kenal kalo begitu, namaku Aziza."

    intro "Arisa bersalaman singkat dengan Aziza, sedikit kaku."
    intro "Ketika akhirnya melepaskan tangannya, Arisa memandang Aziza yang tampaknya mengingat sesuatu."

    show aziza datar at left
    azizah "Oh, iya, kamu tau enggak toiletnya di mana?"

    show arisa datar at right
    arisa "(Ekspresi datar) Kayaknya di koridor sana deh."

    intro "Arisa menunjuk ke arah dosen tadi pergi, merenungkan tentang apakah dia baik-baik saja di dalam sana."

    show aziza senang at left
    azizah "Okeh, makasih ya, sekali lagi."

    show arisa datar at right
    arisa "Iya, sama-sama."

    intro "Sejenak setelah mengamati Aziza pergi, suara familier mulai mengisi seluruh aula sekali lagi."
    intro "“Bagi para peserta, dimohon untuk berkumpul di belakang panggung secepatnya, kompetisi akan segera dimulai.”"
    intro "Arisa pun berdiri, meletakkan buku catatannya kembali di atas tas ranselnya, berpaling ke belakang saat mendengar langkah kaki mendekatinya."

    show ilham gugup at left
    ilham "(Ekspresi gugup) Maaf kelamaan, tadi antriannya panjang banget."

    show arisa datar at right
    arisa "Gapapa, aku makan nanti aja sesudah round terakhir."

    show ilham senang at left
    ilham "(Ekspresi senang) Ya udah, aku tungguin. Semangat!"

    show arisa senang at right
    arisa "(Ekspresi senang) Iya, iya, semangat."

    intro "Sambil tertawa kecil, Arisa beroleh ke panggung besar yang sudah terasa familier."
    intro "Dia tidak sabar untuk menyelesaikan kompetisi ini."

    scene black with fade
    #panggil battle

label bad_ending:
    scene bg perpustakaan with fade
    play music "audio/sad_piano.mp3" fadein 2.0

    intro "Arisa duduk di depan laptopnya yang terbuka, kerutan di dahinya dalam, dan matanya terlihat lelah."
    intro "Perlahan, dia membuka situs universitas, jantungnya berdebar kencang di dadanya."
    intro "Dia mengetikkan nama email serta password-nya sebelum menekan tombol 'Enter'."
    intro "Jauh di dalam hatinya, dia tahu apa yang akan dia temukan di bagian nilai mata kuliahnya."
    intro "Deretan B minus."

    intro "Meskipun begitu, dia tetap tegang, mempersiapkan diri untuk melihat nilai mata kuliah terakhir di semester itu."

    show anggreani sedih at center
    arisa "(Ekspresi sedih) ..."

    intro "Anggreani menatap huruf C yang ada di layarnya."
    intro "Eksistensinya seolah-olah sedang mengejeknya."
    intro "Begitu pula ponselnya yang terdiam di atas meja."

    intro "Entah bagaimana, rasa sakit dari nilai jeleknya kurang penting dibandingkan dengan perasaan hampa di dadanya."

    intro "BAD ENDING"
    return

label good_ending:
    scene bg office with fade
    play music "audio/calm_background.mp3" fadein 2.0

    intro "Arisa dengan lembut menurunkan dirinya di kursi yang dia duduki sebulan yang lalu."
    intro "Rasanya masih sama."
    intro "Tapi ada kenyamanan tertentu kali ini."

    show dosen datar at left
    dosen "(Ekspresi datar) Arisa?"

    intro "Matanya bertemu dengan orang yang duduk di seberang meja."

    show arisa datar at right
    arisa "(Ekspresi datar) Ya, Bu?"

    show dosen datar at left
    dosen "Kamu kenapa?"

    show dosen senang at left
    dosen "(Ekspresi senang) Tidak setiap hari saya lihat seseorang semurung kamu walaupun sudah dapat nilai B."

    intro "Arisa menghela napas."
    intro "Perkataan itu membuatnya tampak tidak bersyukur."

    show arisa datar at right
    arisa "Bukan tentang nilai B-nya, Bu."
    
    show arisa gugup at right
    arisa "(Ekspresi gugup) Gimana ngejelasinnya ya?"

    intro "Perlahan, tangannya meraih kalungnya sambil melirik berbagai jenis barang-barang yang ada di meja."
    intro "Seketika berhenti ketika dia menatap bingkai foto kecil di sebelah tumpukan kertas dan buku."

    show arisa sedih at right
    arisa "(Ekspresi sedih) Rasanya seperti aku tidak berusaha sekeras mungkin."

    show dosen datar at left
    dosen "(Ekspresi datar) Kenapa? Karena kamu tidak dapat juara satu?"

    intro "Arisa diam, memikirkan jawaban apa yang bisa dia katakan."

    show dosen senang at left
    dosen "Kamu itu…"
    dosen "Kemajuan membutuhkan proses dan proses juga membutuhkan waktu."
    dosen "Sebulan itu waktu yang singkat, dan kamu masih bisa menang."
    dosen "Bayangin kalo kamu dapat waktu yang lebih panjang."
    dosen "Dua bulan, empat bulan, setengah tahun."
    dosen "Kamu mungkin bisa melakukan apapun."

    intro "Ada senyuman kecil di wajah Arisa saat dia melihat Dosen mengangkat bahunya."

    dosen "Jadi saran saya itu ambil kemenanganmu yang sekarang."
    dosen "Lalu move on dari itu supaya kamu bisa memenangkan pertempuran yang lebih baik."

    intro "Arisa mengangguk, merasa termotivasi oleh kata-kata yang dosennya baru saja katakan."

    show arisa senang at right
    arisa "(Ekspresi senang) Kalo begitu saya pamit dulu ya, Bu. Permisi."

    intro "Merasa jauh lebih baik, Arisa berdiri dari kursinya sebelum menyalimi tangan Dosen."
    intro "Saat dia menghampiri pintu ruangan, ponselnya berdering halus."
    intro "Arisa tahu persis siapa yang baru saja menelponnya."
    intro "Dan dia tidak bisa menahan senyumnya memikirkan untuk bertemu kembali dengan teman belajarnya."

    return


