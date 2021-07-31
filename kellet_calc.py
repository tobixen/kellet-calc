from math import sqrt
try:
    from nose.tools import assert_almost_equal
except:
    assert_almost_equal = lambda x, y: True
    

def daumann_kalk(daumannsvekt, ankertaulengde, dybde, daumannlengde, dausynk):
    l1 = ankertaulengde - daumannlengde
    l2 = daumannlengde
    l2y = dybde*l2/ankertaulengde+dausynk
    l1y = dybde - l2y
    Dy = daumannsvekt
    l1x = sqrt(l1**2-l1y**2)
    l2x = sqrt(l2**2-l2y**2)
    By = l2y*Dy*sqrt(l1**2-l1y**2)/(l1y*(l2y*sqrt(l1**2-l1y**2)/l1y-sqrt(l2**2-l2y**2)))
    Bx = By*sqrt(l2**2-l2y**2)/l2y
    Ay = By-Dy
    Ax = Bx

    assert_almost_equal(Ay, By-Dy)
    assert_almost_equal(l1x**2+l1y**2, l1**2)
    assert_almost_equal(Ax/Ay, l1x/l1y)
    assert_almost_equal(Bx/By, l2x/l2y)
    
    return locals()
