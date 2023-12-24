label ch0_0:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    mc "Ugh... {w}I {i}hate{/i} mondays."
    "Mornings have always been the worst, sorrounded by the noise of chatter all around me."
    "Large friend groups talk as they walk to school together -- Meanwhile, I hang my head down, trying to ignore it all."
    "I couldn't care less about making new friends, people are usually {i}very{/i} tiring to talk to."
    "Sure, I'd like to meet some girls, but I've never had enough motivation to do it."
    "Could I even impress one with my mediocre socialization skills?"
    "In fact, I don't really have motivation to do anything with my life."
    "I've always been content enough as a recluse, staying at home and watching anime... {w}So why even bother?"
    scene black
    with fade
    "I sigh as I reach the school building... {w=0.5}Today is going to be a long day."
    "Let's just get this over with..."

label ch0_1:
    stop music fadeout 2.0
    scene bg class_day
    with fade
    ".{w=0.5}.{w=0.5}."
    "This class is taking {w=0.1}{cps=*1.2}{b}ages{/b}{/cps}."
    "Usually I can at least get a rough picture of what the teacher is talking about, but I just can't focus on it today."
    "What's the point of even paying attention when I know it's just going to be some useless crap that won't serve me anything in my life?"
    "So I look around the classroom, to see if there's anything even remotely interesting happening."
    "Instead, I'm greeted with the endless sea of likeminded students, who seem to be just as affected by the dull lecture."
    "But luckily, I have a plan to stave off the boredom."
    "I take a book out of my bag -- it's my copy of {i}Half Piece Redux{/i}."
    "I open it under the desk, beginning to scan the pages intently."
    ".{w=0.5}.{w=0.5}."
    $ t = Character("Teacher", what_prefix='"', what_suffix='"')
    t "[player]?"
    mc "Uh... {w=0.2}Yes?"
    "I quickly stop looking at the book and turn my head up to face him, hoping that I haven't been caught."
    t "What role do mitochondria have in the cell?"
    mc "They're the powerhouse."
    t "What nitrogenous base in RNA pairs with adenine in DNA?"
    mc "Uhm... {w=0.2}Uracil?"
    t "What are you holding under your desk?"
    mc "{i}Half Piece Redux{/i} volume 723--{nw}"
    "{b}Crap{/b}."
    t "This is the {i}fifth{/i} time this month, {b}[player]{/b}."
    "The professor takes out his phone and starts typing something on it."
    "Am I in trouble?"
    t "Councelor's office, third floor, room 307. {w=0.3}{i}Now.{/i}"
    "I guess that answers it for me."
    "I sigh, beginning to exit the classroom as the teacher points towards the door."

label ch0_2:
    play music t5
    scene bg corridor
    with wipeleft_scene
    "At least this could be worse."
    extend " I could be sitting in class with nothing interesting to do or look at."
    "I slowly walk across the school, scanning the posters, as I approach the stairs."
    "I go upstairs -- A section of the school I rarely visit, being generally used for third-year classes and activities."
    "I stop to observe one of the bulletin boards. It has a list of the clubs on it."
    mc "Hmm..."
    mc "The drama club... {w}The debate club... {w}{i}The anime club{/i}."
    "They all have their club presidents, and their contact information listed. {w=0.2}Except for one..."
    mc "The literature club?"
    "I guess whoever started the club couldn't find any members and eventually gave up."
    "Or the teachers started it in hope someone would get interested."
    "Either way, I'm not surprised in the slightest that no one wants to join it. {w=0.2}-- Literature isn't any more exciting than the lecture I had to endure."
    "Before I totally lose my train of thought, I remind myself of why I was even here in the first place."
    "I don't want to get in any more trouble than I'm already in, after all."
    mc "Right, I should hurry to the councelor's office."

label ch0_3:
    scene bg club_day
    with wipeleft_scene
    "I look inside the classroom, wondering if I'm at the right place."
    "Why does the councelor even use a classroom? Shouldn't he have his own office?"
    $ c = Character("Councelor", what_prefix='"', what_suffix='"')
    mc "Hello?"
    c "Ah, yes, [player]. Come in."
    "I begrudgingly enter the classroom."
    c "In case you're confused, my office is currently being renovated, so I borrowed this unused classroom."
    mc "Ah."
    mc ".{w=0.5}.{w=0.5}."
    mc "Okay."
    c "In any case..."
    c "I was told that you weren't paying attention during class?"
    mc "..."
    c "Don't worry, you aren't in trouble."
    mc "Why not?"
    c "If it was up to him, you would be, but I have a more constructive approach to the problem at hand."
    c "You've considered joining a club, no?"
    mc "Well, yes... {w=0.2}But I don't have the motivation to do it."
    "Without any words, he hands me a list of clubs. It's identical to the one in the hallway."
    "I look to the literature club... {w}It's still blank."
    mc "Why isn't there a name or contact for the literature club?"
    c "This school has a literature club?"
    mc "Yes, it's right here."
    "I return the list, letting the councelor double-check it."
    c "One moment."
    "He starts typing something into his computer."
    $ pause(2)
    c "There doesn't appear to be a literature club registered."
    c "It's most likely a clerical error. You should look for another club to join."
    "Hearing his words, I come up with an idea."
    mc "If the literature club doesn't exist now, can I start it?"
    c "You want to start a literature club?"
    c "I didn't know you had an interest in {i}{b}actual literature{/b}{/i}, [player]."
    "...I let that slide."
    "Well, I don't really care about \"actual\" literature..."
    extend " But neither does anyone else in this school, which means that {i}nobody{/i} will join it and I won't have to deal with anyone."
    "And I might be able to use it as an excuse to read my manga during class too!"
    mc "Ah, well..."
    mc "This could be a chance to broaden my horizons?"
    c "Hm."
    "He looks at me suspiciously. I hope I'm not being too obvious with this."
    c "It sounds like all you needed was a little push."
    c "Just fill in your name, phone and email here, and consider it done."
    c "You'll be told where the clubroom will be soon afterwards."
    "He hands me a paper and pen, and I grab it."
    stop music fadeout 2.0
    "Okay, let's see how this goes."
    menu:
        "Sign the paper.":
            pass
    $ config.allow_skipping = False
    "With pen in hand, I begin to write my name and contact onto the paper."
    "It's done now."
    "I suddenly--{nw}"
    $ quick_menu=False
    $ persistent.autoload = "ch1_0" # Point of no return.
    $ persistent.affection = 0
    $ renpy.save_persistent()
    play music "mod_assets/audio/frequency.mp3"
    call glitch(0.25)
    image bg club_day3 = "bg/club-skill.png"
    scene bg club_day3
    mc "AAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHH{nw}"
    call glitch(0.25)
    scene bg kitchen
    mc "MY HEAD{nw}"
    call glitch(0.5)
    scene bg bedroom
    mc "WHAT'S HAPPENING?!?!{nw}"
    call glitch(0.5)
    scene s_kill_bg2
    mc "WHAT THE HELL IS HAPPENING TO ME{nw}"
    call glitch(1)
    python:
        import os
        import pyautogui
        import subprocess
        import time
        pyautogui.FAILSAFE = False # This will make it so that if the mouse moves to a corner of the screen, it will keep typing.
        notepad_process = subprocess.Popen(["notepad.exe"])
        time.sleep(1)
        message = "H E L P  M E !  "
        message = message * 50
        pyautogui.typewrite(message, interval=0.01) # Write into our notepad.
        notepad_process.terminate()
    stop music
    python:
        pyautogui.alert(text="Please help me.", title="MC.chr")
        renpy.quit()

label glitch(time=1):
    window hide(None)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/glitch1.ogg"
    $ pause(time)
    stop sound
    hide screen tear
    window show(None)
    return