import streamlit as st

# Title
st.title("refrigeration and cop calculator")

# Sidebar for option selection
option = st.sidebar.selectbox(
    "select calculation",
    (
        "calculate cop",
        "calculate refrigeration effect",
        "calculate compressor work",
        "calculate heat rejected",
    ),
)


# Calculation functions
def calculate_cop(refrigeration_effect, compressor_work):
    return refrigeration_effect / compressor_work


def calculate_refrigeration_effect(cop, compressor_work):
    return cop * compressor_work


def calculate_compressor_work(refrigeration_effect, cop):
    return refrigeration_effect / cop


def calculate_heat_rejected(refrigeration_effect, compressor_work):
    return refrigeration_effect + compressor_work


# UI Logic based on selected option
if option == "calculate cop":
    st.subheader("calculate cop")
    refrigeration_effect = st.number_input(
        "enter refrigeration effect (kW)", min_value=0.0, value=10.0, step=0.1
    )
    compressor_work = st.number_input(
        "enter compressor work (kW)", min_value=0.0, value=2.0, step=0.1
    )

    if st.button("calculate"):
        if compressor_work > 0:
            cop = calculate_cop(refrigeration_effect, compressor_work)
            st.success(f"COP = {cop:.2f} (dimensionless)")
        else:
            st.error("compressor work must be greater than 0.")

elif option == "calculate refrigeration effect":
    st.subheader("calculate refrigeration effect")
    cop = st.number_input("enter COP", min_value=0.0, value=5.0, step=0.1)
    compressor_work = st.number_input(
        "enter compressor work (kW)", min_value=0.0, value=2.0, step=0.1
    )

    if st.button("calculate"):
        if cop >= 0 and compressor_work >= 0:
            refrigeration_effect = calculate_refrigeration_effect(
                cop, compressor_work
            )
            st.success(f"refrigeration effect = {refrigeration_effect:.2f} kW")
        else:
            st.error("values must be non-negative.")

elif option == "calculate compressor work":
    st.subheader("calculate compressor work")
    refrigeration_effect = st.number_input(
        "enter refrigeration effect (kW)", min_value=0.0, value=10.0, step=0.1
    )
    cop = st.number_input("enter COP", min_value=0.0, value=5.0, step=0.1)

    if st.button("calculate"):
        if cop > 0:
            compressor_work = calculate_compressor_work(
                refrigeration_effect, cop
            )
            st.success(f"compressor work = {compressor_work:.2f} kW")
        else:
            st.error("COP must be greater than 0.")

elif option == "calculate heat rejected":
    st.subheader("calculate heat rejected")
    refrigeration_effect = st.number_input(
        "enter refrigeration effect (kW)", min_value=0.0, value=10.0, step=0.1
    )
    compressor_work = st.number_input(
        "enter compressor work (kW)", min_value=0.0, value=2.0, step=0.1
    )

    if st.button("calculate"):
        if refrigeration_effect >= 0 and compressor_work >= 0:
            heat_rejected = calculate_heat_rejected(
                refrigeration_effect, compressor_work
            )
            st.success(f"heat rejected = {heat_rejected:.2f} kW")
        else:
            st.error("values must be non-negative.")
