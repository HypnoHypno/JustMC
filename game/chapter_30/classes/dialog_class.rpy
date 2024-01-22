init -990 python:
    class Dialog:
        """
        Class used for every function relating to generating dialog, or returning dialog.
        Example: Quips, mood-based punctuation and sentence generation.
        """
        def getTalkMenuQuip():
            """
            Will return a sentence which MC will use when clicking on the talk menu.

            Conditionals:
                MC's current mood.

            Out:
                A string containing what MC should say.
            """
            quipmap = { #TODO: in the future, have there be defined quips for every mood, and have variations for different affection levels.
                "fine": [
                    "Hey.",
                    "Yeah?",
                    "What's up?",
                    "What's going on, " + pname + "?",
                    "Oh, me?",
                    "Ah, hi " + pname + ".",
                    "Yo."
                ]
            }
            chosen_quip = random.choice(quipmap["fine"])
            return chosen_quip