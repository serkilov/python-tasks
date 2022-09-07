from calendar import Calendar


class TestDate:
    def test_thursday(self):
        month = 9
        year = 2022
        date = max(
            [
                date
                for date in Calendar().itermonthdates(year, month)
                if date.month == month and date.weekday() == 3
            ]
        ).strftime("%d.%m.%Y")
        print()
        print(f"Month: {month}, Year: {year}")
        print(f"Date: {date}")
