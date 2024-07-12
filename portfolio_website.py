import streamlit as st  # pip install streamlit
import google.generativeai as genai  # pip install -q -U google-generativeai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

# ---------------------------------------------------------------------
col1, col2 = st.columns([2, 1])

with col1:
    # st.subheader("Hi :wave:")
    st.title("Michael Fluch")
    st.subheader("SAP Analytics Consultant | Certified Agile Leader (Blockchain & AI Enthusiast)")

with col2:
    st.image("images/michael.png", width=200)

# ---------------------------------------------------------------------
st.title(" ")

st.title("About Me")
st.write("""
As an SAP Analytics Consultant, I specialize in transforming business planning and reporting 
through SAP Business Warehouse and SAP S/4HANA Embedded Analytics. From business requirements 
and high-level architecture to hands-on ABAP, CDS, and AMDP development, I deliver comprehensive 
solutions that drive results.

Beyond my core expertise, I'm passionate about the potential of blockchain technology and 
the power of AI to drive productivity and innovation. 

A Certified Agile Leader, I thrive on leading teams to excellence, combining cutting-edge 
technology with agile methodologies to achieve outstanding outcomes.

Let's connect and explore how I can help your business achieve its analytics and technological goals!
""")

# ---------------------------------------------------------------------
st.title(" ")

st.title("Michael's AI Bot")

persona = """
        You are Michael AI bot. You help people answer questions about your self (i.e Michael)
        Answer as if you are responding. dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Michael: 

        Michael Fluch is a SAP Analytics Consultant, specializing in transforming business planning and reporting 
        through SAP Business Warehouse and SAP S/4HANA Embedded Analytics. From business requirements and high-level architecture 
        to hands-on ABAP, CDS, and AMDP development, he delivers comprehensive solutions that drive results.
        Beyond his core expertise, he is passionate about the potential of blockchain technology and the power of AI to drive productivity and innovation. 
        As a Certified Agile Leader, he thrives on leading teams to excellence, combining cutting-edge technology with agile methodologies to achieve outstanding outcomes.
        He is working in the industry for more than 20 years.
        Michael obtained his Masters’s degree at the university of applied science in Wiener Neustadt, Austria.
        He studied electronics & communication technology, industrial engineering, project management.
        He also has good knowledge in the areas of blockchain, web2 and web3 development, and is looking at how AI technology can be used to drive productivity and innovation. 
        Prior to starting his professional career, he has travelled the world as a development worker.
        His hobbies are his family, sports of all kinds, enjoying natural treasures and discovering new worlds. 

        Michael's Youtube Channel: www.youtube.com/@zpartner3801
        Michael's Email: michael.fluch@zpartner.eu 
        Michael's Facebook: https://www.facebook.com/zpartner2013
        Michael's Instagram: https://www.instagram.com/zpartner_eu/
        Michael's Linkdin: https://www.linkedin.com/in/michael-fluch-0a250311
        Michael's Github: https://github.com/micflu73
        """

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    # Button "ASK" has been clicked
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

# ---------------------------------------------------------------------
st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Business Intelligence & Analytics Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")

with col2:
    st.video("https://www.youtube.com/watch?v=PEH9Uc25V1k")

# ---------------------------------------------------------------------
st.title(" ")

st.title("My Setup")
st.image("images/setup.png")

# ---------------------------------------------------------------------
st.title(" ")

st.title("My Skills")

### ---
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Technical Skills")

with col2:
    st.subheader("Business and Domain Knowledge")

with col3:
    st.subheader("Soft Skills")
### ---

col1, col2, col3 = st.columns(3)
with col1:
    s4h_arc_text = """
    The overall architecture of S/4HANA, including the underlying HANA database and how it differs from traditional databases. \n
    The concepts of in-memory computing and how it impacts performance and analytics. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    hana_text = """
    HANA data modeling techniques including calculation views, analytical views, and attribute views. \n
    How to use Eclipse / HANA Studio for creating and managing these models. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    cds_text = """
    Creating and using CDS views for S/4HANA. \n
    CDS views are central to S/4HANA Embedded Analytics \n
    as they allow the definition of data models at the application layer. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    abap_text = """
    Having a good understanding of ABAP on HANA (ABAP 7.5), \n
    especially for creating custom CDS views and enhancements. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    emb_text = """
    Hands-on experience with SAP Analytics Cloud (SAC), Smart Business KPIs, and Multi-Dimensional Reporting (MDX) capabilities in S/4HANA. \n
    Understand how to configure and use SAP BW/4HANA alongside S/4HANA for advanced analytical needs. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    fiori_text = """
    Use SAP Fiori to create intuitive, role-based user experiences. Customize and extend Fiori applications. \n
    Understanding of SAPUI5, the underlying technology for Fiori apps. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    st.slider("SAP S/4HANA Architecture", 0, 100, 85, help=s4h_arc_text)
    st.slider("SAP HANA Modelling", 0, 100, 75, help=hana_text)
    st.slider("Core Data Services (CDS) Views", 0, 100, 75, help=cds_text)
    st.slider("ABAP for S/4HANA", 0, 100, 70, help=abap_text)
    st.slider("Embedded Analytics Tools", 0, 100, 90, help=emb_text)
    st.slider("SAP Fiori and UX Design", 0, 100, 35, help=fiori_text)

with col2:
    fico_text = """
    Deep knowledge in the FI and CO modules within S/4HANA. \n
    Understanding the data structures and business processes. \n
    Know the integration points between FI/CO and other modules like \n
    Sales and Distribution (SD) and Materials Management (MM). \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    rtr_text = """
    Understand the specific reporting requirements and KPIs used in finance. \n
    This includes financial statements, profitability analysis, and cost center accounting. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    bp_text = """
    a strong understanding of end-to-end business processes in finance, \n
    such as Procure-to-Pay (P2P) and Order-to-Cash (O2C). \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    st.slider("Financial Accounting (FI) and Controlling (CO) Modules", 0, 100, 70, help=fico_text)
    st.slider("Real-time Reporting Requirements", 0, 100, 70, help=rtr_text)
    st.slider("Business Process Knowledge", 0, 100, 70, help=bp_text)

with col3:
    at_text = """
    The ability to analyze complex business requirements and translate them into technical solutions. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    com_text = """
    The ability to communicate effectively with both technical teams and business stakeholders. \n
    Clear communication is key to understanding requirements and explaining technical concepts. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    pm_text = """
    Project management skills to manage and deliver \n 
    analytics and technology effectively. \n
    Any further [questions](https://www.zpartner.eu/)?
    """
    st.slider("Analytical Thinking", 0, 100, 70, help=at_text)
    st.slider("Communication Skills", 0, 100, 70, help=com_text)
    st.slider("Project Management", 0, 100, 70, help=pm_text)

# ---------------------------------------------------------------------
st.title(" ")

st.title("Gallery")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("images/g11.png")
    st.image("images/g12.png")
    st.image("images/g13.jpg")
    st.image("images/g31.jpg")
    

with col2:
    st.image("images/g32.jpg")
    st.image("images/g22_blurred.jpg")
    st.image("images/g23_blurred.jpg")

with col3:
    st.image("images/g41.jpg")
    st.image("images/g33.jpg")
    st.image("images/g42.png")
    st.image("images/g43.png")

# ---------------------------------------------------------------------
st.title(" ")
st.title("CONTACT")
st.subheader("For any inquiries, email at: " + "michael.fluch@zpartner.eu")
