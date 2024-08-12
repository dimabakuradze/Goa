# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python


def validate_pin(Pin):
        if len(Pin) == 4 or len(Pin) == 6:
            return True 
        else:
            return False 