if __name__ == "__main__":
    def validate_int(
            message: str = "PLEASE ENTER AN INTEGER",
            maximum: int = None,
            minimum: int = None,
    ):
        try:
            output = int(input(f"{message}"))
            output = int(output)
            if maximum != None or minimum != None:
                if maximum >= output and minimum <= output:
                    pass
                else:
                    print(f"PLEASE HAVE IT WITHIN THE BOUNDS ")
                    output = validate_int(message, maximum, minimum)
        except:
            print(f"NOT AN INTEGER")
            output = validate_int(message, maximum, minimum)

        return output


    def validate_str(
            message: str = "PLEASE ENTER A STRING",
            max_Length: int = None,
            upper: bool = False,
            lower: bool = False,
            alpha: bool = False,
            min_Length: int = None,
    ):
        try:
            output = str(input(f"{message}"))
            length = int(len(output))
            if max_Length != None or min_Length != None:
                if length >= min_Length and length <= max_Length:
                    pass
                else:
                    print(f"PLEASE INPUT A STRING WITHIN THE BOUNDS")
                    output = validate_str(message, max_Length, upper, lower, alpha, min_Length)
            if upper == True:
                output = output.upper()
            if lower == True:
                output = output.lower()
            if alpha == True:
                if output.isalpha() == True:
                    pass
                else:
                    print(f"PLEASE MAKE SURE ITS ONLY LETTERS, NO NUMBERS")
                    output = validate_str(message, max_Length, upper, lower, alpha, min_Length)
        except:
            print(f"PLEASE ENTER A STRING")
            output = validate_str(message, max_Length, upper, lower, alpha, min_Length)

        return output
