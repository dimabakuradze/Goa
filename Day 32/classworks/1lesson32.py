# https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python


def validate_pin(pin):
        if len(pin) == 4 or len(pin) == 6:
            return True 
        else:
            return False 