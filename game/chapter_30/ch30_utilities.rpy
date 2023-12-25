init python:
    def jm_add_new_topic(topic_name):
        if topic_name not in persistent.topics:
            persistent.topics.append(topic_name)
            return True
        else:
            return False