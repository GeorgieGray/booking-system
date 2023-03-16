import os, sys, datetime, math
from typing import Tuple, List
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.booking import Booking 
from models.closure_day import ClosureDay
from models.trading_day import TradingDay
from models.table import Table
from models.booking import Booking
from models.restaurant import Restaurant
from db import session


def view_available_times(restaurant_id: int, group_size: int, booking_day: datetime):
    clean_date = datetime.datetime(year=booking_day.year, month = booking_day.month, day = booking_day.day)
    is_restaurant_closed = session.query(ClosureDay).filter_by(date=clean_date).count() >= 1
    if is_restaurant_closed == True: 
        return []


    day_of_week = booking_day.weekday()
    trading_day = session.query(TradingDay).filter_by(day=day_of_week, restaurant_id=restaurant_id).one()
    is_restaurant_closed = not trading_day.is_open
    if is_restaurant_closed == True: 
        return []

    possible_tables = session.query(Table).\
        filter_by(restaurant_id=restaurant_id).\
        filter(Table.min_seats <= group_size).\
        filter(Table.max_seats >= group_size).all()

    def pick_table_id(x: Table):
        return x.id

    possible_table_ids = list(map(pick_table_id, possible_tables))

    bookings_for_today = session.query(Booking).filter(Booking.table_id.in_(possible_table_ids)).filter_by(date=clean_date).all()

    def get_table_id_and_time(booking: Booking):
        return [booking.table_id, booking.time]

    booked_table_times = list(map(get_table_id_and_time, bookings_for_today))
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    hours_per_booking = math.ceil(restaurant.table_time_limit / 60)

    available_table_and_time_list: List[Tuple[Table, int]] = []

    for time in range(trading_day.opening_time, trading_day.closing_time):
        for table in possible_tables:
            for table_time in booked_table_times:
                booked_table = table_time[0]
                booked_time = table_time[1]
                table_expiry_time = booked_time + hours_per_booking
                table_matches = booked_table == table.id

                time_is_during_booking = time in range(booked_time, table_expiry_time)

                new_booking_expiry_time = time + hours_per_booking
                new_booking_would_conflict = booked_time in range(time, new_booking_expiry_time)

                if table_matches and (time_is_during_booking or new_booking_would_conflict):
                    break
            else:
                available_table_and_time_list.append((table, time))

    def get_time(x):
        return x[1]

    available_times = list(map(get_time, available_table_and_time_list))
    available_times.sort()
    available_times = set(available_times)

    print(f'Possible time slots')
    for x in available_times:
        print(f'{x}:00')

    def get_time_and_table_json(pair: Tuple[Table, int]):
        return (pair[1], pair[0].toDict())

    available_time_table_table_jsons = list(map(get_time_and_table_json, available_table_and_time_list))

    return {
        "available_times": list(available_times),
        "available_time_and_table_pairs": available_time_table_table_jsons
    } 
