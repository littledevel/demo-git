from app import Hello

def test_greet():
    h = Hello()
    assert(h.greet() == "Hello World")
