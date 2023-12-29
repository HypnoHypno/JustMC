# "topic_name": {"category": ["category1"], "seen": False, "unlocked": False, "pool": False}
default persistent.topics = {}

label ch30_loop:
    $ persistent.idling = True
    if not renpy.showing("mc idle"):
        show mc idle at t11
    window hide
    python:
        pause(MC.getIdleTime())
        persistent.idling = False
        choice = random.choice(list(persistent.topics.keys()))
        renpy.call(choice)
        persistent.idling = True
    jump ch30_loop

label ch30_talkmenu:
    $ chosen_quip = MC.getTalkMenuQuip()
    mc "[chosen_quip]"
    jump ch30_loop