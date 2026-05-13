import streamlit as st

from src.preprocessing import (
    load_dataset,
    get_instances,
    preprocessing_pipeline
)

from src.bat_algorithm import BatAlgorithm

from src.visualization import (
    plot_route,
    plot_convergence
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(page_title='TSP Bat Algorithm')

st.title('Travelling Salesman Problem')
st.subheader('Bat Algorithm Optimization')

# =====================================
# FILE UPLOAD
# =====================================

uploaded_file = st.file_uploader(
    'Upload CSV Dataset',
    type=['csv']
)

# =====================================
# PARAMETER
# =====================================

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

# =====================================
# MAIN PROCESS
# =====================================

if uploaded_file is not None:

    # Load dataset
    df = load_dataset(uploaded_file)

    st.subheader('Dataset Preview')
    st.dataframe(df)

    # Ambil daftar instance
    instances = get_instances(df)

    # Select instance
    selected_instance = st.selectbox(
        "Pilih Instance TSP",
        instances
    )

    # Preprocessing otomatis
    coords, distance_matrix = preprocessing_pipeline(
    df,
    selected_instance
    )

    # Run Optimization
    if st.button('Run Optimization'):

        ba = BatAlgorithm(
            distance_matrix,
            population_size=population,
            iterations=iterations
        )

        best_route, best_distance, history = ba.optimize()

        st.success('Optimization Completed')

        # =====================================
        # OUTPUT
        # =====================================

        st.subheader('Best Route')
        st.write(best_route)

        st.subheader('Total Distance')
        st.write(round(best_distance, 2))

        # Route Visualization
        route_fig = plot_route(coords, best_route)
        st.pyplot(route_fig)

        # Convergence Graph
        conv_fig = plot_convergence(history)
        st.pyplot(conv_fig)