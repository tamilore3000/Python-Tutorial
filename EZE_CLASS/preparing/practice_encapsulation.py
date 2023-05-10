class Public:
    def __init__(self):
        pass

    def get(self):
        print("This is a public method\n")

class Protected:
    def __init__(self):
        pass

    def _get(self):
        print("This is a protected class\n")

    def call(self):
        print("This is the call coming from protected")
        print(self._get())

class Private(Protected):
    def __init__(self):
        self.__get
    def __get(self):
        print("This is a Private class\n")
    def called(self):
        print("This is the call coming from private")
        print(self.__get())

p = Public()
p.get()

pr = Protected()
# pr._get() cant be called it is protected 
pr.call()

priv = Private()
priv._get()
# priv.__get() cant be called because it is private
priv.called()