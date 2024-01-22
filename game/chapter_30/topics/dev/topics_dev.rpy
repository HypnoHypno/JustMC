init -10 python:
    Topics.addTopic(
        topic_name="mc_dialog_example",
        pretty_name="Dialog Example",
        category=["Dev", "Misc"],
        unlocked=(True and True), # You can use conditionals here as shown, but it will require the game to be restarted to update. Set the default value in here, and use Topics.unlockTopic() and Topics.lockTopic() respectively, if you need it to unlock on the spot.
        playersays=False,
        submod=None # If this is Submod dialog, put the name of the Submod it should be attached to.
    )

label mc_dialog_example:
    mc cross "This is example text.{nw}"
    extend om normal_lookaway "{w=0.4} It should show you how to write your own dialog."
    mc nerv om lhip rhip "But... {w=0.6}Should this really be in the mod?"
    mc ce swea "I don't really think so."
    mc oe neut nosw "Mm... {w=0.6}Who's idea was this, anyways?"
    mc nerv normal rdown "I don't think they should be allowed to contribute, {w=0.2}ahaha..."
    return