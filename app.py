import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

st.title('Ethereum Market Regime Explorer')
st.divider()
model =  pickle.load(open('kmeans.pkl','rb'))

dataset = pd.read_csv('./data/coin_Ethereum.csv')
X = dataset.iloc[:,[8,9]].values
y_kmeans = model.fit_predict(X)

fig,ax = plt.subplots()
ax.scatter(X[y_kmeans == 0,0],X[y_kmeans == 0,1], s = 100, c = 'red', label = 'cluster 1')
ax.scatter(X[y_kmeans == 1,0],X[y_kmeans == 1,1], s = 100, c = 'blue', label = 'cluster 2')
ax.scatter(X[y_kmeans == 2,0],X[y_kmeans == 2,1], s = 100, c = 'green', label = 'cluster 3')
ax.scatter(X[y_kmeans == 3,0],X[y_kmeans == 3,1], s = 100, c = 'cyan', label = 'cluster 4')

ax.set_title('ETH-regime')
ax.set_xlabel('Volume')
ax.set_ylabel('Market Cap')
plt.legend()
st.pyplot(fig)

st.markdown('###### Volume: Volume of transactions')
st.markdown('###### Market Cap: Market Capitalisation in USD')

st.markdown(f"""
    <div style = "
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0,0.05);
                text-align: center;
            ">
    <h4 style="margin:0; font-size: 18px; color: green">Low Activity / Bearish periods </h4>
    <p style="margin: 8px 0 0; color: #555; font-size: 16px;"> Low Volume + Low Market Cap </p>
    </div>
""",unsafe_allow_html=True)

st.markdown(f"""
    <div style = "
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0,0.05);
                text-align: center;
            ">
    <h4 style="margin:0; font-size: 18px; color: red">Stable / Consolidation phases </h4>
    <p style="margin: 8px 0 0; color: #555; font-size: 16px;"> Moderate Volume + Moderate Market Cap </p>
    </div>
""",unsafe_allow_html=True)

st.markdown(f"""
    <div style = "
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0,0.05);
                text-align: center;
            ">
    <h4 style="margin:0; font-size: 18px; color: blue">Bullish / accumulation phases </h4>
    <p style="margin: 8px 0 0; color: #555; font-size: 16px;"> High Volume + High Market Cap </p>
    </div>
""",unsafe_allow_html=True)

st.markdown(f"""
    <div style = "
                border: 1px solid #e8e8e8;
                border-radius: 12px;
                padding: 16px;
                background: #fafafa;
                box-shadow: 0 4px 8px rgba(0,0,0,0,0.05);
                text-align: center;
            ">
    <h4 style="margin:0; font-size: 18px; color: cyan">High-volatility / event-driven days </h4>
    <p style="margin: 8px 0 0; color: #555; font-size: 16px;"> Very High Volume + Very High Market Cap </p>
    </div>
""",unsafe_allow_html=True)