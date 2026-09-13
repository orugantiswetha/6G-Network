import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="6G Smart Factory Dashboard",
    page_icon="🏭",
    layout="wide"
)

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: #666666;
    margin-bottom: 25px;
}

.section-title {
    font-size: 28px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)
st.markdown(
    '<div class="main-title">🏭 6G Smart Factory Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Impact of 6G Network Performance on Manufacturing Efficiency in Smart Factories'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

st.sidebar.title("⚙️ Dashboard Controls")

line = st.sidebar.selectbox(
    "Production Line",
    [
        "All Production Lines",
        "Production Line 1",
        "Production Line 2",
        "Production Line 3",
        "Production Line 4"
    ]
)

hours = st.sidebar.slider(
    "Number of Hours",
    min_value=6,
    max_value=24,
    value=24
)

st.sidebar.divider()

st.sidebar.markdown("###  6G Target Values")

st.sidebar.write("Latency: < 1 ms")
st.sidebar.write("Reliability: > 99.90%")
st.sidebar.write("Throughput: > 20 Gbps")
st.sidebar.write("OEE: > 85%")
np.random.seed(42)

time_values = pd.date_range(
    end=pd.Timestamp.now().floor("h"),
    periods=24,
    freq="h"
)

lines = [
    "Production Line 1",
    "Production Line 2",
    "Production Line 3",
    "Production Line 4"
]

records = []

for current_time in time_values:

    for current_line in lines:

        latency = np.random.uniform(0.35, 1.2)

        reliability = np.random.uniform(
            99.90,
            99.999
        )

        throughput = np.random.uniform(
            20,
            30
        )

        production = np.random.uniform(
            400,
            550
        )

        utilization = np.random.uniform(
            75,
            98
        )

        oee = np.random.uniform(
            80,
            98
        )

        defects = np.random.uniform(
            0.5,
            3.0
        )

        downtime = np.random.uniform(
            2,
            15
        )

        energy = np.random.uniform(
            0.7,
            1.5
        )

        records.append({
            "Time": current_time,
            "Production Line": current_line,
            "6G Latency (ms)": latency,
            "Network Reliability (%)": reliability,
            "6G Throughput (Gbps)": throughput,
            "Production Rate (units/hr)": production,
            "Machine Utilization (%)": utilization,
            "OEE (%)": oee,
            "Defect Rate (%)": defects,
            "Downtime (minutes)": downtime,
            "Energy per Unit (kWh)": energy
        })

df = pd.DataFrame(records)
if line != "All Production Lines":

    df = df[
        df["Production Line"] == line
    ]

    df = df.tail(hours)

else:

    # Select the most recent hours for all production lines
    selected_times = sorted(
        df["Time"].unique()
    )[-hours:]

    df = df[
        df["Time"].isin(selected_times)
    ]

if df.empty:

    st.error("No data available for the selected filters.")
    st.stop()

average_latency = df["6G Latency (ms)"].mean()

average_reliability = df[
    "Network Reliability (%)"
].mean()

average_throughput = df[
    "6G Throughput (Gbps)"
].mean()

average_production = df[
    "Production Rate (units/hr)"
].mean()

average_utilization = df[
    "Machine Utilization (%)"
].mean()

average_oee = df[
    "OEE (%)"
].mean()

average_defect = df[
    "Defect Rate (%)"
].mean()

average_downtime = df[
    "Downtime (minutes)"
].mean()

average_energy = df[
    "Energy per Unit (kWh)"
].mean()
st.markdown(
    '<div class="section-title">'
    ' Current Factory Performance'
    '</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "6G Latency",
        f"{average_latency:.2f} ms"
    )

with col2:
    st.metric(
        "Network Reliability",
        f"{average_reliability:.3f}%"
    )

with col3:
    st.metric(
        "6G Throughput",
        f"{average_throughput:.2f} Gbps"
    )

with col4:
    st.metric(
        "Production Rate",
        f"{average_production:.0f} units/hr"
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "OEE",
        f"{average_oee:.1f}%"
    )

with col2:
    st.metric(
        "Machine Utilization",
        f"{average_utilization:.1f}%"
    )

with col3:
    st.metric(
        "Defect Rate",
        f"{average_defect:.2f}%"
    )

with col4:
    st.metric(
        "Downtime",
        f"{average_downtime:.1f} min"
    )

st.divider()
st.markdown(
    '<div class="section-title">'
    ' 6G Network Performance'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:

    latency_chart = px.line(
        df,
        x="Time",
        y="6G Latency (ms)",
        markers=True,
        title="6G Network Latency"
    )

    latency_chart.add_hline(
        y=1,
        line_dash="dash",
        annotation_text="Target: 1 ms"
    )

    st.plotly_chart(
        latency_chart,
        width="stretch"
    )
with col2:

    reliability_chart = px.line(
        df,
        x="Time",
        y="Network Reliability (%)",
        markers=True,
        title="6G Network Reliability"
    )

    reliability_chart.add_hline(
        y=99.90,
        line_dash="dash",
        annotation_text="Target: 99.90%"
    )

    st.plotly_chart(
        reliability_chart,
        width="stretch"
    )

col1, col2 = st.columns(2)
with col1:

    throughput_chart = px.line(
        df,
        x="Time",
        y="6G Throughput (Gbps)",
        markers=True,
        title="6G Network Throughput"
    )

    st.plotly_chart(
        throughput_chart,
        width="stretch"
    )
with col2:

    network_scatter = px.scatter(
        df,
        x="6G Latency (ms)",
        y="Network Reliability (%)",
        size="6G Throughput (Gbps)",
        title="6G Latency vs Network Reliability"
    )

    st.plotly_chart(
        network_scatter,
        width="stretch"
    )

st.markdown(
    '<div class="section-title">'
    ' Manufacturing Performance'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:

    production_chart = px.line(
        df,
        x="Time",
        y="Production Rate (units/hr)",
        markers=True,
        title="Production Rate"
    )

    st.plotly_chart(
        production_chart,
        width="stretch"
    )
with col2:

    oee_chart = px.line(
        df,
        x="Time",
        y="OEE (%)",
        markers=True,
        title="Overall Equipment Effectiveness (OEE)"
    )

    oee_chart.add_hline(
        y=85,
        line_dash="dash",
        annotation_text="Target: 85%"
    )

    st.plotly_chart(
        oee_chart,
        width="stretch"
    )
col1, col2 = st.columns(2)
with col1:

    utilization_chart = px.line(
        df,
        x="Time",
        y="Machine Utilization (%)",
        markers=True,
        title="Machine Utilization"
    )

    st.plotly_chart(
        utilization_chart,
        width="stretch"
    )
with col2:

    downtime_chart = px.bar(
        df,
        x="Time",
        y="Downtime (minutes)",
        title="Machine Downtime"
    )

    st.plotly_chart(
        downtime_chart,
        width="stretch"
    )

st.markdown(
    '<div class="section-title">'
    ' Product Quality'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:

    defect_chart = px.line(
        df,
        x="Time",
        y="Defect Rate (%)",
        markers=True,
        title="Product Defect Rate"
    )

    st.plotly_chart(
        defect_chart,
        width="stretch"
    )
with col2:

    energy_chart = px.line(
        df,
        x="Time",
        y="Energy per Unit (kWh)",
        markers=True,
        title="Energy Consumption per Unit"
    )

    st.plotly_chart(
        energy_chart,
        width="stretch"
    )
st.markdown(
    '<div class="section-title">'
    ' Impact of 6G on Manufacturing'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)
with col1:

    impact_chart = px.scatter(
        df,
        x="6G Latency (ms)",
        y="Production Rate (units/hr)",
        size="OEE (%)",
        title="6G Latency vs Production Rate",
        hover_data=[
            "Network Reliability (%)",
            "OEE (%)"
        ]
    )

    st.plotly_chart(
        impact_chart,
        width="stretch"
    )
with col2:

    reliability_oee = px.scatter(
        df,
        x="Network Reliability (%)",
        y="OEE (%)",
        size="Production Rate (units/hr)",
        title="Network Reliability vs OEE",
        hover_data=[
            "6G Latency (ms)",
            "Production Rate (units/hr)"
        ]
    )

    st.plotly_chart(
        reliability_oee,
        width="stretch"
    )

col1, col2 = st.columns(2)

with col1:

    throughput_production = px.scatter(
        df,
        x="6G Throughput (Gbps)",
        y="Production Rate (units/hr)",
        size="OEE (%)",
        title="6G Throughput vs Production Rate"
    )

    st.plotly_chart(
        throughput_production,
        width="stretch"
    )

with col2:

    latency_oee = px.scatter(
        df,
        x="6G Latency (ms)",
        y="OEE (%)",
        size="Production Rate (units/hr)",
        title="6G Latency vs OEE"
    )

    st.plotly_chart(
        latency_oee,
        width="stretch"
    )

st.markdown(
    '<div class="section-title">'
    ' Factory Performance Comparison'
    '</div>',
    unsafe_allow_html=True
)

comparison = pd.DataFrame({

    "Metric": [
        "Machine Utilization",
        "OEE",
        "Network Reliability",
        "Production Efficiency"
    ],

    "Value": [
        average_utilization,
        average_oee,
        average_reliability,
        min(
            average_production / 5,
            100
        )
    ]
})

comparison_chart = px.bar(
    comparison,
    x="Metric",
    y="Value",
    title="Key Factory Performance Indicators",
    text_auto=".2f"
)

st.plotly_chart(
    comparison_chart,
    width="stretch"
)

st.markdown(
    '<div class="section-title">'
    ' Correlation Analysis'
    '</div>',
    unsafe_allow_html=True
)

correlation_columns = [
    "6G Latency (ms)",
    "Network Reliability (%)",
    "6G Throughput (Gbps)",
    "Production Rate (units/hr)",
    "Machine Utilization (%)",
    "OEE (%)",
    "Defect Rate (%)",
    "Downtime (minutes)"
]

correlation = df[
    correlation_columns
].corr()

correlation_chart = px.imshow(
    correlation,
    text_auto=".2f",
    aspect="auto",
    title="Relationship Between 6G and Manufacturing Metrics"
)

st.plotly_chart(
    correlation_chart,
    width="stretch"
)

st.markdown(
    '<div class="section-title">'
    ' Automated Insights'
    '</div>',
    unsafe_allow_html=True
)

if average_latency < 1:

    st.success(
        f" 6G latency is excellent at "
        f"{average_latency:.2f} ms. "
        "Low latency supports real-time industrial communication."
    )

else:

    st.warning(
        f" Average latency is "
        f"{average_latency:.2f} ms. "
        "Network optimization may improve automation response."
    )

# Reliability insight

if average_reliability >= 99.90:

    st.success(
        f" Network reliability is "
        f"{average_reliability:.3f}%, "
        "which meets the dashboard target."
    )

else:

    st.warning(
        f" Network reliability is "
        f"{average_reliability:.3f}%. "
        "Improving network stability could reduce "
        "production interruptions."
    )

# OEE insight

if average_oee >= 85:

    st.success(
        f" OEE is {average_oee:.1f}%, "
        "indicating strong manufacturing efficiency."
    )

else:

    st.warning(
        f" OEE is {average_oee:.1f}%. "
        "There may be opportunities to improve "
        "production efficiency."
    )

# Utilization insight

if average_utilization >= 85:

    st.success(
        f"✅ Machine utilization is "
        f"{average_utilization:.1f}%, "
        "showing good equipment utilization."
    )

else:

    st.warning(
        f" Machine utilization is "
        f"{average_utilization:.1f}%. "
        "Equipment utilization could be improved."
    )

# Defect insight

if average_defect < 2:

    st.success(
        f" Defect rate is low at "
        f"{average_defect:.2f}%."
    )

else:

    st.warning(
        f" Defect rate is "
        f"{average_defect:.2f}%. "
        "Quality monitoring may be required."
    )

st.markdown(
    '<div class="section-title">'
    ' Factory Data'
    '</div>',
    unsafe_allow_html=True
)

st.dataframe(
    df.round(2),
    width="stretch",
    hide_index=True
)

csv_data = df.to_csv(
    index=False
)

st.download_button(
    label=" Download Factory Data",
    data=csv_data,
    file_name="6G_Smart_Factory_Data.csv",
    mime="text/csv"
)

st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <b> 6G Smart Factory Dashboard</b><br>
        6G Network Performance • Smart Manufacturing • Industrial Efficiency
    </div>
    """,
    unsafe_allow_html=True
)