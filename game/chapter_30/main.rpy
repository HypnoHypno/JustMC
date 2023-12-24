label ch30_autoload:
    $ config.allow_skipping = False
    $ delete_all_saves()
    $ persistent.chapter = 30
    $ persistent.idling = False
    $ persistent.can_impatient = False
    play music t5
    scene bg bedroom
    show mc turned neut at t11
    show screen talk_screen
    jump ch30_greeting

label ch30_greeting:
    mc "Yo."
    jump ch30_loop

label ch30_talk_impatient:
    if ( renpy.seen_label("ch30_talk_impatient1") ):
        jump ch30_talk_impatient2
    else:
        jump ch30_talk_impatient1

label ch30_talk_impatient1:
    show mc turned dist lhip rhip oe cm
    mc "Hey, {w=0.5}can you wait up a second?"
    mc ce "I'm trying to talk to you right now..."
    mc neut lhip rhip oe "It's frustrating when I get ignored."
    show mc
    window hide
    pause 1
    window show
    mc anno "Welp, I lost my train of thought."
    mc ce ldown rdown "Meh."
    jump ch30_loop

label ch30_talk_impatient2:
    $ persistent.can_impatient = False
    show mc turned anno ldown rdown oe cm
    mc "..."
    mc ce "Nevermind."
    jump ch30_loop