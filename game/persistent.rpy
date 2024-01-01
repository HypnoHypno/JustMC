## TODO: Actually use this system lol. 

init -999 python:
    if not persistent.data: # I hate that I have to do this
        persistent.data = {}
    class memory:
        """
        Instead of setting hundreds of default persistent.(x) values, we only need one using the function below in tandem with persistent.data.get().

        persistent.data stores every persistent variable as a key, and the value of it as the value. If you set default_value to something, it'll automatically return that if the variable name you need isn't in the dict.
        """

        def writeToPersistent(variable_name="", value=None):
            """
            This function will write "variablename: value" to persistent.data.

            Conditions:
                None.
        
            In:
                1. String name of variable you want to add. (Default "".)
                2. What value you want to set to it. (Default None.)
        
            Out:
                The (hopefully) updated persistent.data.
            """
            persistent.data[variable_name] = value
            return persistent.data