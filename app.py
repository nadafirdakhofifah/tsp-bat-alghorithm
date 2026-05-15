import streamlit as st

from src.preprocessing import (
    load_dataset,
    extract_coordinates,
    create_distance_matrix
)

from src.bat_algorithm import BatAlgorithm
from src.nearest_neighbor import NearestNeighbor

from src.visualization import (
    plot_route,
    plot_convergence
)


st.set_page_config(page_title='TSP Bat Algorithm')

st.title('Travelling Salesman Problem')
st.subheader('Bat Algorithm & Nearest Neighbor Optimization')

algorithm = st.selectbox(
    'Pilih Algoritma',
    ['Bat Algorithm', 'Nearest Neighbor']
)

uploaded_file = st.file_uploader(
    'Upload CSV Dataset',
    type=['csv']
)

iterations = st.slider(
    'Jumlah Iterasi',
    10,
    500,
    100
)

population = st.slider(
    'Jumlah Bat',
    5,
    100,
    20
)


if uploaded_file is not None:

    df = load_dataset(uploaded_file)

    st.subheader('Dataset Preview')
    st.dataframe(df)

    coords = extract_coordinates(df)

    distance_matrix = create_distance_matrix(coords)

    if st.button('Run Optimization'):

    # =====================================
    # BAT ALGORITHM
    # =====================================

        if algorithm == 'Bat Algorithm':

            ba = BatAlgorithm(
                distance_matrix,
                population_size=population,
                iterations=iterations
            )

            best_route, best_distance, history, logs = (
                ba.optimize()
            )

    # =====================================
    # NEAREST NEIGHBOR
    # =====================================

        else:

            nn = NearestNeighbor(distance_matrix)

            best_route, best_distance, history, logs = (
                nn.optimize()
            )

        st.success('Optimization Completed')

        st.subheader('Best Route')
        st.write(best_route)

        st.subheader('Total Distance')
        st.write(round(best_distance, 2))
        st.subheader("Optimization Progress")

        for log in logs:
            st.text(log)

        route_fig = plot_route(coords, best_route)
        st.pyplot(route_fig)

        conv_fig = plot_convergence(history)
        st.pyplot(conv_fig)