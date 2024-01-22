init -990 python:
    if not persistent.data.get("affection_daily_cap", None):
        memory.writeToPersistent("affection_daily_cap", 8)
    
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
            "range": (-10000, -250),
            "multi": 0.25
        },
        # This isn't an affection level, but instead a reserved value incase anything goes wrong.
        "invalid": {
            "range": (float("-inf"), float("inf")),
            "multi": 0.00
        }
    }

    class Affection:
        """
        Class used for every operation that involves MC's affection level.
        """
        def isAffection(affection="neutral", higher=False, lower=False):
            """
            Will return if MC is the affection level specified, or higher/lower if stated so.

            Conditions:
                If higher/lower is set to true.

            In:
                1. The affection level you wish to check for, in lowercase. (Default "neutral".)
                2. Whether or not you want to count the player being above this level of affection. (Default False.)
                3. Whether or not you want to count the player being below this level of affection. (Default False.)

            Out:
                A boolean representing whether or not MC is at/above/below this level of affection.
            """
            try:
                global affection_map
                affmap = affection_map[affection]["range"]
                highercheck = persistent.data.get("affection", 0) >= affmap[0]
                lowercheck = persistent.data.get("affection", 0) <= affmap[1]
                if not (higher or lower) or (higher and lower):
                    return highercheck and lowercheck
                elif higher:
                    return highercheck
                return lowercheck
            except:
                return False

        def getAffection():
            """
            Will return the level of affection MC is at. Prefer using MC.isAffection(affection, higher, lower) over this if you can.

            Conditions:
                For every level of affection, is MC that affection level?

            In:
                Nothing.

            Out:
                A string which is MC's current affection level in lowercase.
            """
            global affection_map
            for afflevel in list(affection_map.keys()):
                if MC.isAffection(affection=afflevel):
                    return afflevel
            return "invalid"

        def gainAffection(affectiongain=0.00, override=False):
            """
            Will earn the affection set above to MC. Will be multiplied by the "multi" value in affection_map for the current affection level.

            Conditions:
                1. Is override set to true?
                2. If override is set to false, will the amount of affection added make the amount gained today higher than the daily cap.
                3. Gaining the amount of affection, will our affection be higher than the high hard cap?
            
            In:
                1. A floating point number representing the amount of affection you want to gain. (Default 0.00.)
                2. Do you want to override the daily cap? (Default False.)

            Out:
                MC's current affection now.
            """
            global affection_map
            affection_hard_cap = affection_map["loving"]["range"][0]
            affectionlvl = MC.getAffection()
            multiplier = affection_map[affectionlvl]["multi"]
            affectiongain *= multiplier
            affgaintoday = persistent.data.get("affection_gain_today", 0)
            affcap = persistent.data.get("affection_daily_cap", 8)
            aff = persistent.data.get("affection", 0)
            
            if affgaintoday + affectiongain > affcap and not override:
                affectiongain = affcap - affgaintoday
            
            aff += affectiongain
            
            if not override:
                memory.writeToPersistent("affection_gain_today", affgaintoday + affectiongain)
            
            if aff > affection_hard_cap:
                aff = affection_hard_cap
            
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff

        def loseFloatAffection(affectionloss=0.00):
            """
            Will lose an amount of affection determined by the float passed.

            Conditions:
                1. Losing the amount of affection, will our affection be less than the low hard cap?

            In:
                A floating point number representing how much affection you want to lose. (Default 0.00.)

            Out:
                MC's current affection now.
            """
            affection_hard_cap = affection_map["antagonistic"]["range"][0]
            aff = persistent.data.get("affection", 0)
            aff -= affectionloss
            if aff < affection_hard_cap:
                aff = affection_hard_cap
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff
        
        def losePercentageAffection(affectionloss=0.00):
            """
            Will lose a percentage of affection determined by the float passed. (If affection is less than 100, will assume that MC has exactly 100.0 affection.)

            Conditions:
                1. Is MC's affection less than 100.0?
                2. Losing the amount of affection, will our affection be less than the low hard cap?

            In:
                A floating point number representing how much percentage of total affection you want to lose. (Default 0.00)

            Out:
                MC's current affection now.
            """
            affection_hard_cap = affection_map["antagonistic"]["range"][0]
            aff = persistent.data.get("affection", 0)
            if aff >= 100.0:
                total_affection = aff
            else:
                total_affection = 100.0
            affectionloss = (affectionloss / 100) * total_affection
            aff -= affectionloss
            if aff < affection_hard_cap:
                aff = affection_hard_cap
            memory.writeToPersistent("affection", aff)
            renpy.save_persistent()
            return aff
