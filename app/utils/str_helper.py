

class StrHelper:

    @staticmethod
    def camel_to_snake_case(input_str: str) -> str:
        """
        >>> StrHelper.camel_to_snake_case("SomeSDK")
        'some_sdk'
        >>> StrHelper.camel_to_snake_case("RServoDrive")
        'r_servo_drive'
        >>> StrHelper.camel_to_snake_case("SDKDemo")
        'sdk_demo'
        """

        chars = []
        for c_idx, char in enumerate(input_str):
            if c_idx and char.isupper():
                nxt_idx = c_idx + 1
                # idea of the flag is to separate abbreviations
                # as new words, show them in lower case
                flag = nxt_idx >= len(input_str) or input_str[nxt_idx].isupper()
                prev_char = input_str[c_idx - 1]
                if prev_char.isupper() and flag:
                    pass
                else:
                    chars.append("_")
            chars.append(char.lower())
        return "".join(chars)
