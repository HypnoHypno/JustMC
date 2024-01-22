init -990 python:
    class Topics:
        """
        Class used for everything related to random/pool topics.
        """
        def addTopic(topic_name="mc_dialog_example", pretty_name="Dialog Example", category=["Misc"], unlocked=True, conditional="True", playersays=False, submod=None):
            """
            Will add a new random chatter topic to the database.

            Conditions:
                1. The topic set isn't already in the database.

            In:
                1. A string containing the label name of the topic that you want to add. (Default "mc_dialog_example")
                2. A string containing the in-game name of the topic. (Default "Dialog Example")
                3. A list containing the categories that you want it to be in, in string format.
                    Categories can be anything. (Default ["Misc"])
                4. Do you want this topic to be unlocked or not? (Default False)
                5. A string of a conditional, will be eval'd every time a topic needs to be shown/picked. (Default "true")
                6. Does the player say it (pool topic)? False means it's a random chatter topic. (Default False)
                7. If this is a submod topic, input the string name of the submod it belongs to. (Default None)
            
            Out:
                A boolean representing whether or not we were successfully able to add it to the database.
            """
            topics = persistent.data.get("topics", {})
            if topic_name not in topics:
                new_topic = {topic_name: {"pretty_name": pretty_name, "category": category, "seen": renpy.seen_label(topic_name), "unlocked": unlocked, "conditional": conditional, "pool": playersays, "submod": submod}}
                topics.update(new_topic)
                memory.writeToPersistent("topics", topics)
                return True
            else:
                return False
        
        def changeTopicVariable(topic_name="mc_dialog_example", topic_variable="unlocked", update=True):
            """
            Will update a variable in a topic set. Used internally to unlock and lock topics.

            Conditions:
                1. The topic set is in the database.

            In:
                1. A string containing the label name of the topic that you want to add. (Default "mc_dialog_example")
                2. The key you want to change the value of. (Default "unlocked")
                3. What do you want to change the value to? (Default True)
            
            Out:
                A boolean representing whether or not we were successfully able to update the database.
            """
            if topic_name in topics:
                topics[topic_name][topic_variable] = update
                return True
            else:
                return False
        
        def unlockTopic(topic_name="mc_dialog_example"):
            """
            Will unlock a topic in the database, calls Topics.changeTopicVariable() internally.

            In:
                The name of the topic you want to unlock. (Default "mc_dialog_example")
            
            Out:
                A boolean representing whether or not we were successfully able to update the database.
            """
            return Topics.changeTopicVariable(topic_name=topic_name, topic_variable="unlocked", update=True)

        def lockTopic(topic_name="mc_dialog_example"):
            """
            Will lock a topic in the database, calls Topics.changeTopicVariable() internally.

            In:
                The name of the topic you want to lock. (Default "mc_dialog_example")
            
            Out:
                A boolean representing whether or not we were successfully able to update the database.
            """
            return Topics.changeTopicVariable(topic_name=topic_name, topic_variable="unlocked", update=False)