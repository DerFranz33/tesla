from tesla import Tesla
from batterypack import Batterypack

def tests_tesla():
    t = Tesla('y', 'kebab')
    assert(t.type == 3)
    t.type = 'x'
    assert(t.type == 3)
    t.type = 'X'
    assert(t.type == 'X')
    assert(t.colour == 'Solid Black')
    t.colour ='Midnight Silver'
    assert(t.colour == 'Midnight Silver')
    assert(t.mileage == 0)
    t.mileage = -10
    assert(t.mileage == 0)
    t.mileage = 'kippe'
    assert(t.mileage == 0)
    t.mileage = 1000
    assert(t.mileage == 1000)

def tests_batterypack():
    b = Batterypack(20)
    assert(b.kwh == 70)
    b.kwh = 85
    assert(b.kwh == 85)
    

tests_tesla()
tests_batterypack()