import re


def person_validator(person):
    errors = []
    if not (type(person[0]) == int and person[0]>0):
        errors.append('ID must be an integer > 0')

    if not (type(person[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[1])):
        errors.append('esmdars is Invalid')

    if not (type(person[2]) == int and person[2] > 0):
        errors.append('grade is Invalid')

    if not (type(person[3]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[3])):
        errors.append('teacher is Invalid')

    from datetime import datetime

    def person_validator(person):
        errors = []

        if not (type(person[0]) == int and person[0] > 0):
            errors.append('ID must be an integer > 0')

        if not (type(person[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[1])):
            errors.append('esmdars is Invalid')

        if not (type(person[2]) == int and person[2] > 0):
            errors.append('grade is Invalid')

        if not (type(person[3]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", person[3])):
            errors.append('teacher is Invalid')

        try:
            datetime.strptime(person[4], "%Y-%m-%d")
        except ValueError:
            errors.append('startdate must be in YYYY-MM-DD format')

        if not (type(person[5]) == int and person[5] > 0):
            errors.append('duration is Invalid')

        return errors

    if not (type(person[5]) == int and person[5] > 0):
        errors.append('duration is Invalid')

    return errors


