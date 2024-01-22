# "topic_name": {"category": ["category1"], "seen": False, "unlocked": False, "pool": False}

label ch30_loop:
    $ idling = True
    if not renpy.showing("mc idle"):
        show mc idle at t11
    window hide
    python:
        pause(Idle.getIdleTime())
        idling = False
        topics = persistent.data.get("topics", {})
        choice = random.choice(list(topics.keys()))
        topics[choice]["seen"] = True
        memory.writeToPersistent("topics", topics)
        renpy.show("mc turned")
        renpy.call(choice)
    jump ch30_loop

label ch30_talkmenu:
    $ idling = False
    $ tmenu = True
    $ chosen_quip = MC.getTalkMenuQuip()
    mc "[chosen_quip]" (interact=False)
    $ ui.interact()
    $ tmenu = False
    jump ch30_loop