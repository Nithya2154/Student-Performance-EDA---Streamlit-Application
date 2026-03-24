# 📊 Student Performance EDA - Complete Interactive Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red?style=flat-square&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.1%2B-green?style=flat-square&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-5.17%2B-purple?style=flat-square&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=flat-square)

**Comprehensive exploratory data analysis of 1,194 students with 40+ interactive visualizations**

[Quick Start](#-quick-start) • [Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation) • [Support](#-support)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Documentation](#-documentation)
- [Key Insights](#-key-insights)
- [Dashboard Pages](#-dashboard-pages)
- [Data Dictionary](#-data-dictionary)
- [Technologies](#-technologies)
- [Implementation Paths](#-implementation-paths)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Support](#-support)

---

## Overview

This project provides a **complete Exploratory Data Analysis (EDA)** of student performance data covering 1,194 students across multiple dimensions including:

- 📍 **Demographics** - Age, gender, income, admission cohorts
- 🎓 **Academic Performance** - CGPA, attendance, probation status
- 📚 **Study Habits** - Daily study hours, learning modes, social media usage
- 🎯 **Skills & Interests** - Top skills, career interests, engagement
- 🏥 **Health & Resources** - Health issues, device access, scholarships
- 🔗 **Statistical Analysis** - Correlations, risk factors, predictive insights

The project includes:
- ✅ **Interactive Streamlit Application** with 10 dashboards
- ✅ **40+ Professional Visualizations** using Plotly
- ✅ **1,200+ Lines of Production Code** fully documented
- ✅ **8 Comprehensive Guides** for analysis and implementation
- ✅ **Pre-processed Data** (1,194 records × 35 attributes)
- ✅ **100+ Data Insights** with actionable recommendations

---

## 🎯 Features

### 🎨 10 Interactive Dashboard Pages

| # | Dashboard | Description |
|---|-----------|-------------|
| **1** | 🏠 Home | Project overview, key statistics, navigation |
| **2** | 📍 Demographics | Gender, age, income, admission year distributions |
| **3** | 🎓 Academic | CGPA analysis, attendance impact, probation status |
| **4** | 📚 Study Habits | Study hours, social media, learning modes |
| **5** | 🎯 Skills | Top skills, career interests, co-curriculum |
| **6** | 🏥 Health | Health issues, resources, English proficiency |
| **7** | 🔗 Correlations | CGPA predictors, correlation heatmap |
| **8** | ⭐ Performers | High vs low performer comparisons |
| **9** | ⚠️ Risk Analysis | At-risk identification, interventions |
| **10** | 📊 Data Explorer | Interactive table, filtering, CSV export |

### 📊 40+ Visualizations

- ✅ Scatter plots with trend lines
- ✅ Correlation heatmaps
- ✅ Distribution histograms
- ✅ Box plots & comparisons
- ✅ Bar & column charts
- ✅ Pie & donut charts
- ✅ Line charts with trends
- ✅ Time-series analysis

### 🔧 Interactive Features

- ✅ **Real-time Filtering** - Instant data updates with sliders & dropdowns
- ✅ **Data Export** - Download filtered data as CSV
- ✅ **Hover Details** - Detailed information on chart hover
- ✅ **Multi-select** - Filter by multiple criteria simultaneously
- ✅ **Responsive Design** - Works on desktop, tablet, mobile
- ✅ **Performance Optimized** - `@st.cache_data` for speed

### 📈 Advanced Analytics

- ✅ **Statistical Correlations** - CGPA predictors ranked
- ✅ **Risk Assessment** - Student risk categorization
- ✅ **Performance Segmentation** - High/Medium/Low performers
- ✅ **Comparative Analysis** - Gender, learning mode, demographics
- ✅ **Trend Analysis** - Admission year cohorts
- ✅ **Summary Statistics** - Automatic calculations

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- 2GB RAM minimum
- 500MB free disk space

### Installation (2 minutes)

```bash
# 1. Clone or download project files
cd student-performance-eda

# 2. Install dependencies (one command)
pip install -r requirements.txt

# 3. Run the application
streamlit run streamlit_eda_app.py
```

### Launch (Automatic)

The browser should automatically open to `http://localhost:8501`

If not, manually visit: **http://localhost:8501**

---

## 📥 Installation

### Step 1: Install Python

**Windows/Mac/Linux:**
- Download from [python.org](https://www.python.org/downloads/) (version 3.8+)
- Add Python to PATH during installation

### Step 2: Verify Installation

```bash
python --version
pip --version
```

### Step 3: Install Dependencies

**Option A: One-command installation**

```bash
pip install -r requirements.txt
```

**Option B: Manual installation**

```bash
pip install streamlit==1.28.1
pip install pandas==2.1.3
pip install numpy==1.24.3
pip install plotly==5.17.0
pip install seaborn==0.13.0
pip install matplotlib==3.8.2
pip install scipy==1.11.4
```

### Step 4: Verify Installation

```bash
python -c "import streamlit; print(streamlit.__version__)"
```

### Step 5: Prepare Files

1. Download all files from the project
2. Keep them in the same folder
3. Ensure `Students_Performance_Processed.csv` is in the same directory as `streamlit_eda_app.py`

```
project-folder/
├── streamlit_eda_app.py
├── Students_Performance_Processed.csv
├── requirements.txt
└── [other documentation files]
```

---

## 🎮 Usage

### Running the Application

```bash
# Basic run
streamlit run streamlit_eda_app.py

# Run on specific port
streamlit run streamlit_eda_app.py --server.port 8502

# Run with debug logging
streamlit run streamlit_eda_app.py --logger.level=debug

# Run in wide mode
streamlit run streamlit_eda_app.py --layout=wide
```

### Navigating the Dashboard

1. **Sidebar Navigation** - Select dashboard from left sidebar
2. **Quick Stats** - View key metrics in sidebar
3. **Filters** - Use sliders, dropdowns, multi-select for filtering
4. **Hover Details** - Hover over charts for detailed information
5. **Export Data** - Download filtered data in Data Explorer
6. **Full Screen** - Click expand icon on charts

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `R` | Rerun app |
| `C` | Clear cache |
| `H` | Toggle sidebar |
| `Ctrl+C` | Stop app |

### Common Tasks

**Explore Performance by Gender**
1. Navigate to Academic Performance page
2. View "CGPA by Gender" chart
3. Use sidebar filters if needed

**Find At-Risk Students**
1. Go to Risk Analysis page
2. View "At-Risk Students" table
3. Filter by criteria
4. Export data as CSV

**Compare Study Habits**
1. Open Study Habits page
2. Compare "Study Hours vs CGPA" scatter plot
3. Overlay learning mode colors
4. Check trend line direction

**Export Filtered Data**
1. Go to Data Explorer
2. Apply filters (Gender, CGPA, Semester, etc.)
3. Click "Download Filtered Data as CSV"
4. Use in Excel, Python, or BI tool

---

## 📁 Project Structure

```
student-performance-eda/
│
├── 📄 README.md (this file)
├── 📄 00_START_HERE.md
├── 📄 STREAMLIT_QUICK_START.md
├── 📄 STREAMLIT_README.md
├── 📄 FILE_MANIFEST.txt
│
├── 🐍 streamlit_eda_app.py (MAIN APPLICATION - 1,200 lines)
│   ├── Home dashboard
│   ├── Demographics page
│   ├── Academic performance page
│   ├── Study habits page
│   ├── Skills & interests page
│   ├── Health & resources page
│   ├── Correlations page
│   ├── High vs low performers page
│   ├── Risk analysis page
│   └── Data explorer page
│
├── 📊 Students_Performance_Processed.csv
│   ├── 1,194 student records
│   ├── 35 attributes
│   └── Ready to use (pre-processed)
│
├── 📋 requirements.txt (dependencies)
│
├── 📚 Documentation/
│   ├── EDA_Project_Guide.md
│   ├── EDA_QUICK_START_SUMMARY.md
│   ├── Power_BI_Setup_Guide.md
│   ├── IMPLEMENTATION_CHECKLIST.md
│   └── [other guides]
│
└── 📌 Additional Files/
    └── [configuration, docs, examples]
```

---

## 📚 Documentation

### Quick References

| Document | Purpose | Time |
|----------|---------|------|
| **00_START_HERE.md** | Project overview & paths | 5 min |
| **STREAMLIT_QUICK_START.md** | App setup guide | 5 min |
| **STREAMLIT_README.md** | Full app documentation | 15 min |
| **EDA_QUICK_START_SUMMARY.md** | Key insights | 20 min |
| **EDA_Project_Guide.md** | Analysis framework | 30 min |
| **Power_BI_Setup_Guide.md** | Power BI implementation | Reference |
| **IMPLEMENTATION_CHECKLIST.md** | 12-phase project plan | Reference |
| **FILE_MANIFEST.txt** | File inventory | 10 min |

### Reading Order

1. **Start:** README.md (you are here)
2. **Setup:** STREAMLIT_QUICK_START.md
3. **Run:** `streamlit run streamlit_eda_app.py`
4. **Explore:** 10 dashboard pages
5. **Understand:** EDA_QUICK_START_SUMMARY.md
6. **Reference:** Other documentation as needed

---

## 🔑 Key Insights

### Strongest CGPA Predictors

| Rank | Factor | Correlation | Strength |
|------|--------|-------------|----------|
| **1** | Previous SGPA | +0.85 | ⭐⭐⭐⭐⭐ Very Strong |
| **2** | Study Hours/Day | +0.42 | ⭐⭐⭐ Moderate |
| **3** | Family Income | +0.28 | ⭐⭐ Weak |
| **4** | Skill Development | +0.12 | ⭐ Weak |
| **5** | Social Media Hours | -0.18 | ⭐ Weak (Negative) |

### Key Statistics

| Metric | Value |
|--------|-------|
| **Total Students** | 1,194 |
| **Average CGPA** | 3.17 / 4.00 |
| **High Performers (≥3.5)** | 438 (36.7%) |
| **Low Performers (<2.5)** | 91 (7.6%) |
| **In Academic Probation** | 298 (25.0%) |
| **Suspended** | 46 (3.9%) |
| **Male : Female Ratio** | 56% : 44% |
| **Average Age** | 21.3 years |
| **Average Study Hours/Day** | 3.13 hours |
| **Average Social Media/Day** | 3.29 hours |
| **With Scholarship** | 523 (43.8%) |
| **Co-Curriculum Active** | 505 (42.3%) |
| **Data Quality** | 99.9% complete |

### Performance Categories

```
Excellent (≥3.75):        238 students (19.9%) 🌟
Very Good (3.5-3.74):     200 students (16.8%) ⭐
Good (3.0-3.49):          406 students (34.0%) ✓
Satisfactory (2.5-2.99):  259 students (21.7%) ~
Below Average (<2.5):      91 students (7.6%)  ✗
```

### Success Characteristics (High Performers)

✅ Daily study: 3.5+ hours  
✅ Social media: <2 hours/day  
✅ Attendance: 95%+  
✅ Scholarship: 50%+  
✅ Co-curriculum: 55%+  
✅ Teacher consultancy: 70%+  
✅ Offline learning: 75%  

### Risk Indicators

❌ CGPA < 2.5  
❌ In academic probation  
❌ Study hours < 2/day  
❌ Attendance < 85%  
❌ Social media > 4 hours/day  
❌ No teacher consultancy  

---

## 📊 Dashboard Pages

### 1. 🏠 Home Dashboard
- **Purpose:** Project overview and navigation
- **Contains:** Key statistics, quick insights, page navigation
- **Best For:** First-time users, stakeholder briefings

### 2. 📍 Demographics
- **Purpose:** Understand student population characteristics
- **Contains:** Gender, age, income, admission year distributions
- **Best For:** Understanding sample composition

### 3. 🎓 Academic Performance
- **Purpose:** Analyze academic outcomes and factors
- **Contains:** CGPA distribution, attendance impact, probation status
- **Best For:** Understanding academic health

### 4. 📚 Study Habits
- **Purpose:** Explore study patterns and their impact
- **Contains:** Study hours, social media usage, learning modes
- **Best For:** Identifying behavioral patterns

### 5. 🎯 Skills & Interests
- **Purpose:** Understand skills and career interests
- **Contains:** Top skills, interests, co-curriculum impact
- **Best For:** Career planning insights

### 6. 🏥 Health & Resources
- **Purpose:** Assess resources and support systems
- **Contains:** Health issues, device access, scholarship impact
- **Best For:** Understanding student support needs

### 7. 🔗 Correlations
- **Purpose:** Identify CGPA predictors
- **Contains:** Correlation rankings, heatmap, interpretations
- **Best For:** Statistical understanding

### 8. ⭐ High vs Low Performers
- **Purpose:** Compare successful vs struggling students
- **Contains:** Detailed comparisons, characteristics, differences
- **Best For:** Identifying success factors

### 9. ⚠️ Risk Analysis
- **Purpose:** Identify and support at-risk students
- **Contains:** Risk categorization, warning indicators, at-risk table
- **Best For:** Intervention planning

### 10. 📊 Data Explorer
- **Purpose:** Deep dive into individual records
- **Contains:** Interactive table, advanced filters, CSV export
- **Best For:** Custom analysis and data export

---

## 📖 Data Dictionary

### Key Columns

| Column | Description | Type | Range |
|--------|-------------|------|-------|
| **What is your current CGPA?** | Current GPA | Numeric | 0.00 - 4.00 |
| **What was your previous SGPA?** | Previous semester GPA | Numeric | 0.00 - 4.00 |
| **Gender** | Student gender | Text | Male, Female |
| **Age** | Student age | Numeric | 18 - 27 |
| **How many hour do you study daily?** | Daily study commitment | Numeric | 0 - 13 hours |
| **Average attendance on class** | Class attendance percentage | Numeric | 0 - 100% |
| **How many hour do you spent daily in social media?** | Social media usage | Numeric | 0 - 20 hours |
| **What is your preferable learning mode?** | Learning preference | Text | Online, Offline |
| **Do you have meritorious scholarship ?** | Scholarship status | Yes/No | Yes, No |
| **Did you ever fall in probation?** | Probation history | Yes/No | Yes, No |
| **Are you engaged with any co-curriculum activities?** | Co-curriculum engagement | Yes/No | Yes, No |
| **What is your monthly family income?** | Monthly family income | Numeric | Rs. 4,000 - 2,000,000 |
| **Current Semester** | Semester number | Numeric | 1 - 24 |
| **Do you have personal Computer?** | PC access | Yes/No | Yes, No |
| **Do you use smart phone?** | Smartphone access | Yes/No | Yes, No |

### Calculated Columns

| Column | Calculation | Purpose |
|--------|-------------|---------|
| **CGPA_Category** | Binned CGPA | Performance classification |
| **Study_Level** | Binned study hours | Study commitment classification |
| **Age_Group** | Age ranges | Age grouping |
| **Income_Range** | Income brackets | Income classification |
| **Performance_Segment** | CGPA-based | Segmentation (High/Med/Low) |

### Data Quality

- **Total Records:** 1,194 students
- **Missing Values:** <1% (minimal)
- **Duplicates:** 0
- **Data Completeness:** 99.9%
- **Preprocessing:** Already done
- **Ready to Use:** Yes

---

## 💻 Technologies

### Backend
- **Python 3.8+** - Programming language
- **Streamlit 1.28+** - Web app framework
- **Pandas 2.1+** - Data manipulation
- **NumPy 1.24+** - Numerical computing

### Visualization
- **Plotly 5.17+** - Interactive charts
- **Seaborn 0.13+** - Statistical graphics
- **Matplotlib 3.8+** - Plotting library

### Data Science
- **SciPy 1.11+** - Statistical functions
- **Scikit-learn 1.3+** - Machine learning (ready)

### Environment
- **OS:** Windows, macOS, Linux
- **Browser:** Chrome, Firefox, Safari, Edge
- **RAM:** 2GB minimum
- **Disk:** 500MB

---

## 🛣️ Implementation Paths

### Path 1: Quick Streamlit App (⚡ 5 minutes)

**Goal:** Immediate interactive dashboard

**Steps:**
1. Read: `STREAMLIT_QUICK_START.md`
2. Install: `pip install -r requirements.txt`
3. Run: `streamlit run streamlit_eda_app.py`
4. Explore: 10 dashboards in browser

**Output:** Working web dashboard

**Best For:** Quick exploration, presentations

---

### Path 2: Professional Power BI (📊 7-13 hours)

**Goal:** Enterprise-grade dashboards

**Steps:**
1. Read: `IMPLEMENTATION_CHECKLIST.md`
2. Reference: `Power_BI_Setup_Guide.md`
3. Build: 7 dashboards (12-phase plan)
4. Test: Validate with checklist

**Output:** 7 professional Power BI dashboards

**Best For:** Institutions, long-term reporting

---

### Path 3: Custom Python Analysis (🔬 Flexible)

**Goal:** Custom analysis using Python

**Steps:**
1. Load: CSV file in your tool
2. Explore: Use provided examples
3. Analyze: Create custom analysis
4. Visualize: Build custom visualizations

**Output:** Custom insights

**Best For:** Research, advanced analytics

---

## 🆘 Troubleshooting

### Installation Issues

**Error: "Python not found"**
```bash
# Solution: Verify Python installation
python --version

# If not found, reinstall from python.org
```

**Error: "Module not found"**
```bash
# Solution: Reinstall dependencies
pip install --upgrade streamlit pandas plotly
```

**Error: "Port already in use"**
```bash
# Solution: Use different port
streamlit run streamlit_eda_app.py --server.port 8502
```

### Runtime Issues

**Error: "Data file not found"**
```
Solution: Ensure Students_Performance_Processed.csv is in same folder
as streamlit_eda_app.py
```

**App loads slowly**
```bash
# Solution: Clear cache and restart
streamlit cache clear
streamlit run streamlit_eda_app.py
```

**Charts not displaying**
```
Solution: Try refresh (Ctrl+R or F5)
Or rerun streamlit command
```

**Memory error**
```bash
# Solution: Run on machine with 4GB+ RAM
# Or restart the app
```

### Browser Issues

**Browser doesn't open automatically**
```
Manual solution: Open http://localhost:8501 in browser
```

**Charts appear broken**
```
Solution: Try different browser
Clear cache (Ctrl+Shift+Delete)
Restart streamlit app
```

---

## 🤝 Contributing

### Report Issues
If you find bugs or issues:
1. Note the exact error message
2. List steps to reproduce
3. Check troubleshooting section
4. Include Python version and OS

### Suggestions
Have ideas to improve? Consider:
- Additional visualizations
- New analysis sections
- Performance improvements
- Documentation enhancements

### Code Quality
If contributing code:
- Follow PEP 8 style guide
- Add comments for clarity
- Test thoroughly
- Document changes

---

## 📄 License

This project is provided as-is for educational and analytical purposes.

---

## 📞 Support

### Getting Help

1. **Quick Issues:** Check [Troubleshooting](#-troubleshooting) section
2. **Setup Help:** Read `STREAMLIT_QUICK_START.md`
3. **Feature Questions:** See `STREAMLIT_README.md`
4. **Data Questions:** Check `EDA_QUICK_START_SUMMARY.md`
5. **Power BI:** Refer to `IMPLEMENTATION_CHECKLIST.md`

### Documentation Files

- **00_START_HERE.md** - Main entry point
- **STREAMLIT_QUICK_START.md** - Setup guide
- **STREAMLIT_README.md** - App documentation
- **EDA_QUICK_START_SUMMARY.md** - Data insights
- **EDA_Project_Guide.md** - Analysis framework
- **Power_BI_Setup_Guide.md** - BI specifications
- **IMPLEMENTATION_CHECKLIST.md** - Project plan
- **FILE_MANIFEST.txt** - File reference

### Common Questions

**Q: Can I use this with my own data?**
A: Yes! Replace CSV file and adjust column names in code.

**Q: How do I deploy this online?**
A: See "Deployment Options" in `STREAMLIT_README.md`

**Q: Can I customize the dashboards?**
A: Absolutely! Edit `streamlit_eda_app.py` and customize.

**Q: Is this production-ready?**
A: Yes! Fully tested, documented, and optimized.

**Q: What's the learning curve?**
A: No coding needed to run. Basic Python to customize.

---

## 🎓 Learning Resources

### Streamlit
- [Official Docs](https://docs.streamlit.io)
- [Gallery](https://streamlit.io/gallery)
- [Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)

### Plotly
- [Documentation](https://plotly.com/python/)
- [Examples](https://plotly.com/python/basic-charts/)

### Pandas
- [Official Docs](https://pandas.pydata.org/docs/)
- [Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html)

### Python
- [Official Site](https://www.python.org/)
- [Real Python](https://realpython.com/)

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| **Total Files** | 11 |
| **Total Size** | ~365 KB |
| **Code Lines** | 1,200+ |
| **Visualizations** | 40+ |
| **Dashboards** | 10 |
| **Student Records** | 1,194 |
| **Data Attributes** | 35 |
| **Insights** | 100+ |
| **Documentation Pages** | 8 |
| **Setup Time** | 5 minutes |
| **Python Dependencies** | 8 |
| **Data Quality** | 99.9% |

---

## ✅ Verification Checklist

Before you start, ensure:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] pip working (`pip --version`)
- [ ] All files downloaded (11 total)
- [ ] Files in same folder
- [ ] `requirements.txt` present
- [ ] CSV file included
- [ ] Enough disk space (500MB+)
- [ ] 2GB+ RAM available

---

## 🎯 Success Criteria

The app is working correctly when:

- [ ] Streamlit app opens in browser
- [ ] All 10 dashboard pages load
- [ ] Charts display correctly
- [ ] Filters work in real-time
- [ ] Data export works
- [ ] Navigation smooth
- [ ] No error messages
- [ ] Visualizations interactive
- [ ] Page switches fast
- [ ] Insights make sense

---

## 🚀 Getting Started Now

### 5-Step Launch

```bash
# 1. Navigate to project folder
cd /path/to/project

# 2. Install dependencies (one-time)
pip install -r requirements.txt

# 3. Run the application
streamlit run streamlit_eda_app.py

# 4. Wait for server to start
# Should see: "You can now view your Streamlit app in your browser"

# 5. Explore dashboards!
# Browser opens automatically to http://localhost:8501
```

### Alternative: No Command Line

1. Download all files
2. Double-click `streamlit_eda_app.py` (if configured)
3. Or use IDE (VS Code, PyCharm) to run

---

## 📈 What's Next?

### Immediate (5 minutes)
✅ Run the app
✅ Explore dashboards
✅ Check key insights

### Short-term (1 hour)
✅ Export filtered data
✅ Share dashboards
✅ Print visualizations

### Long-term (1+ weeks)
✅ Build Power BI version
✅ Customize for your needs
✅ Integrate with systems
✅ Create reports

---

## 🙏 Acknowledgments

This project was created to demonstrate:
- Comprehensive EDA techniques
- Interactive dashboard development
- Data visualization best practices
- Statistical analysis methods
- Professional documentation

---

## 📝 Version History

### v1.0 (March 24, 2026)
- ✅ Initial release
- ✅ 10 interactive dashboards
- ✅ 40+ visualizations
- ✅ Complete documentation
- ✅ Production-ready code

---

## 📢 Final Notes

**This is a complete, production-ready project.**

Everything you need is included:
- Working application
- Real data (1,194 students)
- Comprehensive documentation
- Implementation guides
- Troubleshooting help

**No additional setup needed beyond Python installation.**

---

<div align="center">

### 🎉 Ready to Explore Student Performance Data?

**[Get Started Now →](#-quick-start)**

---

**Made with ❤️ for Data Enthusiasts**

*Last Updated: March 24, 2026*  
*Status: Production Ready ✅*  
*Version: 1.0*

</div>
