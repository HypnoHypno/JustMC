label ch30_autoload:
    python:
        config.allow_skipping = False
        delete_all_saves()
        idling = False
        tmenu = False
        renpy.save_persistent()
        p_name = persistent.data.get("player_name", "Player")
        if not persistent.data.get("mc_aware", False):
            memory.writeToPersistent("mc_aware", True)
        last_visit = persistent.data.get("last_visit", None)
        if last_visit and last_visit > datetime.now():
            memory.writeToPersistent("player_clock_broken", True)
        one_day_ago = datetime.now() - timedelta(days=1)
        if not last_visit or last_visit <= one_day_ago:
            memory.writeToPersistent("affection_gain_today", 0)
        pname = persistent.data.get("player_name", "Player")
    play music t5
    scene bg bedroom
    show mc turned neut at t11
    show screen talk_screen
    jump ch30_greeting

label ch30_greeting:
    mc "Yo."
    $ memory.writeToPersistent("last_visit", datetime.now())
    jump ch30_loop