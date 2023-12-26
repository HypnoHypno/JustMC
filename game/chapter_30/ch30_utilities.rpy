init -999 python:
    persistent.topics = {}
    
    #---------------------------------------------------------
    # idle
    def jm_add_new_topic(topic_name, category):
        """
        Will add a new random chatter topic to the database.
        
        Conditions:
            1. The topic set isn't already in the database.
        
        In:
            1. A string containing the label name of the topic that you want to add.
            2. A list containing the categories that you want it to be in, in string format. 
               Categories can be anything.
        
        Out:
            A boolean representing whether or not we were successfully able to add it to the database.
        """
        if topic_name not in persistent.topics:
            persistent.topics[topic_name] = (category, renpy.seen_label(topic_name))
            return True
        else:
            return False
    
    def jm_get_idle_time():
        """
        Will return an amount of seconds to wait during idle.
        
        Conditions:
            1. The random chatter frequency set.
        
        In:
            Nothing.
        
        Out:
            An integer representing how many seconds should be waited until the next random chatter.
        """
        return random.randint(25, 45)
    
    #---------------------------------------------------------
    # affection
    # see documents/affection_sanity_and_trust.md for details.
    affection_map = {
        "loving": {
            "range": (550, 10000),
            "multi": 1.75
        },
        "friendly": {
            "range": (250, 549),
            "multi": 1.5
        },
        "warm": {
            "range": (100, 249),
            "multi": 1.25
        },
        "neutral": {
            "range": (-29, 99),
            "multi": 1.00
        },
        "cold": {
            "range": (-99, -30),
            "multi": 0.75
        },
        "hostile": {
            "range": (-249, -100),
            "multi": 0.5
        },
        "antagonistic": {
            "range": (-350, -250),
            "multi": 0.25
        },
        # This isn't an affection level, but instead a reserved value incase anything goes wrong.
        "invalid": {
            "range": (float("-inf"), float("inf")),
            "multi": 0.00
        }
    }
    
    def jm_isaffection(affection="neutral", higher=False, lower=False):
        """
        Will return if MC is the affection level specified, or higher/lower if stated so.
        
        Conditions:
            1. If higher/lower is set to true.
        
        In:
            1. The affection level you wish to check for, in lowercase. (Default "neutral".)
            2. Whether or not you want to count the player being above this level of affection. (Default False.)
            3. Whether or not you want to count the player being below this level of affection. (Default False.)
        
        Out:
            A boolean representing whether or not MC is at/above/below this level of affection.
        """    
        global affection_map
        affmap = affection_map[affection]["range"]
        highercheck = persistent.affection >= affmap[0]
        lowercheck = persistent.affection <= affmap[1]
        if not (higher or lower) or (higher and lower):
            return highercheck and lowercheck
        elif higher:
            return highercheck
        else:
            return lowercheck
    
    def jm_getaffection():
        """
        Will return the level of affection MC is at. Prefer using jm_isaffection(affection, higher, lower) over this.
        
        Conditions:
            1. For every level of affection, is MC that affection level?
        
        In:
            Nothing.
        
        Out:
            A string which is MC's current affection level in lowercase.
        """
        global affection_map
        for afflevel in list(affection_map.keys()):
            if jm_isaffection(affection=afflevel):
                return afflevel