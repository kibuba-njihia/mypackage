from ALX_my_Packages import my_module

def test_top_n():
    """
    Make sure top_n works correctly
    """

    assert my_module.top_n([1,3,54,7,34,5,6,3,7,8,9],4) == [54,34,9,8], 'Incorrect'
    assert my_module.top_n([11,32,34,4,9,3,70],2) == [70,34], 'Incorrect'
    assert my_module.top_n([1,3,25,44,7],2) == [44,25], 'Incorrect'