# "topic_name": {"category": ["category1"], "seen": False, "unlocked": False, "pool": False}

label ch30_loop:
    $ idling = True
    if not renpy.showing("mc idle"):
        show mc idle at t11
    window hide
    python:
        pause(MC.getIdleTime())
        idling = False
        choice = random.choice(list(topics.keys()))
        topics[choice]["seen"] = True
        renpy.show("mc turned")
        renpy.call(choice)
    jump ch30_loop

label ch30_talkmenu:
    $ chosen_quip = MC.getTalkMenuQuip()
    mc "[chosen_quip]"
    jump ch30_loop