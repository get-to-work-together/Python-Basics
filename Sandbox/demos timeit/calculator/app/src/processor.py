"""

>>> p = Processor(); p.keyPressed('1'); p.getDisplay()
'1'
"""

class Processor:

    decimal_character = '.'

    def __init__(self):
        self.invoer = 0
        self.stored = 0
        self.display = 0
        self.operator = ''
        self.decimal = None

    def getDisplay(self):
        return f'{self.display:g}'.replace('.', Processor.decimal_character)

    def keyPressed(self, key):
        key = {'*': '×', '/': '÷', ',': '.'}.get(key, key)

        if key in '1234567890':
            if self.decimal is None:
                self.invoer = self.invoer * 10 + int(key)
                self.display = self.invoer
            else:
                self.decimal += 1
                self.invoer = self.invoer + int(key) / (10 ** self.decimal)
                self.display = self.invoer

        elif key in '÷×−+=':
            self.calculate()
            self.operator = key
            self.invoer = 0
            self.display = self.stored
            self.decimal = None

        elif key == '.':
            self.decimal = 0

        elif key == 'AC':
            self.invoer = 0
            self.stored = 0
            self.operator = ""
            self.display = self.stored
            self.decimal = None

        elif key == '+/−':
            if self.invoer != 0:
                self.invoer = -self.invoer
                self.display = self.invoer

        elif key == '%':
            self.invoer = self.invoer / 100
            self.display = self.invoer

    def calculate(self):
        if self.operator == '+':
            self.stored += self.invoer
        elif self.operator == '−':
            self.stored -= self.invoer
        elif self.operator == '×':
            self.stored *= self.invoer
        elif self.operator == '÷':
            self.stored /= self.invoer
        elif self.operator == "=" or self.operator == "":
            self.stored = self.display


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
