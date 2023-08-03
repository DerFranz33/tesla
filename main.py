from tesla import Tesla

def tests_tesla():
    t = Tesla('y')
    assert(t.type == 3)
    t.type = 'x'
    assert(t.type == 3)
    t.type = 'X'
    assert(t.type == 'X')

tests_tesla()