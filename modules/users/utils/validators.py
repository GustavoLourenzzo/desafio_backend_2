
class Validators:

    def isNotEmptyString(self, value, min_length = 1):
        if not isinstance(value, str):
            return False
        if len(value) < min_length :
            return False
        
        return True
