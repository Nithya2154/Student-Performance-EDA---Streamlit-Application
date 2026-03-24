"""
Student Performance EDA - Streamlit Application
Comprehensive exploratory data analysis with interactive visualizations
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Page config
st.set_page_config(
    page_title="Student Performance EDA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 5px solid #1f77b4;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    h1 {
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    h2 {
        color: #2c3e50;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load data


@st.cache_data
def load_data():
    df = pd.read_csv('Students_Performance_Processed.csv')

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert attendance to numeric
    df['Attendance_Numeric'] = pd.to_numeric(
        df['Average attendance on class'].astype(str).str.extract('(\d+)')[0],
        errors='coerce'
    )

    # Fill any missing values
    df['Attendance_Numeric'].fillna(
        df['Attendance_Numeric'].median(), inplace=True)

    return df


# Load data
df = load_data()

# Sidebar Navigation
st.sidebar.title("🎓 Student Performance EDA")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Dashboard",
    [
        "🏠 Home",
        "📍 Demographics",
        "🎓 Academic Performance",
        "📚 Study Habits",
        "🎯 Skills & Interests",
        "🏥 Health & Resources",
        "🔗 Correlations",
        "⭐ High vs Low Performers",
        "⚠️ Risk Analysis",
        "📊 Data Explorer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.subheader("📈 Quick Stats")
col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("Total Students", f"{len(df):,}")
with col2:
    st.metric("Avg CGPA", f"{df['What is your current CGPA?'].mean():.2f}")

col1, col2 = st.sidebar.columns(2)
with col1:
    st.metric("Avg Age", f"{df['Age'].mean():.1f}")
with col2:
    st.metric("Male %", f"{(df['Gender'] == 'Male').sum()/len(df)*100:.1f}%")

# ============================================================================
# PAGE: HOME
# ============================================================================
if page == "🏠 Home":
    st.title("📊 Student Performance EDA Dashboard")
    st.markdown("### Comprehensive Analysis of 1,194 Students")

    st.info("""
    This interactive dashboard provides a complete exploratory data analysis of student performance 
    across academics, study habits, resources, and personal factors. 
    Navigate using the sidebar to explore different aspects of the data.
    """)

    # Key Statistics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1,194</div>
            <div class="metric-label">Total Students</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">3.17</div>
            <div class="metric-label">Avg CGPA</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">36.7%</div>
            <div class="metric-label">High Performers</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">25.0%</div>
            <div class="metric-label">In Probation</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Main Statistics
    st.subheader("📈 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("**Admission Year Range**")
        st.write(
            f"From {df['University Admission year'].min()} to {df['University Admission year'].max()}")

    with col2:
        st.write("**CGPA Range**")
        st.write(
            f"From {df['What is your current CGPA?'].min():.2f} to {df['What is your current CGPA?'].max():.2f}")

    with col3:
        st.write("**Age Range**")
        st.write(f"From {df['Age'].min()} to {df['Age'].max()} years")

    st.markdown("---")

    # Key Insights
    st.subheader("🔑 Key Insights")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Strongest CGPA Predictor:**")
        st.success("Previous SGPA (+0.85 correlation) ⭐⭐⭐⭐⭐")
        st.write("**Other Strong Factors:**")
        st.info(
            "• Daily Study Hours (+0.42)\n• Family Income (+0.28)\n• Skill Development (+0.12)")

    with col2:
        st.write("**Negative Factors:**")
        st.error(
            "• Excessive Social Media (-0.18)\n• Low Attendance\n• No Teacher Consultancy")
        st.write("**Success Patterns:**")
        st.success(
            "• 55% attend teacher consultancy\n• 42% in co-curriculum activities\n• 98.7% have smartphone access")

    st.markdown("---")

    # Navigation Guide
    st.subheader("📖 Dashboard Guide")

    guide_cols = st.columns(3)

    with guide_cols[0]:
        st.write("**Demographics**")
        st.write("Gender, age, income, and cohort distributions")

    with guide_cols[1]:
        st.write("**Academic Performance**")
        st.write("CGPA, attendance, probation, and semester trends")

    with guide_cols[2]:
        st.write("**Study Habits**")
        st.write("Study hours, learning mode, social media usage")

    guide_cols = st.columns(3)

    with guide_cols[0]:
        st.write("**Skills & Interests**")
        st.write("Top skills, career interests, co-curriculum impact")

    with guide_cols[1]:
        st.write("**Health & Resources**")
        st.write("English proficiency, scholarship, devices")

    with guide_cols[2]:
        st.write("**Advanced Analysis**")
        st.write("Correlations, risk factors, detailed comparisons")

# ============================================================================
# PAGE: DEMOGRAPHICS
# ============================================================================
elif page == "📍 Demographics":
    st.title("📍 Demographic Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Male Students", f"{(df['Gender'] == 'Male').sum()}",
                  f"{(df['Gender'] == 'Male').sum()/len(df)*100:.1f}%")
    with col2:
        st.metric("Female Students", f"{(df['Gender'] == 'Female').sum()}",
                  f"{(df['Gender'] == 'Female').sum()/len(df)*100:.1f}%")
    with col3:
        st.metric("Avg Age", f"{df['Age'].mean():.1f} years",
                  f"Range: {df['Age'].min()}-{df['Age'].max()}")

    st.markdown("---")

    # Gender Distribution
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Gender Distribution")
        gender_data = df['Gender'].value_counts()
        fig = go.Figure(data=[
            go.Pie(
                labels=gender_data.index,
                values=gender_data.values,
                hole=0.3,
                marker=dict(colors=['#1f77b4', '#ff7f0e'])
            )
        ])
        fig.update_layout(height=400, showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Age Distribution")
        fig = go.Figure(data=[
            go.Histogram(x=df['Age'], nbinsx=20, marker_color='#1f77b4')
        ])
        fig.update_layout(
            xaxis_title="Age (years)",
            yaxis_title="Count",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Age Groups
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age Group Distribution")
        age_groups = pd.cut(df['Age'], bins=[0, 20, 22, 25, 100], labels=[
                            '18-20', '21-22', '23-24', '25+'])
        age_data = age_groups.value_counts().sort_index()
        fig = go.Figure(data=[
            go.Bar(x=age_data.index, y=age_data.values, marker_color='#2ca02c')
        ])
        fig.update_layout(
            xaxis_title="Age Group",
            yaxis_title="Count",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Admission Year Trends")
        admit_data = df['University Admission year'].value_counts(
        ).sort_index()
        fig = go.Figure(data=[
            go.Scatter(x=admit_data.index, y=admit_data.values, mode='lines+markers',
                       line=dict(color='#d62728', width=3),
                       marker=dict(size=8))
        ])
        fig.update_layout(
            xaxis_title="Admission Year",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Family Income
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Family Income Distribution")
        fig = go.Figure(data=[
            go.Histogram(x=df['What is your monthly family income?'], nbinsx=30,
                        marker_color='#9467bd')
        ])
        fig.update_layout(
            xaxis_title="Monthly Family Income (Rs.)",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Income Statistics")
        income_stats = df['What is your monthly family income?'].describe()
        stats_df = pd.DataFrame({
            'Metric': ['Mean', 'Median', 'Std Dev', 'Min', 'Max'],
            'Value': [
                f"Rs. {income_stats['mean']:,.0f}",
                f"Rs. {income_stats['50%']:,.0f}",
                f"Rs. {income_stats['std']:,.0f}",
                f"Rs. {income_stats['min']:,.0f}",
                f"Rs. {income_stats['max']:,.0f}"
            ]
        })
        st.table(stats_df)

    # Current Semester
    st.subheader("Current Semester Distribution")
    semester_data = df['Current Semester'].value_counts().sort_index()
    fig = go.Figure(data=[
        go.Bar(x=semester_data.index, y=semester_data.values,
               marker_color='#17becf')
    ])
    fig.update_layout(
        xaxis_title="Semester",
        yaxis_title="Number of Students",
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: ACADEMIC PERFORMANCE
# ============================================================================
elif page == "🎓 Academic Performance":
    st.title("🎓 Academic Performance Analysis")

    cgpa_col = 'What is your current CGPA?'

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Avg CGPA", f"{df[cgpa_col].mean():.2f}", "Scale: 0-4.0")
    with col2:
        st.metric("High Performers",
                  f"{(df[cgpa_col] >= 3.5).sum()}", "CGPA ≥ 3.5")
    with col3:
        st.metric("Low Performers",
                  f"{(df[cgpa_col] < 2.5).sum()}", "CGPA < 2.5")
    with col4:
        st.metric(
            "In Probation", f"{(df['Did you ever fall in probation?'] == 'Yes').sum()}", "25% of students")

    st.markdown("---")

    # CGPA Distribution
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CGPA Distribution")
        fig = go.Figure(data=[
            go.Histogram(x=df[cgpa_col], nbinsx=20, marker_color='#1f77b4')
        ])
        avg_cgpa = df[cgpa_col].mean()
        fig.add_vline(x=avg_cgpa, line_dash="dash", line_color="red",
                      annotation_text=f"Mean: {avg_cgpa:.2f}", annotation_position="top right")
        fig.update_layout(
            xaxis_title="CGPA",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("CGPA Categories")
        cgpa_cat = pd.cut(df[cgpa_col],
                          bins=[0, 2.5, 3.0, 3.5, 3.75, 4.0],
                          labels=['Below Avg', 'Satisfactory', 'Good', 'Very Good', 'Excellent'])
        cat_data = cgpa_cat.value_counts().sort_index()
        colors_map = {'Below Avg': '#d62728', 'Satisfactory': '#ff7f0e',
                      'Good': '#ffdd00', 'Very Good': '#90ee90', 'Excellent': '#2ca02c'}
        fig = go.Figure(data=[
            go.Bar(x=cat_data.index, y=cat_data.values,
                   marker=dict(color=[colors_map.get(x, '#1f77b4') for x in cat_data.index]))
        ])
        fig.update_layout(
            xaxis_title="CGPA Category",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Attendance vs CGPA
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Attendance vs CGPA")
        fig = go.Figure(data=[
            go.Scatter(x=df['Attendance_Numeric'], y=df[cgpa_col], mode='markers',
                       marker=dict(size=5, color=df[cgpa_col], colorscale='Viridis',
                                   showscale=True, colorbar=dict(title="CGPA")))
        ])
        # Add trend line
        z = np.polyfit(df['Attendance_Numeric'].dropna(),
                       df[cgpa_col].dropna(), 1)
        p = np.poly1d(z)
        x_trend = np.linspace(
            df['Attendance_Numeric'].min(), df['Attendance_Numeric'].max(), 100)
        fig.add_trace(go.Scatter(x=x_trend, y=p(x_trend), mode='lines',
                                 name='Trend', line=dict(color='red', width=3)))
        fig.update_layout(
            xaxis_title="Attendance (%)",
            yaxis_title="CGPA",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Probation Status")
        probation_data = df['Did you ever fall in probation?'].value_counts()
        fig = go.Figure(data=[
            go.Pie(
                labels=probation_data.index,
                values=probation_data.values,
                marker=dict(colors=['#2ca02c', '#d62728']),
                hole=0.3
            )
        ])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    # CGPA by Gender and Learning Mode
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CGPA by Gender")
        gender_cgpa = df.groupby('Gender')[cgpa_col].agg(
            ['mean', 'std', 'count'])
        fig = go.Figure(data=[
            go.Bar(x=gender_cgpa.index, y=gender_cgpa['mean'],
                   error_y=dict(type='data', array=gender_cgpa['std']),
                   marker=dict(color=['#1f77b4', '#ff7f0e']))
        ])
        fig.update_layout(
            xaxis_title="Gender",
            yaxis_title="Average CGPA",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("CGPA by Learning Mode")
        mode_cgpa = df.groupby('What is your preferable learning mode?')[
            cgpa_col].agg(['mean', 'std', 'count'])
        fig = go.Figure(data=[
            go.Bar(x=mode_cgpa.index, y=mode_cgpa['mean'],
                   error_y=dict(type='data', array=mode_cgpa['std']),
                   marker=dict(color=['#2ca02c', '#1f77b4']))
        ])
        fig.update_layout(
            xaxis_title="Learning Mode",
            yaxis_title="Average CGPA",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Credits vs CGPA
    st.subheader("Credits Completed vs CGPA")
    fig = go.Figure(data=[
        go.Scatter(x=df['How many Credit did you have completed?'], y=df[cgpa_col],
                   mode='markers',
                   marker=dict(size=5, color=df['Age'], colorscale='Rainbow',
                               showscale=True, colorbar=dict(title="Age")))
    ])
    fig.update_layout(
        xaxis_title="Credits Completed",
        yaxis_title="CGPA",
        height=400,
        hovermode='closest'
    )
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: STUDY HABITS
# ============================================================================
elif page == "📚 Study Habits":
    st.title("📚 Study Habits & Engagement Analysis")

    study_col = 'How many hour do you study daily?'
    social_col = 'How many hour do you spent daily in social media?'
    skill_col = 'How many hour do you spent daily on your skill development?'
    cgpa_col = 'What is your current CGPA?'

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Study Hours",
                  f"{df[study_col].mean():.2f}", "hours/day")
    with col2:
        st.metric("Avg Social Media",
                  f"{df[social_col].mean():.2f}", "hours/day (HIGH!)")
    with col3:
        st.metric("Avg Skill Dev", f"{df[skill_col].mean():.2f}", "hours/day")

    st.markdown("---")

    # Study Hours Distribution
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Daily Study Hours Distribution")
        study_data = df[study_col].value_counts().sort_index()
        fig = go.Figure(data=[
            go.Bar(x=study_data.index, y=study_data.values,
                   marker_color='#1f77b4')
        ])
        fig.update_layout(
            xaxis_title="Hours/Day",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Social Media Usage Distribution")
        fig = go.Figure(data=[
            go.Histogram(x=df[social_col], nbinsx=15, marker_color='#ff7f0e')
        ])
        fig.update_layout(
            xaxis_title="Hours/Day",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Study Hours vs CGPA
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Study Hours vs CGPA")
        fig = go.Figure(data=[
            go.Scatter(x=df[study_col], y=df[cgpa_col], mode='markers',
                       marker=dict(size=6, color=df[cgpa_col], colorscale='Viridis',
                                   showscale=True, colorbar=dict(title="CGPA")))
        ])
        # Trend line
        z = np.polyfit(df[study_col], df[cgpa_col], 1)
        p = np.poly1d(z)
        x_trend = np.linspace(df[study_col].min(), df[study_col].max(), 100)
        fig.add_trace(go.Scatter(x=x_trend, y=p(x_trend), mode='lines',
                                 name='Trend', line=dict(color='red', width=3)))
        fig.update_layout(
            xaxis_title="Study Hours/Day",
            yaxis_title="CGPA",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Social Media vs CGPA")
        fig = go.Figure(data=[
            go.Scatter(x=df[social_col], y=df[cgpa_col], mode='markers',
                       marker=dict(size=6, color=df[cgpa_col], colorscale='Viridis',
                                   showscale=True, colorbar=dict(title="CGPA")))
        ])
        # Trend line
        z = np.polyfit(df[social_col], df[cgpa_col], 1)
        p = np.poly1d(z)
        x_trend = np.linspace(df[social_col].min(), df[social_col].max(), 100)
        fig.add_trace(go.Scatter(x=x_trend, y=p(x_trend), mode='lines',
                                 name='Trend', line=dict(color='red', width=3)))
        fig.update_layout(
            xaxis_title="Social Media Hours/Day",
            yaxis_title="CGPA",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    # Learning Mode
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Learning Mode Preference")
        mode_data = df['What is your preferable learning mode?'].value_counts()
        fig = go.Figure(data=[
            go.Pie(labels=mode_data.index, values=mode_data.values,
                   marker=dict(colors=['#2ca02c', '#1f77b4']), hole=0.3)
        ])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Study Sessions per Day")
        session_data = df['How many times do you seat for study in a day?'].value_counts(
        ).sort_index()
        fig = go.Figure(data=[
            go.Bar(x=session_data.index, y=session_data.values,
                   marker_color='#9467bd')
        ])
        fig.update_layout(
            xaxis_title="Sessions/Day",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Study Level Impact
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Study Levels and CGPA")
        study_level = pd.cut(df[study_col], bins=[0, 2, 4, 15],
                             labels=['Low (1-2h)', 'Moderate (3-4h)', 'High (5+h)'])
        level_cgpa = df.groupby(study_level)[cgpa_col].agg(['mean', 'count'])
        fig = go.Figure(data=[
            go.Bar(x=level_cgpa.index, y=level_cgpa['mean'],
                   marker=dict(color=['#d62728', '#ff7f0e', '#2ca02c']))
        ])
        fig.update_layout(
            xaxis_title="Study Level",
            yaxis_title="Average CGPA",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Study Hours by Learning Mode")
        mode_study = df.groupby('What is your preferable learning mode?')[
            study_col].mean()
        fig = go.Figure(data=[
            go.Bar(x=mode_study.index, y=mode_study.values,
                   marker=dict(color=['#2ca02c', '#1f77b4']))
        ])
        fig.update_layout(
            xaxis_title="Learning Mode",
            yaxis_title="Average Study Hours/Day",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: SKILLS & INTERESTS
# ============================================================================
elif page == "🎯 Skills & Interests":
    st.title("🎯 Skills & Interests Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Students in Co-Curriculum",
                  f"{(df['Are you engaged with any co-curriculum activities?'] == 'Yes').sum()}",
                  f"{(df['Are you engaged with any co-curriculum activities?'] == 'Yes').sum()/len(df)*100:.1f}%")
    with col2:
        st.metric("Avg Skill Dev Hours",
                  f"{df['How many hour do you spent daily on your skill development?'].mean():.2f}",
                  "hours/day")
    with col3:
        st.metric("With Scholarship",
                  f"{(df['Do you have meritorious scholarship ?'] == 'Yes').sum()}",
                  f"{(df['Do you have meritorious scholarship ?'] == 'Yes').sum()/len(df)*100:.1f}%")

    st.markdown("---")

    # Top Skills
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top 15 Skills")
        skills_data = df['What are the skills do you have ?'].value_counts().head(
            15)
        fig = go.Figure(data=[
            go.Bar(y=skills_data.index, x=skills_data.values, orientation='h',
                   marker_color='#1f77b4')
        ])
        fig.update_layout(
            xaxis_title="Number of Students",
            yaxis_title="Skill",
            height=500,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Top 15 Interested Areas")
        interests_data = df['What is you interested area?'].value_counts().head(
            15)
        fig = go.Figure(data=[
            go.Bar(y=interests_data.index, x=interests_data.values, orientation='h',
                   marker_color='#ff7f0e')
        ])
        fig.update_layout(
            xaxis_title="Number of Students",
            yaxis_title="Area",
            height=500,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Co-curriculum
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Co-Curriculum Participation")
        cocurr_data = df['Are you engaged with any co-curriculum activities?'].value_counts()
        fig = go.Figure(data=[
            go.Pie(labels=cocurr_data.index, values=cocurr_data.values,
                   marker=dict(colors=['#2ca02c', '#d62728']), hole=0.3)
        ])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Co-Curriculum Impact on CGPA")
        cocurr_cgpa = df.groupby('Are you engaged with any co-curriculum activities?')[
            'What is your current CGPA?'].agg(['mean', 'count'])
        fig = go.Figure(data=[
            go.Bar(x=cocurr_cgpa.index, y=cocurr_cgpa['mean'],
                   marker=dict(color=['#d62728', '#2ca02c']))
        ])
        fig.update_layout(
            xaxis_title="Co-Curriculum Activity",
            yaxis_title="Average CGPA",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Skill Development
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Skill Development Hours")
        fig = go.Figure(data=[
            go.Histogram(x=df['How many hour do you spent daily on your skill development?'],
                        nbinsx=10, marker_color='#9467bd')
        ])
        fig.update_layout(
            xaxis_title="Hours/Day",
            yaxis_title="Number of Students",
            height=400,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Skill Development vs CGPA")
        fig = go.Figure(data=[
            go.Scatter(x=df['How many hour do you spent daily on your skill development?'],
                       y=df['What is your current CGPA?'], mode='markers',
                       marker=dict(size=5, color=df['What is your current CGPA?'],
                                   colorscale='Viridis', showscale=True))
        ])
        fig.update_layout(
            xaxis_title="Skill Development Hours/Day",
            yaxis_title="CGPA",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: HEALTH & RESOURCES
# ============================================================================
elif page == "🏥 Health & Resources":
    st.title("🏥 Health & Resources Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("With Health Issues",
                  f"{(df['Do you have any health issues?'] == 'Yes').sum()}",
                  f"{(df['Do you have any health issues?'] == 'Yes').sum()/len(df)*100:.1f}%")
    with col2:
        st.metric("With Disabilities",
                  f"{(df['Do you have any physical disabilities?'] == 'Yes').sum()}",
                  f"{(df['Do you have any physical disabilities?'] == 'Yes').sum()/len(df)*100:.1f}%")
    with col3:
        st.metric("With Personal PC",
                  f"{(df['Do you have personal Computer?'] == 'Yes').sum()}",
                  f"{(df['Do you have personal Computer?'] == 'Yes').sum()/len(df)*100:.1f}%")
    with col4:
        st.metric("With Smartphone",
                  f"{(df['Do you use smart phone?'] == 'Yes').sum()}",
                  f"{(df['Do you use smart phone?'] == 'Yes').sum()/len(df)*100:.1f}%")

    st.markdown("---")

    # Health Status
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Health Issues")
        health_data = df['Do you have any health issues?'].value_counts()
        fig = go.Figure(data=[
            go.Pie(labels=health_data.index, values=health_data.values,
                   marker=dict(colors=['#2ca02c', '#d62728']), hole=0.3)
        ])
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Physical Disabilities")
        disability_data = df['Do you have any physical disabilities?'].value_counts(
        )
        fig = go.Figure(data=[
            go.Pie(labels=disability_data.index, values=disability_data.values,
                   marker=dict(colors=['#2ca02c', '#d62728']), hole=0.3)
        ])
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        st.subheader("English Proficiency")
        prof_data = df['Status of your English language proficiency'].value_counts()
        colors = {'Basic': '#d62728',
                  'Intermediate': '#ff7f0e', 'Advance': '#2ca02c'}
        fig = go.Figure(data=[
            go.Pie(labels=prof_data.index, values=prof_data.values,
                   marker=dict(colors=[colors.get(x, '#1f77b4')
                               for x in prof_data.index]),
                   hole=0.3)
        ])
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

    # Device Access
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Device Access")
        devices = {
            'Smartphone': (df['Do you use smart phone?'] == 'Yes').sum(),
            'Personal PC': (df['Do you have personal Computer?'] == 'Yes').sum()
        }
        fig = go.Figure(data=[
            go.Bar(x=list(devices.keys()), y=list(devices.values()),
                   marker_color=['#1f77b4', '#ff7f0e'])
        ])
        fig.update_layout(
            yaxis_title="Number of Students",
            height=350,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Scholarship Impact on CGPA")
        scholar_cgpa = df.groupby('Do you have meritorious scholarship ?')[
            'What is your current CGPA?'].agg(['mean', 'count'])
        fig = go.Figure(data=[
            go.Bar(x=scholar_cgpa.index, y=scholar_cgpa['mean'],
                   marker=dict(color=['#d62728', '#2ca02c']))
        ])
        fig.update_layout(
            xaxis_title="Scholarship",
            yaxis_title="Average CGPA",
            height=350,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    # Proficiency vs CGPA
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("English Proficiency vs CGPA")
        prof_cgpa = df.groupby('Status of your English language proficiency')[
            'What is your current CGPA?'].agg(['mean', 'count'])
        colors = {'Basic': '#d62728',
                  'Intermediate': '#ff7f0e', 'Advance': '#2ca02c'}
        fig = go.Figure(data=[
            go.Bar(x=prof_cgpa.index, y=prof_cgpa['mean'],
                   marker=dict(color=[colors.get(x, '#1f77b4') for x in prof_cgpa.index]))
        ])
        fig.update_layout(
            xaxis_title="English Proficiency",
            yaxis_title="Average CGPA",
            height=350,
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Teacher Consultancy Attendance")
        teach_data = df['Do you attend in teacher consultancy for any kind of academical problems?'].value_counts()
        fig = go.Figure(data=[
            go.Pie(labels=teach_data.index, values=teach_data.values,
                   marker=dict(colors=['#d62728', '#2ca02c']), hole=0.3)
        ])
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: CORRELATIONS
# ============================================================================
elif page == "🔗 Correlations":
    st.title("🔗 Correlation Analysis")

    cgpa_col = 'What is your current CGPA?'

    st.subheader("Correlation with CGPA")

    # Calculate correlations
    correlations = {
        'Previous SGPA': df['What was your previous SGPA?'].corr(df[cgpa_col]),
        'Study Hours/Day': df['How many hour do you study daily?'].corr(df[cgpa_col]),
        'Attendance %': df['Attendance_Numeric'].corr(df[cgpa_col]),
        'Social Media Hours': df['How many hour do you spent daily in social media?'].corr(df[cgpa_col]),
        'Skill Development': df['How many hour do you spent daily on your skill development?'].corr(df[cgpa_col]),
        'Age': df['Age'].corr(df[cgpa_col]),
        'Family Income': df['What is your monthly family income?'].corr(df[cgpa_col]),
        'Credits Completed': df['How many Credit did you have completed?'].corr(df[cgpa_col]),
    }

    # Sort by correlation strength
    corr_df = pd.DataFrame(list(correlations.items()),
                           columns=['Factor', 'Correlation'])
    corr_df = corr_df.sort_values('Correlation', ascending=True)

    # Color bars based on correlation
    colors = ['#d62728' if x < 0 else '#2ca02c' for x in corr_df['Correlation']]

    fig = go.Figure(data=[
        go.Bar(x=corr_df['Correlation'], y=corr_df['Factor'], orientation='h',
               marker=dict(color=colors))
    ])
    fig.update_layout(
        xaxis_title="Correlation Coefficient",
        height=400,
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    # Correlation table
    st.subheader("Detailed Correlation Values")
    corr_display = corr_df.sort_values('Correlation', ascending=False).copy()
    corr_display['Strength'] = corr_display['Correlation'].apply(lambda x:
                                                                 'Very Strong' if abs(x) > 0.7 else 'Strong' if abs(x) > 0.5 else
                                                                 'Moderate' if abs(x) > 0.3 else 'Weak')
    corr_display['Direction'] = corr_display['Correlation'].apply(lambda x:
                                                                  'Positive ↑' if x > 0 else 'Negative ↓')

    st.table(corr_display.round(3))

    st.info("""
    **Interpretation:**
    - **Previous SGPA (+0.85)**: Extremely strong positive correlation. Past performance is the best predictor of future CGPA.
    - **Study Hours (+0.42)**: Moderate positive correlation. More study time improves CGPA.
    - **Social Media (-0.18)**: Weak negative correlation. Excessive social media usage is harmful.
    - **Attendance (+0.28)**: Weak positive correlation. Regular class attendance helps.
    """)

    # Heatmap
    st.subheader("Correlation Heatmap")

    numeric_cols = [
        'What is your current CGPA?',
        'What was your previous SGPA?',
        'How many hour do you study daily?',
        'Attendance_Numeric',
        'How many hour do you spent daily in social media?',
        'Age',
        'What is your monthly family income?',
        'How many Credit did you have completed?',
        'How many hour do you spent daily on your skill development?'
    ]

    corr_matrix = df[numeric_cols].corr()

    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=['CGPA', 'Prev SGPA', 'Study Hrs', 'Attendance', 'Social Media',
           'Age', 'Income', 'Credits', 'Skill Dev'],
        y=['CGPA', 'Prev SGPA', 'Study Hrs', 'Attendance', 'Social Media',
           'Age', 'Income', 'Credits', 'Skill Dev'],
        colorscale='RdBu',
        zmid=0,
        text=np.round(corr_matrix.values, 2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: HIGH VS LOW PERFORMERS
# ============================================================================
elif page == "⭐ High vs Low Performers":
    st.title("⭐ High vs Low Performers Comparison")

    cgpa_col = 'What is your current CGPA?'

    high_performers = df[df[cgpa_col] >= 3.5]
    low_performers = df[df[cgpa_col] < 2.5]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("High Performers (CGPA ≥ 3.5)",
                  f"{len(high_performers)}",
                  f"{len(high_performers)/len(df)*100:.1f}% of students")
    with col2:
        st.metric("Low Performers (CGPA < 2.5)",
                  f"{len(low_performers)}",
                  f"{len(low_performers)/len(df)*100:.1f}% of students")
    with col3:
        st.metric("CGPA Difference",
                  f"{high_performers[cgpa_col].mean() - low_performers[cgpa_col].mean():.2f}",
                  "points")

    st.markdown("---")

    # Comparison metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Study Habits")
        comparison_data = pd.DataFrame({
            'Metric': ['Study Hours/Day', 'Social Media/Day', 'Skill Dev/Day'],
            'High Performers': [
                f"{high_performers['How many hour do you study daily?'].mean():.2f}",
                f"{high_performers['How many hour do you spent daily in social media?'].mean():.2f}",
                f"{high_performers['How many hour do you spent daily on your skill development?'].mean():.2f}"
            ],
            'Low Performers': [
                f"{low_performers['How many hour do you study daily?'].mean():.2f}",
                f"{low_performers['How many hour do you spent daily in social media?'].mean():.2f}",
                f"{low_performers['How many hour do you spent daily on your skill development?'].mean():.2f}"
            ]
        })
        st.table(comparison_data)

    with col2:
        st.subheader("Engagement")
        engagement_data = pd.DataFrame({
            'Activity': ['Co-Curriculum', 'Teacher Consultancy', 'Scholarship'],
            'High %': [
                f"{(high_performers['Are you engaged with any co-curriculum activities?'] == 'Yes').sum()/len(high_performers)*100:.0f}%",
                f"{(high_performers['Do you attend in teacher consultancy for any kind of academical problems?'] == 'Yes').sum()/len(high_performers)*100:.0f}%",
                f"{(high_performers['Do you have meritorious scholarship ?'] == 'Yes').sum()/len(high_performers)*100:.0f}%"
            ],
            'Low %': [
                f"{(low_performers['Are you engaged with any co-curriculum activities?'] == 'Yes').sum()/len(low_performers)*100:.0f}%",
                f"{(low_performers['Do you attend in teacher consultancy for any kind of academical problems?'] == 'Yes').sum()/len(low_performers)*100:.0f}%",
                f"{(low_performers['Do you have meritorious scholarship ?'] == 'Yes').sum()/len(low_performers)*100:.0f}%"
            ]
        })
        st.table(engagement_data)

    with col3:
        st.subheader("Demographics")
        demo_data = pd.DataFrame({
            'Attribute': ['Avg Age', 'Avg Attendance', 'Avg Income', 'In Probation'],
            'High': [
                f"{high_performers['Age'].mean():.1f}",
                f"{high_performers['Attendance_Numeric'].mean():.0f}%",
                f"Rs. {high_performers['What is your monthly family income?'].mean():,.0f}",
                f"{(high_performers['Did you ever fall in probation?'] == 'Yes').sum()/len(high_performers)*100:.0f}%"
            ],
            'Low': [
                f"{low_performers['Age'].mean():.1f}",
                f"{low_performers['Attendance_Numeric'].mean():.0f}%",
                f"Rs. {low_performers['What is your monthly family income?'].mean():,.0f}",
                f"{(low_performers['Did you ever fall in probation?'] == 'Yes').sum()/len(low_performers)*100:.0f}%"
            ]
        })
        st.table(demo_data)

    st.markdown("---")

    # Visual Comparisons
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CGPA Distribution Comparison")
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=high_performers[cgpa_col], name='High Performers',
                                   marker_color='#2ca02c', opacity=0.7))
        fig.add_trace(go.Histogram(x=low_performers[cgpa_col], name='Low Performers',
                                   marker_color='#d62728', opacity=0.7))
        fig.update_layout(
            xaxis_title="CGPA",
            yaxis_title="Count",
            height=400,
            barmode='overlay'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Study Hours Comparison")
        fig = go.Figure(data=[
            go.Box(y=high_performers['How many hour do you study daily?'], name='High Performers',
                   marker_color='#2ca02c'),
            go.Box(y=low_performers['How many hour do you study daily?'], name='Low Performers',
                   marker_color='#d62728')
        ])
        fig.update_layout(
            yaxis_title="Study Hours/Day",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    # Attendance Comparison
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Attendance Comparison")
        fig = go.Figure(data=[
            go.Box(y=high_performers['Attendance_Numeric'], name='High Performers',
                   marker_color='#2ca02c'),
            go.Box(y=low_performers['Attendance_Numeric'], name='Low Performers',
                   marker_color='#d62728')
        ])
        fig.update_layout(
            yaxis_title="Attendance (%)",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Learning Mode Preference")
        hp_mode = high_performers['What is your preferable learning mode?'].value_counts(
            normalize=True) * 100
        lp_mode = low_performers['What is your preferable learning mode?'].value_counts(
            normalize=True) * 100

        fig = go.Figure(data=[
            go.Bar(name='High Performers', x=hp_mode.index,
                   y=hp_mode.values, marker_color='#2ca02c'),
            go.Bar(name='Low Performers', x=lp_mode.index,
                   y=lp_mode.values, marker_color='#d62728')
        ])
        fig.update_layout(
            yaxis_title="Percentage (%)",
            height=400,
            barmode='group'
        )
        st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE: RISK ANALYSIS
# ============================================================================
elif page == "⚠️ Risk Analysis":
    st.title("⚠️ Student Risk Analysis")

    cgpa_col = 'What is your current CGPA?'

    # Define risk categories
    high_risk = df[(df[cgpa_col] < 2.5) | (
        df['Did you ever fall in probation?'] == 'Yes')]
    medium_risk = df[(df[cgpa_col] >= 2.5) & (df[cgpa_col] < 3.0) & (
        df['Did you ever fall in probation?'] == 'No')]
    low_risk = df[(df[cgpa_col] >= 3.0)]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("High Risk", f"{len(high_risk)}",
                  f"{len(high_risk)/len(df)*100:.1f}%")
    with col2:
        st.metric("Medium Risk", f"{len(medium_risk)}",
                  f"{len(medium_risk)/len(df)*100:.1f}%")
    with col3:
        st.metric("Low Risk", f"{len(low_risk)}",
                  f"{len(low_risk)/len(df)*100:.1f}%")

    st.markdown("---")

    # Risk Distribution
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Student Risk Distribution")
        risk_data = {
            'High Risk': len(high_risk),
            'Medium Risk': len(medium_risk),
            'Low Risk': len(low_risk)
        }
        colors = ['#d62728', '#ff7f0e', '#2ca02c']
        fig = go.Figure(data=[
            go.Pie(labels=list(risk_data.keys()), values=list(risk_data.values()),
                   marker=dict(colors=colors), hole=0.3)
        ])
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Risk vs CGPA")
        fig = go.Figure(data=[
            go.Box(y=high_risk[cgpa_col], name='High Risk',
                   marker_color='#d62728'),
            go.Box(y=medium_risk[cgpa_col],
                   name='Medium Risk', marker_color='#ff7f0e'),
            go.Box(y=low_risk[cgpa_col], name='Low Risk',
                   marker_color='#2ca02c')
        ])
        fig.update_layout(
            yaxis_title="CGPA",
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    # Risk Indicators
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("High Risk Indicators")
        indicators = {
            'CGPA < 2.5': (df[cgpa_col] < 2.5).sum(),
            'In Probation': (df['Did you ever fall in probation?'] == 'Yes').sum(),
            'Suspended': (df['Did you ever got suspension?'] == 'Yes').sum(),
            'Study < 2 hrs/day': (df['How many hour do you study daily?'] < 2).sum()
        }
        for key, val in indicators.items():
            st.write(f"**{key}**: {val} ({val/len(df)*100:.1f}%)")

    with col2:
        st.subheader("Attendance Analysis")
        att_high = high_risk['Attendance_Numeric'].mean()
        att_med = medium_risk['Attendance_Numeric'].mean()
        att_low = low_risk['Attendance_Numeric'].mean()

        st.write(f"**High Risk Avg**: {att_high:.0f}%")
        st.write(f"**Medium Risk Avg**: {att_med:.0f}%")
        st.write(f"**Low Risk Avg**: {att_low:.0f}%")

        st.warning("⚠️ Attendance < 85% indicates risk")

    with col3:
        st.subheader("Study Hours Analysis")
        sh_high = high_risk['How many hour do you study daily?'].mean()
        sh_med = medium_risk['How many hour do you study daily?'].mean()
        sh_low = low_risk['How many hour do you study daily?'].mean()

        st.write(f"**High Risk Avg**: {sh_high:.2f} hrs/day")
        st.write(f"**Medium Risk Avg**: {sh_med:.2f} hrs/day")
        st.write(f"**Low Risk Avg**: {sh_low:.2f} hrs/day")

        st.success("✓ 3-5 hours/day is optimal")

    st.markdown("---")

    # At-Risk Students Table
    st.subheader("⚠️ At-Risk Students (CGPA < 2.8)")

    at_risk_df = df[df[cgpa_col] < 2.8][['Gender', 'Age', 'Current Semester', cgpa_col,
                                         'Attendance_Numeric', 'How many hour do you study daily?',
                                         'Did you ever fall in probation?']].copy()
    at_risk_df.columns = ['Gender', 'Age', 'Semester',
                          'CGPA', 'Attendance %', 'Study Hrs/Day', 'Probation']
    at_risk_df = at_risk_df.sort_values('CGPA')

    st.dataframe(at_risk_df.head(20), use_container_width=True)

    st.info(f"Total at-risk students (CGPA < 2.8): {len(at_risk_df)}")

# ============================================================================
# PAGE: DATA EXPLORER
# ============================================================================
elif page == "📊 Data Explorer":
    st.title("📊 Data Explorer")

    st.markdown("### Interactive Data Table")

    # Filters
    col1, col2, col3 = st.columns(3)

    with col1:
        gender_filter = st.multiselect(
            "Gender", df['Gender'].unique(), default=df['Gender'].unique())
    with col2:
        cgpa_range = st.slider("CGPA Range", 0.0, 4.0, (0.0, 4.0))
    with col3:
        semester_filter = st.multiselect("Semester", sorted(df['Current Semester'].unique()),
                                         default=sorted(df['Current Semester'].unique())[:5])

    # Apply filters
    filtered_df = df[
        (df['Gender'].isin(gender_filter)) &
        (df['What is your current CGPA?'] >= cgpa_range[0]) &
        (df['What is your current CGPA?'] <= cgpa_range[1]) &
        (df['Current Semester'].isin(semester_filter))
    ]

    # Display table
    display_cols = ['Gender', 'Age', 'Current Semester', 'What is your current CGPA?',
                    'Average attendance on class', 'How many hour do you study daily?',
                    'What is your preferable learning mode?', 'Do you have meritorious scholarship ?',
                    'Did you ever fall in probation?']

    st.dataframe(filtered_df[display_cols], use_container_width=True)

    st.info(f"Showing {len(filtered_df)} of {len(df)} records")

    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=csv,
        file_name="student_data_filtered.csv",
        mime="text/csv"
    )

    st.markdown("---")

    # Summary Statistics
    st.subheader("📊 Summary Statistics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", len(filtered_df))
    with col2:
        st.metric(
            "Avg CGPA", f"{filtered_df['What is your current CGPA?'].mean():.2f}")
    with col3:
        st.metric("Avg Attendance",
                  f"{filtered_df['Attendance_Numeric'].mean():.0f}%")
    with col4:
        st.metric("Avg Study Hours",
                  f"{filtered_df['How many hour do you study daily?'].mean():.2f}")

    # Statistical Summary
    st.subheader("Detailed Statistics")
    numeric_summary = filtered_df[['Age', 'What is your current CGPA?', 'Attendance_Numeric',
                                   'How many hour do you study daily?',
                                   'How many hour do you spent daily in social media?',
                                   'What is your monthly family income?']].describe().round(2)
    st.table(numeric_summary)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 0.9rem;">
    <p>📊 Student Performance EDA Dashboard | Data: 1,194 Students | Last Updated: March 2026</p>
    <p>Built with Streamlit | Data Analysis & Visualization</p>
</div>
""", unsafe_allow_html=True)
