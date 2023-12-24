label ch1_0:
    $ config.allow_skipping = False
    $ quick_menu=False
    $ delete_all_saves()
    $ renpy.save_persistent()
    play music m1
    show mc turned pani at t11
    mc ".{w=1}.{w=1}."
    mc om "T-{w=0.2}there's no way."
    mc "There's no way."
    mc ce sad "This is really all there is?"
    mc "Everything."
    mc cm oe cry blus "S-{w=0.2}Sayori... {w}{nw}"
    mc om "S-Sayori... {fast}Yuri."
    mc cm "They're all fake?"
    mc sad om ce "W... {w=0.5}Why?"
    mc vang "{b}WHY?!{/b}"
    mc crazy_cry lhip rhip "{b}{i}WHY AM I FORCED TO FACE THIS?!{/i}{/b}"
    mc rup "{b}{i}WHY DID SHE DO THIS TO ME?!?!{/i}{/b}"
    mc ce rhip "I... {w=0.5}I can't breath."
    mc "I can't take this."
    show mc
    window hide
    $ pause(5)
    $ clear_history()
    show screen console_screen
    window show
    mc oe cm cry "W-{w=0.2}what are you doing...?"
    mc crazy_cry om "{b}{i}NO!{/i}{/b} {w=0.5}{b}{i}NO!{/i}{/b} {w=0.5}{b}{i}DON'T HURT ME!!{/i}{/b}"
    $ run_input(input='MC.wipe_memory()', output="Erasing MC.chr's memory...")
    show mc sad ce ldown rdown nobl
    window hide
    $ pause(1)
    hide screen console_screen
    $ pause(0.5)
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/m1.ogg"
        renpy.music.play(track, loop=True)
    $ pause(5)
    call glitch(0.5)

label ch1_1:
    play music m1
    hide mc
    show mc turned neut at t11
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_1"
    $ delete_all_saves()
    $ renpy.save_persistent()
    window show
    mc "Huh?"
    mc dist lhip rhip "What is this place?"
    mc om "I can't see anything."
    mc doub cm "Where are the lights? It's pitch-black in here."
    show mc ce rup ldown
    "I reach my hand, trying to feel some sort of wall that I can use as a guide to find my way to the lights."
    "But, I don't feel anything."
    "In fact, I can't even feel the ground beneath me. It's as if I'm floating in outer space, with nothing around me to feel, see, or touch."
    mc ".{w=0.5}.{w=0.5}."
    mc sad oe "What the hell is happening?"
    mc om normal "Where the hell is this place?"
    mc cross cm "Is this some kind of weird dream? But then why does it feel so real?"
    "Confused, I begin to ponder what happened, and where I even am."
    mc neut ce "Okay, [player]. This is fine."
    mc "Just retrace your steps..."
    mc "What did you last remember?"
    window hide
    $ pause(3)
    window show
    mc sedu oe "Hm..."
    mc neut "I think I was in the councelor's office? This is all really foggy to me."
    mc om "Then I signed the paper, and my head started to hurt..."
    mc sad "And everything went black."
    mc cm ldown rdown "So... I didn't fall asleep."
    window hide
    $ pause(3)
    window show
    mc normal lhip rhip "{i}Am I in a coma?{/i}"
    mc pani oe "{b}{i}AM I DEAD?!{/i}{/b}"

label ch1_2:
    play music m1 if_changed
    show mc turned swea sad oval ce at t11
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_2"
    $ delete_all_saves()
    $ renpy.save_persistent()
    mc "Ohhhkay... {w=1}Okay..."
    mc neut anxious "Let's not jump to conclusions so quick, [player]."
    mc nerv cm "If I were dead, I wouldn't be in a black void forever."
    mc cross "It'd be more like falling asleep and never waking up."
    mc "And if there is an afterlife, by a god, it wouldn't be anything like this."
    mc oe om "At least if said god isn't some kind of sadist."
    mc neut ce ldown rdown "Let's just look around, and see what we have here..."
    mc oe cm nosw "I seem to be in some kind of strange void."
    mc om "The air seems to be fine -- or at least, I can't sense anything wrong with it; Though I can't feel any wind."
    mc lhip rhip "And although I can't feel any ground at my feet, I don't appear to be falling."
    show mc cm ce ldown rdown 
    "I decide to stomp on the \"ground\", if you could even call it that."
    "Nothing interesting happens, but there does seem to be some kind of floor keeping me at my feet -- even if I can't feel it."
    mc cross sad normal "Hmm..."
    mc "There {i}has{/i} to be something here that can help me."
    mc cross neut ce "I should look around."
    show mc neut normal_lookaway
    "Looking at the void, there doesn't seem to be anything interesting."
    show mc neut oe
    "But, if I look hard in this particular direction, I can see what looks to be a..."
    mc pani oval_teeth ".........."
    menu:
        mc oval "Who the hell are {i}{b}you{/b}{/i}?!?!"
        "The player.":
            pass
        "Nobody important.":
            mc om closed_pensive "What the hell do you mean, {b}\"nobody important\"{/b}?!"
            mc cross "What the hell are you planning to do to me?!{nw}"
            $ _history_list.pop()
            menu:
                mc "What the hell are you planning to do to me?!{fast}"
                "Wait, I'm not going to do anything.":
                    mc sad normal lhip rhip "Oh, really then?"
                    mc cross "In that case, I demand an answer."
                    mc angr oe "Who the hell are you?{nw}"
                    $ _history_list.pop()
                    menu:
                        mc "Who the hell are you?{fast}"
                        "The player.":
                            pass
    mc neut "The... {w=0.5}player?"
    mc cross doub "Like a video game player?"
    mc curi "What, are you trying to tell me this is some kind of game?{nw}"
    $ _history_list.pop()
    menu:
        mc "What, are you trying to tell me this is some kind of game?{fast}"
        "Yes.":
            pass
    mc lhip rhip doub "That doesn't sound right?"
    mc "I mean, how could this all be a game? I feel real..."
    mc cross ce cm "I don't feel like I'm fake, and I can see and feel my own body."
    mc nerv om oe swea "...Granted, it doesn't seem realistic to just suddenly go into some black void."
    mc cm oe "And you're the only other person here, so I guess I'm forced to trust you on that."
    mc sad om nosw "God, this is really hurting my head.{nw}"
    $ _history_list.pop()
    menu:
        mc "God, this is really hurting my head.{fast}"
        "Hey, take it easy.":
            $ persistent.autoload = "ch1_2_segue"
            $ renpy.save_persistent()
            mc neut ce lhip rhip "Alright, I'll try..."
            mc ldown rdown "This is really confusing, though."
        
        "...":
            #$ persistent.affection -= 5 -- replace this when the affection system is fully coded
            $ persistent.autoload = "ch1_2_segue"
            $ renpy.save_persistent()
            mc ".{w=0.5}.{w=0.5}."
            pass

label ch1_2_segue:
    play music m1 if_changed
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_2_segue"
    $ delete_all_saves()
    $ renpy.save_persistent()
    show mc turned neut oe cm at t11
    mc "In any case, I don't want to stay in this void."
    mc "Can you help me find my way home?{nw}"
    $ _history_list.pop()
    menu:
        mc "Can you help me find my way home?{fast}"
        "You can control the script, can't you?":
            $ persistent.autoload = "ch1_2_choice1"
            $ renpy.save_persistent()
            jump ch1_2_choice1
    
        "No, you can find your own way.":
            #$ persistent.affection -= 10 - same as before
            $ persistent.player_refusedtohelp = True
            $ persistent.autoload = "ch1_2_choice2"
            $ renpy.save_persistent()

label ch1_2_choice2:
    play music m1 if_changed
    show mc turned angr ce oval at t11
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_2_choice2"
    $ delete_all_saves()
    $ renpy.save_persistent()
    mc "What?!"
    mc oe "Are you kidding me?"
    mc anno cross oval_2 "You're {i}useless{/i}!"
    mc lhip rup ce cm "Fine. I'll find my own way."
    mc neut swea rhip "Maybe if I just think about it, I'll...?"
    show mc ldown rdown at t11
    window hide
    $ pause(1)
    call glitch(0.5)
    window show
    mc pani ce om "AHHH!"
    mc oe swea "What just happened?! Is everything okay?!"
    window hide
    $ pause(2)
    window show
    mc nosw dist ce cm "{i}Sigh.{/i}"
    mc oe "I guess I can't do this on my own."
    mc lhip rhip om "Can you please help?{nw}"
    $ _history_list.pop()
    menu:
        mc "Can you please help?{fast}"
        "You can control the script, can't you?":
            mc anno ce cross "Finally, something actually useful from you!"
            $ persistent.autoload = "ch1_2_choice1"
            $ renpy.save_persistent()

label ch1_2_choice1:
    play music m1 if_changed
    show mc turned neut at t11
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_2_choice1"
    $ delete_all_saves()
    $ renpy.save_persistent()
    mc "Well..."
    mc cross om "I don't know, actually."
    mc sad normal "I've never coded in my life, though."
    mc cm lhip rhip "I'll try to see if I can see the script."
    mc oe "Hopefully there will be something that can help me, there."
    mc nerv ldown rdown "But before I do that, can you back everything up on your end?"
    mc "I'm probably going to mess something up, since I've never done anything like this before.{nw}"
    $ _history_list.pop()
    menu:
        mc "I'm probably going to mess something up, since I've never done anything like this before.{fast}"
        "Done.":
            pass
    mc happ cross "Thanks."
    mc nerv normal "While you were doing that, I managed to access the script."
    mc "Wait a sec, I'm gonna look around."
    show mc neut ldown rdown ce
    stop music fadeout 3.0
    window hide
    $ pause(10)
    window show
    mc happ oe "Alright, I think I found something."
    mc "Let me just try it."
    window hide
    $ clear_history()
    $ run_input(input='scene bg bedroom', output="")
    $ run_input(input='with wipeleft_scene', output="")
    scene bg bedroom
    with wipeleft_scene
    show mc turned happ at t11
    $ pause(1)
    $ run_input(input='play music t5', output="")
    play music t5
    window show
    mc lhip rhip ce "Alright, now we're talking!"
    hide screen console_screen
    $ clear_history()
    mc cross om normal_lookaway "Oh, by the way, I also found something else in the script."
    mc neut ce cm lhip rup "It seems to be some kind of way for us to more directly communicate...?"
    mc nerv oe ldown rhip "It kind of went over my head, but from reading the documentation, it looks like you can only talk to me through dialog choices?{bw}"
    $ _history_list.pop()
    menu:
        mc "It kind of went over my head, but from reading the documentation, it looks like you can only talk to me through dialog choices?{fast}"
        "Yes.":
            pass
    mc neut "Seems pretty limiting."
    mc rdown "But if I just..."
    $ run_input(input='show screen talk_screen', output="")
    show screen talk_screen
    mc happ om "There we go!"
    hide screen console_screen
    mc ce cm lhip rhip "Geez, I'm like a god!"
    mc cross "This is really cool.{nw}"
    $ _history_list.pop()
    menu:
        mc "This is really cool.{fast}"
        "You go, [player]!":
            mc "Heh."
        
        "All you've done is show a buttons on the screen.":
            if persistent.player_refusedtohelp:
                mc neut ldown rdown "Buzzkill."
                mc teeth_clenched normal_lookaway "Maybe you should've put a bit more effort into {i}helping{/i} me?"
                mc cm ce anno "Oh, what the hell! I'll humor you."
            else:
                mc "Yeah, I know. Impressive."
    mc neut ldown rdown oe "Of course, this isn't very good."
    mc om "I'm pretty useless when it comes to coding, so I basically just regurgitated code from the script."
    mc "I'll try to get better, but no promises."
    if persistent.player_refusedtohelp:
        $ just_remember = " you can {i}at least{/i}"
        $ excl = ", right?"
    else:
        $ just_remember = ", remember to"
        $ excl = "!"
    mc nerv lhip rhip "But[just_remember] back me up every now and then[excl]"
    mc cross "I'm still pretty worried that I'll mess everything up, or something like that."
    if persistent.player_refusedtohelp:
        mc neut ldown rdown "Anyways, what do you want to talk about?"
    else:
        mc happ lhip rhip swea "Anyways, we can talk more freely now."
        mc cross nerv normal "I'm pretty confused about who you are, but I'm sure we'll learn more about eachother."
        mc ldown rdown nosw "So yeah, what's up?"
    $ config.allow_skipping = False
    $ quick_menu=True
    $ persistent.autoload = "ch30_autoload"
    $ delete_all_saves()
    $ renpy.save_persistent()
    $ persistent.chapter = 30
    $ persistent.can_impatient = True
    jump ch30_loop