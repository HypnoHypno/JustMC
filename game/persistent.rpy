## TODO: Actually use this system lol. 

default persistent.data = {}

init python -999:
    def readFromPersistent(variable_name="", default_value=None)
        """
        Instead of setting hundreds of default persistent.(x) values, we only need one using this function.

        persistent.data stores every persistent variable as a key, and the value of it as the value. If you set default_value to something, it'll automatically return that if the variable name you need isn't in the dict.

        Conditions:
            Is "variable_name" in persistent.data?

        In:
            1. String name of variable you want to check. (Default "".)
            2. What value you want by default if it's not there. (Default None.)
        
        Out:
            The variable from persistent.data, or what you inputted as default_value if it's not there.
        """
        if not variable_name in persistent.data:
            return default_value
        else:
            return persistent.data[variable_name]
    
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
        try:
            persistent.data[variable_name] = value
        except:
            pass
        return persistent.data