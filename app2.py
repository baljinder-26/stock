import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from streamlit_option_menu import option_menu
import plotly_express as px
# import plotly.graph_objects as go

# import plotly.graph_objects as go
# import matplotlib.pyplot as plt
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
    ticker1='AAPL'
elif a=='Google':
    ticker1='GOOG'
elif a=='Adobe':
    ticker1='ADBE'
elif a=='Tesla':
    ticker1='TSLA'
elif a=='Microsoft':
    ticker1='MSFT'

if b=='Apple':
    ticker2='AAPL'
elif b=='Google':
    ticker2='GOOG'
elif b=='Adobe':
    ticker2='ADBE'
elif b=='Tesla':
    ticker2='TSLA'
elif b=='Microsoft':
    ticker2='MSFT'
# list1=yf.download(ticker,start="2024-08-01",end=today)
# data1={'Date':list1.Date,'Open':list1.Open,'High':list1.High,
#         'Low':list1.Low,'Close':list1.Close,'Adj Close':list1['Adj Close']
#         ,'Volume':list1.Volume}
# df=pd.DataFrame(data1)
list1=yf.download(ticker1,start="2024-08-01",end=today)
df=pd.DataFrame(list1)
st.write(df)

list2=yf.download(ticker,start="2024-08-01",end=today)
df1=pd.DataFrame(list2)

df1.rename(columns={'Open':'Open1',"High":"High1","Close":'Close1','Adj Close':"tclose",'Volume':'Vol','Low':'lo'},inplace=True)

# df1.drop(columns=["Date"],axis=1,inplace=True)
# st.write(df1)
df_new= pd.concat((df,df1),axis=1)

st.write(df_new)
# fig=px.line(df_new,y='Open')
st.subheader(f"Comparison Analysis of {a} and {b}")
fig=px.line(df_new,y=['High','High1'])
st.plotly_chart(fig,use_container_width=True)

# df_new= 
st.line_chart(df_new, y=['Open',"Open1"])
# 
# 
# 
# # 
# fig=px.line(list2,y="Hdf1


# fig.add_scatter(y=df1["Close"])
# st.plotly_chart(fig,use_container_width=True)
# st.pyplot(fig)


# st.line_chart(data=[])


