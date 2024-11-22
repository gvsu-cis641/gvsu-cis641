# sources: 
# * https://www.datacamp.com/tutorial/test-driven-development-in-python
# * https://testdriven.io/blog/modern-tdd/

def sum_two_numbers(a, b):
    return a + b

def test_sum_two_numbers():
    assert(sum_two_numbers(4, 8) == 12)
