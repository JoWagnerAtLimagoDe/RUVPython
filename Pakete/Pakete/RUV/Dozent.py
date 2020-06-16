def foo():
    print ("Hier ist Foo")

def bar():
    print ("Hier ist Bar")

def demo():
    print(__name__)

def __foobar():
    foo()
    bar()


if __name__ == "__main__":
    print("Dies ist ein Modul und sollte nicht direkt aufgerufen werden")