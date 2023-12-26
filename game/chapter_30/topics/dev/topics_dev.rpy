init -10 python:
    jm_add_new_topic( "mc_dialog_test", ["Dev"] )

label mc_dialog_test:
    show mc turned
    $ getaffection = jm_getaffection()
    mc "I am [getaffection]"
    $ persistent.affection = int(renpy.input("Input a value for affection.", default=persistent.affection, allow="1234567890-"))
    return