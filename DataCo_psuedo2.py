import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import plotly.express as px 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import us

st.set_page_config(layout = 'wide')
df = pd.read_csv('DataCo_Handled.csv')


def page0():
    st.title("DataCo's Historical Data Analysis")
    st.subheader("The following table shows the orders made over the course of 4 years, from 2015 - 2018")
    st.dataframe(df)


def page1():
    st.header("Overview")
    tab1 , tab2 = st.tabs(['Unary', 'Comparison'])
    
    with tab1:
        msk_yr = st.multiselect("Select year(s)", options= df['Order Year'].unique())
        msk_q = st.multiselect('Select Quarter(s)', options= df['Quarter'].unique())
        if st.button("Apply", key='tab1') == True:
            if len(msk_yr) == 1 and len(msk_q) == 1:
                st.divider()
                st.subheader(f"The total net profit achieved in {str(msk_q[0])} of {str(msk_yr[0])} was {round(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)]["Benefit per order"].sum())}$", divider=True)
                col1, col2 = st.columns(2)
                with col1:
                    fig1 = px.line(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Order Month", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Month', y="Benefit per order", title='Time Series Analysis')
                    fig2 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Customer City", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Customer City" , y="Benefit per order", title='Top 10 ordering cities in terms of Total Benefit')
                    st.plotly_chart(fig1)
                    st.plotly_chart(fig2)
                with col2:
                    fig3 = px.pie(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                    fig4 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                    st.plotly_chart(fig3)
                    st.plotly_chart(fig4)
            if len(msk_yr) == 1 and len(msk_q) == 4:
                st.divider()
                st.subheader(f"The total net profit achieved in {str(msk_yr[0])} was {round(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)]["Benefit per order"].sum())}$", divider=True)
                col1, col2 = st.columns(2)
                with col1:
                    fig1 = px.line(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Order Month", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Month', y="Benefit per order", title='Time Series Analysis')
                    fig2 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Customer City", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Customer City" , y="Benefit per order", title='Top 10 ordering cities in terms of Total Benefit')
                    st.plotly_chart(fig1)
                    st.plotly_chart(fig2)
                with col2:
                    fig3 = px.pie(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                    fig4 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                    st.plotly_chart(fig3)
                    st.plotly_chart(fig4)
            if len(msk_yr) == 1 and 1 < len(msk_q) < 4:
                st.divider()
                st.subheader(f"The total net profit achieved in {sorted(msk_q)} of {str(msk_yr[0])} was {round(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)]["Benefit per order"].sum())}$", divider=True)
                col1, col2 = st.columns(2)
                with col1:
                    fig1 = px.line(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Order Month", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Month', y="Benefit per order", title='Time Series Analysis')
                    fig2 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Customer City", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Customer City" , y="Benefit per order", title='Top 10 ordering cities in terms of Total Benefit')
                    st.plotly_chart(fig1)
                    st.plotly_chart(fig2)
                with col2:
                    fig3 = px.pie(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                    fig4 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                    st.plotly_chart(fig3)
                    st.plotly_chart(fig4)
            if len(msk_yr) > 1:
                st.divider()
                st.subheader(f"The total net profit achieved in {sorted(msk_q)} of years {sorted(msk_yr)} was {round(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)]["Benefit per order"].sum())}$", divider=True)
                col1, col2 = st.columns(2)
                with col1:
                    fig1 = px.line(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Order Year", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Year', y="Benefit per order", title='Time Series Analysis')
                    fig2 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Customer City", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Customer City" , y="Benefit per order", title='Top 10 ordering cities in terms of Total Benefit')
                    st.plotly_chart(fig1)
                    st.plotly_chart(fig2)
                with col2:
                    fig3 = px.pie(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                    fig4 = px.histogram(df[df["Order Year"].isin(msk_yr) & df["Quarter"].isin(msk_q)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                    st.plotly_chart(fig3)
                    st.plotly_chart(fig4)
                    
    with tab2:
        msk_yr1 = st.selectbox("Select year for the left side", key="left1", options= df['Order Year'].unique())
        msk_q1 = st.multiselect('Select Quarter(s) for the left side', key='left2', options= df['Quarter'].unique())
        msk_yr2 = st.selectbox("Select year for the right side", key='right1', options= df['Order Year'].unique())
        msk_q2 = st.multiselect('Select Quarter(s) for the right side', key='right2', options= df['Quarter'].unique())
        if st.button("Apply", key='tab2') == True:
            st.divider()
            col1, col2 = st.columns(2)
            with col1:
                fig1 = px.line(df[(df["Order Year"] == msk_yr1) & df["Quarter"].isin(msk_q1)].groupby("Order Month", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Month', y="Benefit per order", title='Time Series Analysis')
                fig2 = px.pie(df[(df["Order Year"] == msk_yr1) & df["Quarter"].isin(msk_q1)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                fig3 = px.histogram(df[(df["Order Year"] == msk_yr1) & df["Quarter"].isin(msk_q1)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                st.plotly_chart(fig1, key = "k1")
                st.plotly_chart(fig2, key = "k2")
                st.plotly_chart(fig3, key = "k3")   
            with col2:
                fig4 = px.line(df[(df["Order Year"] == msk_yr2) & df["Quarter"].isin(msk_q2)].groupby("Order Month", as_index=False).sum().sort_values(by = "order date (DateOrders)"), x='Order Month', y="Benefit per order", title='Time Series Analysis')
                fig5 = px.pie(df[(df["Order Year"] == msk_yr2) & df["Quarter"].isin(msk_q2)], names='Delivery Status', labels='Benefit per order', title='Total Benefit per Delivery status')
                fig6 = px.histogram(df[(df["Order Year"] == msk_yr2) & df["Quarter"].isin(msk_q2)].groupby("Product Name", as_index=False)["Benefit per order"].sum().sort_values(by = "Benefit per order", ascending=False).head(10), x="Product Name" , y="Benefit per order", title='Top 10 selling products')
                st.plotly_chart(fig4, key = "k4")
                st.plotly_chart(fig5, key = "k5")
                st.plotly_chart(fig6, key = "k6")

    
def page2():
    st.header('Sales Analysis')
    tab1, tab2 = st.tabs(['Best Performing', 'Worst Performing'])
    msk_yr = st.sidebar.multiselect("Select year(s)", options=df['Order Year'].unique())
    msk_q = st.sidebar.multiselect("Select quarter(s)", options=df['Quarter'].unique())

    with tab1:
        msk_no = st.slider("Specify the no. of cities" , key= "kjdfh", min_value=5 , max_value=(df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()[df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()['Benefit per order'] > 0].value_counts()).sum() , value= 10, step=5)
        msked_df = df[df['Order Year'].isin(msk_yr) & df['Quarter'].isin(msk_q)]
        c_lst_p = msked_df.groupby(['Customer City'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False).head(msk_no)['Customer City'].unique()
        if st.button("Apply", key='tab21') == True:
            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                fig1 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Customer Segment'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False), names='Customer Segment', values='Benefit per order', title='Total Benefit per Customer Segment')
                fig2 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Category Name'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False).head(10), x= 'Category Name', y= "Benefit per order", title='Total Benefit per Category')
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)
            with col2:
                fig3 = px.line(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Order Month'], as_index=False)['Benefit per order'].sum().sort_values(by='Order Month', ascending=True), x= "Order Month", y= 'Benefit per order', title='Time Series Analysis')
                fig4 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Customer City'], as_index=False)['Order Item Discount Rate'].mean().sort_values(by='Order Item Discount Rate', ascending=False).head(10), x= 'Customer City', y= "Order Item Discount Rate", title='Average Discount Rate per Ordering City')
                st.plotly_chart(fig3)
                st.plotly_chart(fig4)
            with col3:
                fig5 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Order Country'], as_index=False)['Benefit per order'].mean().sort_values(by='Benefit per order', ascending=False).head(10), x= 'Order Country', y= "Benefit per order", title='Total Benefit per target delivery Country')
                fig6 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Order Country'], as_index=False)['Order Item Discount Rate'].mean().sort_values(by='Order Item Discount Rate', ascending=False).head(10), x= 'Order Country', y= "Order Item Discount Rate", title='Average Discount Rate per target delivery Country')
                st.plotly_chart(fig5)
                st.plotly_chart(fig6)
                
    with tab2:
        msk_no = st.slider("Specify the no. of cities" , key= "kjdfg", min_value=5 , max_value=(df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()[df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()['Benefit per order'] < 0].value_counts()).sum() , value= 10, step=5)
        msked_df = df[df['Order Year'].isin(msk_yr) & df['Quarter'].isin(msk_q)]
        c_lst_n = msked_df.groupby(['Customer City'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True).head(msk_no)['Customer City'].unique()
        if st.button("Apply", key='tab22') == True:
            st.divider()
            col1, col2, col3 = st.columns(3)
            with col1:
                fig1 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Customer Segment'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True), names='Customer Segment', values=msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Customer Segment'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True)['Benefit per order'].apply(abs), title='Total Benefit (negative) per Customer Segment')
                fig2 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Category Name'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True).head(10), x= 'Category Name', y= "Benefit per order", title='Total Benefit per Category')
                st.plotly_chart(fig1)
                st.plotly_chart(fig2)
            with col2:
                fig3 = px.line(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Order Month'], as_index=False)['Benefit per order'].sum().sort_values(by='Order Month', ascending=True), x= "Order Month", y= 'Benefit per order', title='Time Series Analysis')
                fig4 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Customer City'], as_index=False)['Order Item Discount Rate'].mean().sort_values(by='Order Item Discount Rate', ascending=False).head(10), x= 'Customer City', y= "Order Item Discount Rate", title='Average Discount Rate per Ordering City')
                st.plotly_chart(fig3)
                st.plotly_chart(fig4)
            with col3:
                fig5 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Order Country'], as_index=False)['Benefit per order'].mean().sort_values(by='Benefit per order', ascending=True).head(10), x= 'Order Country', y= "Benefit per order", title='Total Benefit per target delivery Country')
                fig6 = px.histogram(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Order Country'], as_index=False)['Order Item Discount Rate'].mean().sort_values(by='Order Item Discount Rate', ascending=False).head(10), x= 'Order Country', y= "Order Item Discount Rate", title='Average Discount Rate per target delivery Country')
                st.plotly_chart(fig5)
                st.plotly_chart(fig6)


def page3():
    st.header('Logistics Analysis')
    tab1 , tab2 = st.tabs(['Best Performing' ,'Worst performing'])
    msk_yr = st.sidebar.multiselect("Select year(s)", options=df['Order Year'].unique())
    msk_q = st.sidebar.multiselect("Select quarter(s)", options=df['Quarter'].unique())
    
    with tab1:
        msk_no = st.slider("Specify the no. of cities" , key= "kjdfh", min_value=5 , max_value=(df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()[df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()['Benefit per order'] > 0].value_counts()).sum() , value= 10, step=5)
        msked_df = df[df['Order Year'].isin(msk_yr) & df['Quarter'].isin(msk_q)]
        c_lst_p = msked_df.groupby(['Customer City'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False).head(msk_no)['Customer City'].unique()
        st_f = st.selectbox("Select A US State to perform a logistic study on:", options=msked_df[msked_df['Customer City'].isin(c_lst_p)]['Customer State'].unique())
        def get_state(x):
            state = us.states.lookup(x)
            return state.name if state else None
        if st.button("Apply", key='tab21') == True:
            st.divider()
            st.subheader('Overview Logistics Analysis:')
            col1 , col2 = st.columns(2)
            with col1:
                fig1 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Delivery Status'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False), names='Delivery Status', values='Benefit per order', title='Total Benefit per Delievery Status')
                fig2 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Customer State'], as_index=False)['del_enc'].mean().sort_values(by='del_enc', ascending=False), locationmode='USA-states', locations='Customer State', color='del_enc', hover_name='Customer State', projection='natural earth', color_continuous_scale=px.colors.sequential.amp, title='Shipping delay per Ordering US State')
                st.plotly_chart(fig1)
                st.plotly_chart(fig2) 
            with col2:
                fig3 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Shipping Mode'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False), names='Shipping Mode', values='Benefit per order', title='Total Benefit per Shipping mode')
                fig4 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_p)].groupby(['Order Country', 'Order Country code'], as_index=False)['del_enc'].mean().sort_values(by='del_enc', ascending=False), locationmode='ISO-3', locations='Order Country code', color='del_enc', hover_name='Order Country', projection='natural earth', color_continuous_scale=px.colors.sequential.amp, title='Shipping delay per Target delivery Country')
                st.plotly_chart(fig3)
                st.plotly_chart(fig4)
            st.divider()
            st.subheader(f'Logistics of orders made from the state of {get_state(st_f)}:')
            fig5 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_p)][msked_df['Customer State'] == st_f].groupby(['Order Country', 'Order Country code'], as_index=False)['del_enc'].mean(), locationmode='ISO-3', locations='Order Country code', color='del_enc', hover_name='Order Country', projection='natural earth', color_continuous_scale=px.colors.sequential.amp)
            st.plotly_chart(fig5)
    with tab2:
        msk_no = st.slider("Specify the no. of cities" , key= "kjdfdfdg", min_value=5 , max_value=(df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()[df[(df['Order Year'].isin(msk_yr)) & (df['Quarter'].isin(msk_q))].groupby('Customer City', as_index=False)['Benefit per order'].sum()['Benefit per order'] < 0].value_counts()).sum() , value= 10, step=5)
        msked_df = df[df['Order Year'].isin(msk_yr) & df['Quarter'].isin(msk_q)]
        c_lst_n = msked_df.groupby(['Customer City'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True).head(msk_no)['Customer City'].unique()
        st_f = st.selectbox("Select A US State to perform a logistic study on:", options=msked_df[msked_df['Customer City'].isin(c_lst_p)]['Customer State'].unique(), key=';ldjfajbas')
        def get_state(x):
            state = us.states.lookup(x)
            return state.name if state else None
        if st.button("Apply", key='tab22') == True:
            st.divider()
            st.subheader('Overview Logistics Analysis:')
            col1 , col2 = st.columns(2)
            with col1:
                fig1 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Delivery Status'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False), names='Delivery Status', values=msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Delivery Status'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True)['Benefit per order'].apply(abs), title='Total Benefit per Delievery Status')
                fig2 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Customer State'], as_index=False)['del_enc'].mean().sort_values(by='del_enc', ascending=False), locationmode='USA-states', locations='Customer State', color='del_enc', hover_name='Customer State', projection='natural earth', color_continuous_scale=px.colors.sequential.amp, title='Shipping delay per Ordering US State')
                st.plotly_chart(fig1)
                st.plotly_chart(fig2) 
            with col2:
                fig3 = px.pie(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Shipping Mode'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=False), names='Shipping Mode', values=msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Shipping Mode'], as_index=False)['Benefit per order'].sum().sort_values(by='Benefit per order', ascending=True)['Benefit per order'].apply(abs), title='Total Benefit per Shipping mode')
                fig4 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_n)].groupby(['Order Country', 'Order Country code'], as_index=False)['del_enc'].mean().sort_values(by='del_enc', ascending=False), locationmode='ISO-3', locations='Order Country code', color='del_enc', hover_name='Order Country', projection='natural earth', color_continuous_scale=px.colors.sequential.amp, title='Shipping delay per Target delivery Country')
                st.plotly_chart(fig3)
                st.plotly_chart(fig4)
            st.divider()
            st.subheader(f'Logistics of orders made from the state of {get_state(st_f)}:')
            fig5 = px.choropleth(msked_df[msked_df['Customer City'].isin(c_lst_n)][msked_df['Customer State'] == st_f].groupby(['Order Country', 'Order Country code'], as_index=False)['del_enc'].mean(), locationmode='ISO-3', locations='Order Country code', color='del_enc', hover_name='Order Country', projection='natural earth', color_continuous_scale=px.colors.sequential.amp)
            st.plotly_chart(fig5)
            

pgs = {
    "Overview" : page1,
    "Sales Analysis" : page2,
    "Logistics Analysis" : page3
}

if st.checkbox("Navigate Dashboard") == True:
    pg = st.sidebar.radio("Navigate", options = pgs.keys())
    st.sidebar.divider()
    pgs[pg]()
else:
    page0()

