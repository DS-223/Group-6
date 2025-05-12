# Marketing Analytics Project: A/B Testing for Hot Sales Display Optimization  

## Problem Definition  

### The Problem Area  
**A/B Testing** – Optimizing the online display of promotional content to improve customer engagement and sales in the e-commerce grocery and retail sector.  

### Defining the Specific Problem  
Supermarkets lack data-driven guidelines on the optimal sequence to display "Hot Sales" items on their website homepage. The absence of an optimized ordering may result in:  
- Lower click-through rates (CTR)  
- Missed sales opportunities  
- Suboptimal customer engagement  

## Proposed Solution & Methodology  

### Data Collection  
- Conduct a **controlled A/B test** with two or more homepage versions, each displaying "Hot Sales" products in a different order.  
- Track user interactions (clicks, time spent, conversions) and store data in a structured database.  

**Microservice Components:**
- **Frontend:** Streamlit – displays model outputs and visualizations
- **Backend:** FastAPI – exposes endpoints to interact with the model and database
- **Database:** PostgreSQL – stores users and bandit parameters
- **Model:** Thompson Sampling (Bayesian Bandit Algorithm) – used for product ranking and experimentation
- **Documentation:** 


## Expected Outcomes  
- **Higher CTR** on "Hot Sales" items.  
- **Increased revenue** from optimized product placement.  

---
**Next Steps**:  
- Link to [methodology](model.md) for technical details.  
- Refer to [database schema](database.md) for data collection structure.  
