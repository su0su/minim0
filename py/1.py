def validate_pw(pw):
    validate_codition = [
        lambda s: all(x.islower() or x.isupper() or x.isdigit() or (x in ['!', '@', '#', '$', '%', '^', '&', '*', '_']) for x in s),
        lambda s: any(x.isupper() for x in s),
        lambda s: any(x.islower() for x in s),
        lambda s: any(x.isdigit() for x in s),
        lambda s: len(s) == len(s.replace(" ","")),
        lambda s: len(s) >= 10
    ]

    for validator in validate_codition:
        if not validator(pw):
            print(pw)
            print("통과")
            return True
        else :
            print(pw)
            print("불통")
            return False

pw="qQlll1231~341512344"
validate_pw(pw)