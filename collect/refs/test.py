import datetime



def main():
    start_date = datetime.date(2022, 5, 13)
    end_date = datetime.date(2022, 5, 14)
    delta_date = datetime.timedelta(days=1)
   
    yield start_date.strftime("%Y%m%d")
    print( start_date.strftime("%Y%m%d"))

    while start_date <= end_date:
        start_date += delta_date
        yield start_date.strftime("%Y%m%d")

if __name__ == "__main__":
    a = main()
    b = next(a)
    print(b)

    next(a)
    # next(a)