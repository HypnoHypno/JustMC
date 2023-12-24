init 1 python:
    jm_add_new_topic("mc_komi")

label mc_komi: # MC talks about Komi Can't Communicate; Topic by Yogapants_73
    show mc turned cross
    mc "Do you know about the Anime {i}Komi Can't Communicate{/i}?{nw}"
    menu:
        mc "Do you know about the Anime {i}Komi Can't Communicate{/i}?{fast}"
        "Yes, I've heard of it":
            $ mc_komianswer = 1
            mc nerv om "Heh, stupid question, it's pretty popular."
            $ well = "Well, "
        
        "Yes, I've watched it":
            $ mc_komianswer = 2
            mc happ closed_pensive om "My condolences to you."
        
        "No":
            $ mc_komianswer = 3
            mc "Ah, I see."
            $ well = ""
    if ( mc_komianswer != 2 ):
        mc neut lhip rup om "[well]I seriously can't reccomend it to you."
    hide window
    menu:
        "Huh, why?":
            pass
    #FALLTHROUGH

label mc_komi2:
    mc neut om ldown rdown "It's a {i}really{/i} bad Anime."
    mc nerv cm swea "Yamai Ren is... {w=0.5}something else."
    show mc nosw
    if ( mc_komianswer != 2 ):
        mc neut om "You fine with spoilers?"
        menu:
            "Yes":
                jump mc_komi3
            
            "No":
                pass
        mc cm "Well, all I'll say is that you'll probably hate pretty much everyone when you watch episode 4."
        mc curi smile "Also known as \"It's just a physical.\"."
        mc happ om "...And if you {i}do{/i} decide to watch it..."
        mc lhip rhip ce "Don't say I didn't warn you!"