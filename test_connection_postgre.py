import streamlit as st
import psycopg2
import pandas as pd
import plotly.graph_objects as go

def init_connection():
    return psycopg2.connect(**st.secrets['postgres'])

conn = init_connection()

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query('''
select fa.actor_id, concat(a.first_name, ' ',a.last_name) as full_name, fa.film_id, f.title, f.release_year, l.name as "language" from film_actor fa
join actor a
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id
join language l
on f.language_id = l.language_id 
''')

df = pd.DataFrame(rows)
df.columns = ['actor_id', 'full_name', 'film_id', 'title', 'release_year', 'language']

st.markdown("## Data Frame Used")
st.text("Data Frame 1:")
st.write(
    df.style.set_table_styles([
        {'selector': 'table', 'props': [('overflow', 'auto'), ('height', '400px')]}
    ])
)

rows2 = run_query('''
select rating, count(title) from film
group by rating
''')

df2 = pd.DataFrame(rows2)
df2.columns = ['rating', 'count']

st.text("Data Frame 2:")
st.write(
    df2.style.set_table_styles([
        {'selector': 'table', 'props': [('overflow', 'auto'), ('height', '400px')]}
    ])
)

rows3 = run_query('''
select f.title, c.name from film f
join film_category fc
on f.film_id = fc.film_id 
join category c
on c.category_id = fc.category_id
''')

df3 = pd.DataFrame(rows3)
df3.columns = ['title', 'category_name']

st.text("Data Frame 3:")
st.write(
    df3.style.set_table_styles([
        {'selector': 'table', 'props': [('overflow', 'auto'), ('height', '400px')]}
    ])
)


st.markdown("## Chart:")
df = df.groupby('full_name')['film_id'].count().sort_values(ascending = False).reset_index().head(10)
df.columns = ['actor_name', 'film_count']
fig = go.Figure(go.Bar(x=df['actor_name'], 
                       y=df['film_count'],
                       text=df['film_count'],  # Menambahkan teks pada setiap bar
                        textposition='outside',marker=dict(color=df['film_count'], colorscale='ice', colorbar=dict(title='Count'))
                        ))


fig.update_layout(
    title='Top 10 Most Actor/Actrees Participate in Films:',
    xaxis=dict(type='category', categoryorder='total descending', title='Actor Name'),
    yaxis=dict(title='Film Count'),
    width=700,
    height=500
)
st.plotly_chart(fig)

fig.write_image("bar_chart.png")



fig = go.Figure(go.Pie(
    labels=df2['rating'],
    values=df2['count'],
    textinfo='label+percent+value',
    marker=dict(colors=['#FFA07A', '#87CEEB', '#98FB98', '#FFD700', '#FF69B4'])
))
# fig.update_traces(textposition='inside', textinfo='percent+label') #put annotations
fig.update_layout(
    title='Rating Film Distribution:',
    width=700,
    height=500
)
st.plotly_chart(fig)

fig.write_image("pie_chart.png", format = "png")


df3 = df3['category_name'].value_counts().reset_index().sort_values('count')
# df_reversed = df3[::-1]
fig = go.Figure(go.Bar(
    x=df3['count'],
    y=df3['category_name'],
    text=df3['count'],  # Menambahkan teks pada setiap bar
    textposition='outside',
    orientation='h',marker=dict(color=df3['count'], colorscale='peach', colorbar=dict(title='Count'))
))

# Update layout
fig.update_layout(
    title='Genre Counts:',
    xaxis_title='Count',
    yaxis_title='Genre',
    width=700,
    height=700
)
st.plotly_chart(fig)

fig.write_image("horizontal_bar_chart.png")
