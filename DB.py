import mysql.connector
import pandas as pd

def connectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="I6x8h5c9@",
        database="dashboard_ecommerce",

    )

df = pd.read_csv('orders.csv')

df['order_date'] = pd.to_datetime(df['order_date'])

df['mounth'] = df['order_date'].dt.to_period('M')

monthly_revenue = df.groupby('month')['price'].sum()

print(monthly_revenue)