def test_function():
    def inner_function():
        print('Я')
    inner_function()


#inner_function()    NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
test_function()