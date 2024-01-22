init -990 python:
    class Idle:
        """
        Class containing every function relevant to the Chapter 30 Idle loop.
        """
        def getIdleTime():
            """
            Will return an amount of seconds to wait during idle.

            Conditions:
                The random chatter frequency set.
            
            Out:
                An integer representing how many seconds should be waited until the next random chatter.
            """
            return random.randint(25, 45)