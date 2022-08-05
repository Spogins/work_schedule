from datetime import datetime, timedelta, date


# параметры принимаемые функцией
# для ввода даты строкой исп формат 00-00-0000
START = '05-08-2022' #date.today()
END = '05-09-2022' #START+timedelta(days=10)
WORK = 2
SKIP = 2


def work_schedule(date_start=START, date_end=END, days_work=WORK, days_skip=SKIP):
    # форматирование в iso datetime если дата представлена строкой разделенными '-' символами 00-00-0000
    if type(START) == str:
        date_start = datetime.strptime(START, '%d-%m-%Y').date()
    if type(END) == str:
        date_end = datetime.strptime(END, '%d-%m-%Y').date()

    # создание списка для хранения рабочих дней
    data = []
    # высчитывание общего количества дней в расписании
    schedule = date_end - date_start
    schedule = int(schedule.days)
    # интервал для вычисления выходных дней
    interval = days_work + days_skip

    # цикл расписания
    for x in range(0, schedule, interval):
        # цикл добавления рабочих дней
        for y in range(days_work):
            # вычисление следующего рабочего дня
            n_date = date_start + timedelta(days=x+y)
            # условие добавления новой даты в список / выход из цикла
            if n_date < date_end or len(data) != schedule:
                data.append(n_date)
            else:
                return data
    return data


print(work_schedule())
