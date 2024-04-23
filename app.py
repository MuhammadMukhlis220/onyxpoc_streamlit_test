# import module
import streamlit as st

# title
st.title("Ini adalah title")

# header
st.header("Ini adalah header")

# subheader
st.subheader("Ini adalah subheader")

# text
st.text("Ini adalah text")

# markdown
st.markdown("# Ini satu hashtag markdown")
st.markdown("## Ini dua hashtag markdown")
st.markdown("### Ini tiga hashtag markdown")
st.markdown("#### Ini empat hashtag markdown")
st.markdown("##### Ini lima hashtag markdown")
st.markdown("###### Ini enam hashtag markdown")


# markdown multibaris
st.markdown("""
            # multibaris markdown hashtag satu
            ## multibaris markdown hashtag dua
            ### multibaris markdown hashtag tiga
            """, True)

# code
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# latex
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')