import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from streamlit_option_menu import option_menu
# import plotly.graph_objects as go
import matplotlib.pyplot as plt
# pio.templates.default = "plotly_white"

primaryColor="#6eb52f"
backgroundColor="#f0f0f5"
secondaryBackgroundColor="#e0e0ef"
textColor="#262730"
font="sans serif"
st.set_page_config("Stocks",page_icon=':chart_with_upwards_trend:')
today=datetime.date.today()
var=option_menu("Select the Stocks you want to view",options=['Apple','Google','Adobe','Tesla','Microsoft'],
                icons=['apple','google','file-pdf','ev-front','microsoft'],orientation='vertical')
#options=["AAPL","MSFT","GOOG","ADBE","TSLE"]
if var=='Apple':
    ticker='AAPL'
elif var=='Google':
    ticker='GOOG'
elif var=='Adobe':
    ticker='ADBE'
elif var=='Tesla':
    ticker='TSLA'
elif var=='Microsoft':
    ticker='MSFT'
list=yf.download(ticker,start="2024-08-01",end=today)
# st.write(list)
# hist=ticker.history(period="ly")
# st.write(hist)
# splits=ticker.close
# st.write(splits)
# def colour_background(col):
#     return ['background:yellow' for _ in col]
# styled_list1=list.style.apply(colour_background,subset=['Open'])
# st.table(styled_list1)

# def colour_background1(col1):
#     return ['background:#262730' for _ in col1]
# styled_list=list.style.apply(colour_background1,subset=['Close'])
st.header(f"Stocks of {var}")
st.dataframe(list)
# st.subheader(f"Stocks of {var}")
# col1,col2=st.columns()
st.subheader("Closing Stock value Analysis")
st.line_chart(list,y="Close")
st.subheader("Opening Stock value Analysis")
st.line_chart(list,y="High")
st.header("Compare two different Company Stocks")
a=st.selectbox("Select Company-1",options=['Apple','Google','Adobe','Tesla','Microsoft'])
b=st.selectbox("Select Company-2",options=['Apple','Google','Adobe','Tesla','Microsoft'])
if a=='Apple':
    ticker='AAPL'
elif a=='Google':
    ticker='GOOG'
elif a=='Adobe':
    ticker='ADBE'
elif a=='Tesla':
    ticker='TSLA'
elif a=='Microsoft':
    ticker='MSFT'

if b=='Apple':
    ticker='AAPL'
elif b=='Google':
    ticker='GOOG'
elif b=='Adobe':
    ticker='ADBE'
elif b=='Tesla':
    ticker='TSLA'
elif b=='Microsoft':
    ticker='MSFT'
list1=yf.download(ticker,start="2024-08-01",end=today)
list2=yf.download(ticker,start="2024-08-01",end=today)

list1['High'] = list1['Close'].pct_change()
list2['High'] = list2['Close'].pct_change()

# # Create a figure to visualize the daily returns
# fig = go.Figure()
# fig=plt.figure(figsize=(10,10))

# fig.add_trace(go.Scatter(x=list1.index, y=list1['High'],
#                          mode='lines', name=f'{list1}', line=dict(color='blue')))
# fig.add_trace(go.Scatter(x=list2.index, y=list2['High'],
#                         mode='lines', name=f'{list2}', line=dict(color='green')))

# fig.update_layout(title=f'Stock Analysis for {list1} and {list2}',
#                   xaxis_title='Date', yaxis_title='High',
#                   legend=dict(x=0.02, y=0.95))

# fig.show()
# fig,ax=plt.subplots(figsize=(10,6))
# ax.plot(a,a['Close'])
# ax.plot(b,b['Close'])
# ax.set_title("Share Stock Price")
# ax.xlabel("Date")
# ax.ylabel("Stock Price")
# ax.grid(True)
# ax.legend()

# st.pyplot(fig)