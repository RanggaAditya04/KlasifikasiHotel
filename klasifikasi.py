import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('reservasi_hotel.sav', 'rb'))

st.title('Prediksi Pembatalan Pemesanan Hotel')
c1, c2, c3 = st.columns(3)

with c1:
    no_of_adults = st.number_input('Jumlah Orang Dewasa')
    no_of_week_nights = st.number_input('Jumlah Malam yang Dipesan (weekday)')
    lead_time = st.number_input('Jarak Waktu Pesan Dengan Datang')
    no_of_previous_cancellations = st.number_input('Jumlah Pesanan Yang Dibatalkan Sebelumnya')
    no_of_special_requests = st.number_input('Jumlah Permintaan Khusus')

with c2:
    no_of_children = st.number_input('Jumlah Anak-Anak')
    type_of_meal_plan = st.number_input('Jenis Paket Makan')
    market_segment_type = st.number_input('Jenis Pemesanan')
    no_of_previous_bookings_not_canceled = st.number_input('Jumlah Pesanan Yang Tidak Dibatalkan Sebelumnya')

with c3:
    no_of_weekend_nights = st.number_input('Jumlah Malam yang Dipesan (weekend)')
    room_type_reserved = st.number_input('Tipe Kamar')
    repeated_guest = st.number_input('Langganan')
    avg_price_per_room = st.number_input('Rata-rata Harga Per Kamar')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[no_of_adults, no_of_children, no_of_weekend_nights, no_of_week_nights, type_of_meal_plan,
                               room_type_reserved, lead_time, market_segment_type, repeated_guest, no_of_previous_cancellations,
                               no_of_previous_bookings_not_canceled, avg_price_per_room, no_of_special_requests]])

    if (prediksi [0] == 0):
        prediksi = ('Pemesanan Hotel Dibatalkan')
    else:
        prediksi = ('Pemesanan Hotel Tidak Dibatalkan')
st.success(prediksi)