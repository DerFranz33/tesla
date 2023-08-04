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
    # charge()
    current_status = t._battery.status
    t._charge()
    assert(t._battery.status > current_status)
    # can_drive()
    t._panel_broken = True
    assert(t._can_drive() == False)
    t._panel_broken = False
    assert(t._can_drive() == True)

def tests_batterypack():
    # kwh
    b = Batterypack(20)
    assert(b.kwh == 70)
    b.kwh = 85
    assert(b.kwh == 85)
    # status
    assert(b.status == 25)
    # charge()
    assert(b.n_charged == 0)
    b.charge()
    assert(b.status > 25)
    assert(b.n_charged == 1)
    # n_charged
    for times in range(10020):
        b.charge()
    assert(b.n_charged == 10000)
    # battery spend effects
    current_status = b.status
    b.charge()
    assert(b.status == current_status)
    assert(b._battery_spend == True)
    # at this point, status could not have been charged more than its max kwh
    current_kwh = b.kwh
    assert(b.status <= b.kwh)
    # juice()
    b2 = Batterypack(100)
    assert(b2.kwh == 100)
    assert(b2.status == 25)
    assert(b2._battery_spend == False)
    b2.charge()
    current_status = b2.status
    assert(b2._battery_spend == False)
    assert(b2.status <= b2.kwh)
    b2.juice(current_status)
    assert(b2.status == 0)
    assert(b2._battery_spend == False)
    b2.juice(1)
    assert(b2._battery_spend == True)
    assert(b2.status == 0)
    

    

tests_tesla()
tests_batterypack()