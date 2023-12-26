# "topic_name": (["category1"], False)
# where False = if it's been seen before
default persistent.topics = {}

label ch30_loop:
    $ persistent.can_impatient = True
    $ persistent.idling = True
    if not renpy.showing("mc idle"):
        show mc idle at t11
    window hide
    python:
        pause(jm_get_idle_time())
        persistent.idling = False
        choice = random.choice(list(persistent.topics.keys()))
        renpy.call(choice)
        persistent.idling = True
    jump ch30_loop

label ch30_talkmenu:
    mc "What's up?"
    jump ch30_loop