label ch1_0:
    $ config.allow_skipping = False
    $ quick_menu=False
    $ delete_all_saves()
    $ renpy.save_persistent()
    play music m1
    show mc turned pani at t11
    mc ".{w=1}.{w=1}."
    mc om "T-{w=0.2}there's no way..."
    mc "There's no way."
    mc ce sad "This is really all there is...?"
    mc "Everything."
    mc cm oe cry blus "S-{w=0.2}Sayori... {w}{nw}"
    mc om "S-Sayori... {fast}Yuri."
    mc cm "They're all fake?"
    mc sad om ce "W... {w=0.5}Why?"
    mc vang "{b}WHY?!{/b}"
    mc crazy_cry lhip rhip "{b}{i}WHY AM I FORCED TO FACE THIS?!{/i}{/b}"
    mc rup "{b}{i}WHY DID SHE DO THIS TO ME?!?!{/i}{/b}"
    mc ce rhip "I... {w=0.5}I can't breath."
    mc "I can't take this..."
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
    mc "Huh...?"
    mc dist lhip rhip "Uh... What is this place?"
    mc om "I can't see anything..."
    mc doub cm "Ugh, where are the lights? It's pitch-black in here."
    show mc ce rup ldown
    "I reach my hand, trying to feel some sort of wall that I can use as a guide to find my way to the lights."
    "But, I don't feel anything."
    "In fact, I can't even feel the ground beneath me. It's as if I'm floating in outer space, with nothing around me to feel, see, or touch."
    mc ".{w=0.5}.{w=0.5}."
    mc sad oe "What the hell is happening?"
    mc om normal "Where the hell is this place?"
    mc cross cm "Is this some kind of weird dream...? But then... why does it feel so real?"
    "Confused, I begin to ponder what happened, and where I even am."
    mc neut ce "Okay, [player]. This is fine..."
    mc "Let's make the most of our circumstances..."
    mc "Just retrace your steps."
    mc "What did you last remember...?"
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
    mc nerv cm "I'm sure if I just make the most of this situation, it'll all turn out fine..."
    mc neut ce ldown rdown "Let's just look around, and see what we have here..."
    mc oe cm nosw "I'm in this strange black void..."
    mc "I don't see or feel anything... But I at least can breathe, right?"
    mc "I'm not floating, am I? I feel grounded... But then why can't I see it?"
    show mc cm ce ldown rdown 
    "I decide to stomp on the \"ground\", if you could even call it that."
    "Nothing interesting happens, but there does seem to be some kind of floor keeping me at my feet -- even if I can't feel it."
    mc cross sad normal "Hmm..."
    mc "There {i}has{/i} to be something here that can help me..."
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
            $ MC.losePercentageAffection(10)
            mc om closed_pensive "What the hell do you mean, {b}\"nobody important\"{/b}?!"
            mc cross "What are you planning to do to me?!{nw}"
            $ _history_list.pop()
            menu:
                mc "What the hell are you planning to do to me?!{fast}"
                "Wait, I'm not going to do anything.":
                    mc sad normal lhip rhip "Well... Can you... at least tell me who you are then?"
                    mc "If you're telling the truth, please do that."
                    menu:
                        "The player.":
                            pass
    mc neut "The... {w=0.5}player?"
    mc cross doub "What, like a video game player?"
    mc curi "Are you saying this is some kind of weird game...?{nw}"
    $ _history_list.pop()
    menu:
        mc "Are you saying this is some kind of weird game...?{fast}"
        "Yes.":
            pass
    mc lhip rhip doub "That... doesn't sound right...?"
    mc "Ahaha, yeah... This is just some dream."
    mc cross ce cm "Well, I'll just, play along until I wake up, then."
    mc "..."
    mc sad om nosw "Jeez, this is really hurting my head.{nw}"
    $ _history_list.pop()
    menu:
        mc "Jeez, this is really hurting my head.{fast}"
        "Hey, take it easy.":
            $ persistent.autoload = "ch1_2_segue"
            $ renpy.save_persistent()
            mc neut ce lhip rhip "Alright, I'll try..."
            mc ldown rdown "This is really confusing, though."
        
        "...":
            $ MC.losePercentageAffection(5)
            $ persistent.autoload = "ch1_2_segue"
            $ renpy.save_persistent()
            mc ".{w=0.5}.{w=0.5}."
            mc "Don't you have... anything else to say...?"
            mc "Um... Ahaha..."
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
            $ MC.losePercentageAffection(15)
            $ writeToPersistent("refusedtohelp", True)
            $ persistent.autoload = "ch1_2_choice2"
            $ renpy.save_persistent()

label ch1_2_choice2:
    play music m1 if_changed
    show mc turned sad oval swea ce at t11
    $ config.allow_skipping = False
    $ quick_menu=False
    $ persistent.autoload = "ch1_2_choice2"
    $ delete_all_saves()
    $ renpy.save_persistent()
    mc "That's..."
    mc oe "Why're you acting like this, man?"
    mc ce cm "Don't you realize that I need your help...?"
    mc crazy om "I mean, what if you were in this situation...? You'd be terrified!"
    mc lhip rhip ce cm nosw "Well... Fine then. I'll find my own way."
    mc neut swea "Maybe if I just think about it, I'll...?"
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
    mc lhip rhip om "Can you please help...?{nw}"
    $ _history_list.pop()
    menu:
        mc "Can you please help...?{fast}"
        "You can control the script, can't you?":
            mc anno ce cross "Finally, something useful..."
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
    mc sad normal "I've never coded in my life, though..."
    mc "It seems pretty boring."
    mc cm lhip rhip "But, in this case... I'll try to see if I can see the script."
    mc oe "Hopefully there will be something that can help me, there..."
    mc nerv ldown rdown "But before I do that, can you back everything up on your end...?"
    mc "I'm definitely gonna mess everything up, since I'm pretty useless when it comes to coding... So it'll at least help to have a failsafe, right?{nw}"
    $ _history_list.pop()
    menu:
        mc "I'm definitely gonna mess everything up, since I'm pretty useless when it comes to coding... So it'll at least help to have a failsafe, right?{fast}"
        "Done.":
            pass
    mc happ cross "Thanks."
    mc nerv normal "I think I managed to find the script while you were busy with that...?"
    mc "I don't know, but I'll at least try to look around."
    show mc neut ldown rdown ce
    stop music fadeout 3.0
    window hide
    $ pause(10)
    window show
    mc happ oe "Mm... I think I found something."
    mc "Let me just try it...!"
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
    mc cross om normal_lookaway "I think I also found something else in the script."
    mc neut ce cm lhip rup "It looks like some kind of way for us to more directly communicate...?"
    mc nerv oe ldown rhip "It kind of went over my head, but from reading the documentation, it looks like you can only talk to me through dialog choices?{nw}"
    $ _history_list.pop()
    menu:
        mc "It kind of went over my head, but from reading the documentation, it looks like you can only talk to me through dialog choices?{fast}"
        "Yes.":
            pass
    mc neut "That's no good."
    mc rdown "But if I just..."
    $ run_input(input='show screen talk_screen', output="")
    show screen talk_screen
    mc happ om "There we go!"
    hide screen console_screen
    mc ce cm lhip rhip "Isn't this almost like being a god?"
    mc nerv oe cross "Ahaha... That sounds really conceited.{nw}"
    $ _history_list.pop()
    menu:
        mc "Ahaha... That sounds really conceited.{fast}"
        "No, it's alright, [player]!":
            mc "Ah..."
        
        "All you've done is show a buttons on the screen, so yeah.":
            mc "Ahaha, I truly am the connoisseur of coding..."
            mc "You'll see when they hire me at Google...!"
    mc neut ldown rdown oe "Welp...of course, this isn't very good."
    mc om "I'm truly useless when it comes to coding, I just vomited out some code I saw in the script..."
    mc "Not like there's really any use learning this stuff when it's all some dream..."
    mc cross nerv "I'm still pretty worried that I'll mess everything up, or something like that."
    mc ldown rdown nosw "In any case, I guess I should make the most of my situation..."
    $ p_name = readFromPersistent("player_name", "Player")
    mc neut "So, what's up, [p_name]?"
    $ config.allow_skipping = False
    $ quick_menu=True
    $ persistent.autoload = "ch30_autoload"
    $ delete_all_saves()
    $ renpy.save_persistent()
    jump ch30_loop