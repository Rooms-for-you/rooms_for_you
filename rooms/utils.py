from datetime import timedelta

def get_dates(room_queryset):
    lista_datas = []

    for reservation in room_queryset:

        checkin = reservation.checkin_date
        checkout = reservation.checkout_date
        
        delta = checkout - checkin

        for i in range(delta.days):
            day = checkin + timedelta(days=i)
            lista_datas.append(day)

    return lista_datas

def get_dates_interval(initial_date, final_date):
        delta = final_date - initial_date
        lista_datas = []

        for i in range(delta.days + 1):
            day = initial_date + timedelta(days=i)
            lista_datas.append(day)

        return lista_datas