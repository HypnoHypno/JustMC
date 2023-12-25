default persistent.topics = []

init python:
    def jm_get_idle_time():
        return random.randint(25, 45)

label ch30_loop:
    $ persistent.can_impatient = True
    $ persistent.idling = True
    if not renpy.showing("mc idle"):
        show mc idle at t11
    window hide
    python:
        pause(jm_get_idle_time())
        persistent.idling = False
        choice = random.choice(persistent.topics)
        renpy.call(choice)
        persistent.idling = True
    jump ch30_loop

label ch30_talkmenu:
    mc "What's up?"
    jump ch30_loop