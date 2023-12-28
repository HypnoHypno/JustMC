label ch30_autoload:
    $ config.allow_skipping = False
    $ delete_all_saves()
    $ persistent.chapter = 30
    $ persistent.idling = False
    $ renpy.save_persistent()
    python:
        if persistent.last_visit > datetime.now():
            raise TimeError
        one_day_ago = datetime.now() - timedelta(days=1)
        if not persistent.last_visit or persistent.last_visit <= one_day_ago:
            persistent.affection_gain_today = 0
    python:
        if persistent.last_visit > datetime.now():
            renpy.quit()
    play music t5
    scene bg bedroom
    show mc turned neut at t11
    show screen talk_screen
    jump ch30_greeting

label ch30_greeting:
    mc "[persistent.affection] [persistent.affection_gain_today]"
    $ persistent.last_visit = datetime.now()
    jump ch30_loop