#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""
import statistics as st


def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = st.mean(number_list)
    return mean


def get_median(number_list):
    median = st.median(number_list)
    return median


def main():
    number_list = [39, 54, 32, 11, 99, 5]
    print(get_greatest(number_list))
    print(get_smallest(number_list))
    print(get_mean(number_list))
    print(get_median(number_list))


if __name__ == '__main__':
    main()
