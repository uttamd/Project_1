try:
    a = list(input('Enter the marks'))
    assert len(a)<0,'insert some elements'
except AssertionError:
    raise('no value inserted')


