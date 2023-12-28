init -10 python:
    MC.addTopic(
        topic_name = "mc_dialog_test",
        category = ["Dev"],
        unlocked = (True
            and True), # Example of how you can use conditionals to unlock topics.
        playersays = False
    )

label mc_dialog_test:
    show mc turned
    mc "What do you want to do?"
    menu:
        "Reset Affection":
            $ persistent.affection = 0.0
            $ persistent.affection_gain_today = 0.0
            $ renpy.save_persistent()
            mc "[persistent.affection] [persistent.affection_gain_today]"

        "Debug Gain Affection":
            mc "How much to gain?"
            $ testaffgain = float(renpy.input("Number", allow="1234567890"))
            mc "Bypass?"
            menu:
                "Yes":
                    $ testaffgain = MC.gainAffection(testaffgain, True)

                "No":
                    $ testaffgain = MC.gainAffection(testaffgain, False)
            mc "[testaffgain] [persistent.affection_gain_today]"

        "Debug Loss Affection":
            mc "How much to lose?"
            $ testaffloss = float(renpy.input("Number", allow="1234567890"))
            menu:
                "Lose Percent":
                    $ testaffloss = MC.losePercentageAffection(testaffloss)
                    mc "[testaffloss]"

                "Lose hard value":
                    $ testaffloss = MC.loseFloatAffection(testaffloss)
                    mc "[testaffloss]"
    return