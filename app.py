import streamlit as st
import streamlit.components.v1 as components

def main():
    st.title('Index Fund Trend Prediction')

    option = st.selectbox('Select an option:', ['S&P 500', 'NASDAQ 100', 'Russell 2000', 'Dow Jones Industrial Average'])

    if option == 'Dow Jones Industrial Average':
        HtmlFile = open("graphs/DJI.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code,height = 600)
    elif option == 'NASDAQ 100':
        HtmlFile = open("graphs/NDX.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code,height = 600)
    elif option == 'Russell 2000':
        HtmlFile = open("graphs/RUT.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code,height = 600)
    elif option == 'S&P 500':
        HtmlFile = open("graphs/snp.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code,height = 600)

if __name__ == "__main__":
    main()
