from src.maths_opp import add,sub


def test_add():
    assert add(2,3)==5
    assert add(3,-1)==2
    
def test_sub():
    assert sub(2,3)==-1
    assert sub(3,-1)==4