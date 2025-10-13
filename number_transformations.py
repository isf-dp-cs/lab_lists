# number_transformations.py


def total_sum(num_list):
    '''Returns sum of numbers in num_list'''
    sum = 0
    for num in num_list:
        sum += num
    return sum
 

def minimum(num_list):
    '''Returns the smallest number in num_list'''
    min = num_list[0]
    for num in num_list:
        if num < min:
            min = num

    return min


def maximum(num_list):
    '''Returns the smallest number in num_list'''
    
    max = num_list[0]
    for num in num_list:
        if num > max:
            max = num

    return max 

def biggest_difference(num_list):
    '''Given an array length 1 or more of ints, 
    return the difference between the largest and smallest values in the array. (codingbat)

        Which previous function(s) may be helpful?
    '''
    
    min = minimum(num_list)
    max = maximum(num_list)
    return max - min


if __name__ == '__main__':
    # TODO: write 2 tests for each function using asert 
    assert total_sum([2,4,6]) == 12

    assert minimum([2,4,6]) == 2

    assert maximum([2,4,6]) == 6

    assert biggest_difference([2,4,6]) == 4


