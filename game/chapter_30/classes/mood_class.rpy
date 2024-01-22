init -990 python:
    class Mood:
        """
        A class which contains every function that is related to managing the Mood system.
        """
        def getMood():
            return persistent.data.get("mood", "fine") #not done obviously lol