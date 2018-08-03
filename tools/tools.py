class Tools:

    @staticmethod
    def is_char_a_number(c):

        """

        Checks if a certain character is a valid num

        """

        try:

            int(c)

            return True

        except Exception:

            return False

    def string_is_a_number(self, s):

        """

        Uses above method for strings

        """

        return [self.is_char_a_number(c) for c in s]

    def is_expression_valid(self, a):

        """
        Checking expression syntax for validity by comparing string_is_a_number array with created pattern-array based
        on length
        :param a: string_is_a_number
        :return: True if syntax is correct, false if syntax is senseless
        """
        a = self.string_is_a_number(a)
        lng_array = len(a)
        if lng_array < 2:
            return False
        pattern_list = [True, False] * (lng_array / 2) + [True]

        if pattern_list == a:
            return True

        else:
            return False

    def evaluate_complete_expression(self, b):

        b = self.evaluate_divdide_multiplicate_first(b)
        complete_expression = list(b)
        occ = 1

        while occ == 1:
            occ = 0
            for dx, val in enumerate(complete_expression):
                if occ == 1:
                    break
                if val == '+' or val == '-':
                    single_expression = complete_expression[dx - 1:dx + 2]
                    del complete_expression[dx - 1]
                    del complete_expression[dx]
                    if val == '+':
                        result = int(single_expression[0]) + int(single_expression[2])
                        complete_expression[dx - 1] = result
                        occ = 1
                    elif val == '-':
                        result = int(single_expression[0]) - int(single_expression[2])
                        complete_expression[dx - 1] = result
                        occ = 1


        return complete_expression

    @staticmethod
    def evaluate_divdide_multiplicate_first(l):
        """
        Taking math expression as list and looks for multiplicate or divide operators and evaluates them first
        . While-Loop for the case of multiple operators and quitting if no searched operator
        found anymore
        :param l:
        :return:
        """

        complete_expression = list(l)
        occ = 1

        while occ == 1:
            occ = 0
            for dx, val in enumerate(complete_expression):
                if occ == 1:
                    break
                if val == '*' or val == '/':
                    single_expression = complete_expression[dx - 1:dx + 2]
                    del complete_expression[dx - 1]
                    del complete_expression[dx]
                    if val == '*':
                        result = int(single_expression[0]) * int(single_expression[2])
                        complete_expression[dx - 1] = result
                        occ = 1
                    elif val == '/':
                        result = int(single_expression[0]) / int(single_expression[2])
                        complete_expression[dx - 1] = result
                        occ = 1
        return complete_expression
