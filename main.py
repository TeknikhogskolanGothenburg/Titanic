import pyreadr


def main():
    result = pyreadr.read_r('titanic_data.rda')  # also works for Rds, rda

    # done! let's see what we got
    # result is a dictionary where keys are the name of objects and the values python
    # objects
    print(result.keys())  # let's check what objects we got
    df1 = result["titanic_data"]  # extract the pandas data frame for object df1
    df1.to_csv('titanic.csv')

if __name__ == '__main__':
    main()