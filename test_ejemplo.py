from ejemplo import suma

def test_suma():
    assert suma(2,3) ==5
    assert suma(-1,1) ==0
    assert suma(0,0) ==0
    assert suma(100,200) ==300
    assert suma (-5,-5) ==-10