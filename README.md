# 🚗 Impact of Autonomous Vehicle Penetration on Traffic Flow and Emissions in Lagos

![image](https://github.com/Onabanjomicheal/third-mainland-av-hdv-simulation/blob/main/av.png)

A simulation-based study of the Third Mainland Bridge corridor to assess how varying levels of Autonomous Vehicle (AV) adoption influence **travel time**, **emissions**, and **platooning behavior** using **SUMO (Simulation of Urban Mobility)**.

---

### 🎬 Simulation Demo: AV Penetration on Third Mainland Bridge

Explore how different levels of Autonomous Vehicle (AV) penetration affect traffic dynamics on Lagos' busiest corridor.

[![Watch the video](https://img.youtube.com/vi/ibqoPXFH9O0/0.jpg)](https://youtu.be/ibqoPXFH9O0)

🔗 [Click here to watch on YouTube](https://youtu.be/ibqoPXFH9O0)

> 🎥 This 40-second demo provides a high-level visual of our SUMO simulation environment. For full methodology, scenarios, and results, see the rest of this repo.

## 📚 Table of Contents

- [📌 Project Motivation](#-project-motivation)
- [🌍 Network Setup](#-network-setup)
- [📈 Methodology](#-methodology)
- [🚦 Penetration Scenarios](#-penetration-scenarios)
- [📊 Key Simulation Results](#-key-simulation-results)
- [🧠 Insights & Analysis](#-insights--analysis)
- [📌 Recommendations](#-recommendations)
- [🔭 Future Work](#-future-work)
- [🔧 Technologies Used](#-technologies-used)
- [🙋‍♂️ Author Profile](#-author-profile)

---

## 📌 Project Motivation

Lagos is plagued by severe congestion and air pollution. As Autonomous Vehicles (AVs) become more viable, it's critical to assess their future impact on traffic efficiency and sustainability. This project simulates how AV adoption, under realistic traffic conditions, affects overall system performance.

---

## 🌍 Network Setup

We modeled the **Third Mainland Bridge**, a major arterial route in Lagos, using data from **OpenStreetMap (OSM)** and manually refined it in **NetEdit** for realism.

Vehicle classes simulated:
- `av_car` – Autonomous Vehicles (AVs)
- `hdv_car` – Human-Driven Private Cars
- `danfo_bus` – Informal Minibuses
- `brt` – Bus Rapid Transit Vehicles

---

## 📈 Methodology

1. **Road Network Creation:** Extracted from OSM, refined in NetEdit.
2. **Traffic Demand**
To reflect the real-world congestion on the Third Mainland Bridge, we based traffic demand on an estimated daily volume of over 105,000 vehicles—a figure reported in local traffic and infrastructure sources.
- With an average daily vehicular traffic of 117,000, Third Mainland Bridge in Lagos has been named the busiest road in the country by the ministry of works said by **The cable Media and Publishing Limited**
- This translates to roughly 5,435 vehicles per hour during peak flow conditions.
While not from a single authoritative dataset, the demand profile reflects a reasonable and realistic approximation of peak-hour bridge load, sufficient for comparative simulation of AV–HDV interaction.
4. **Vehicle Volume Estimation:**
   - Based on public news reports, social media traffic visuals, and research.
   - Estimated 5,435 vehicles/hour distributed as:
     - 3,750 Private Cars/hour  
     - 1,560 Minibuses/hour  
     - 125 BRTs/hour
5. **AV–HDV Distribution:**  
   Applied AV penetration only to private cars. Buses remain HDV-controlled.
6. **SUMO Simulation:**  
   - Traffic flow modeled over time using `sumo-gui`  
   - Used Python (Traci API) to track:
     - Vehicle entry/exit
     - Travel time
     - Emission levels
     - Platooning (AVs following AVs < 10m apart)

---

## 🚦 Penetration Scenarios

| Scenario     | AV % | AV Cars | HDV Cars | HDV Buses |
|--------------|------|---------|----------|------------|
| Conservative | 10%  | 375     | 3,375    | 1,685      |
| Moderate     | 30%  | 1,125   | 2,625    | 1,685      |
| Aggressive   | 50%  | 1,875   | 1,875    | 1,685      |

---

## 📊 Key Simulation Results

### 🔹 10% Penetration
- Avg Travel Time: **335.21 s**
- AV Platoons: **57**
- CO₂ Emissions: **3.06 × 10⁹ mg** (HDV Car)

### 🔹 30% Penetration
- Avg Travel Time: **323.95 s**
- AV Platoons: **391**
- CO₂ Emissions: **2.35 × 10⁹ mg** (HDV Car)

### 🔹 50% Penetration
- Avg Travel Time: **343.44 s**
- AV Platoons: **924**
- CO₂ Emissions: **2.12 × 10⁹ mg** (AV Car)

---

## 🧠 Insights & Analysis

- **Travel Time:** AVs help reduce travel time slightly at 10–30% but congestion persists at 50% due to AV–HDV interactions.
- **Emissions:** AVs consistently produce fewer emissions than HDVs.
- **Platooning:** AV platoons increase non-linearly with penetration — demonstrating better flow efficiency at higher densities.

---

## 📌 Recommendations

1. **Policy-Driven AV Integration:** Gradual adoption (starting at 30%) can yield measurable traffic and environmental benefits.
2. **Dedicated AV Lanes:** Consider AV-only lanes to improve platooning and reduce interaction friction.
3. **Mixed-Traffic Management:** Implement adaptive signal controls to handle AV–HDV coordination.
4. **Electric Vehicle (EV)**: As many AVs will be electric by design, layer EV infrastructure strategy into AV policy—charging accessibility, route planning, and energy grid integration must be considered from day one.
5. **Further Study:** Expand simulations to include incident response, weather conditions, or intersection behavior.

---

## 🔭 Future Work

- **Real-World Calibration:** Collect actual traffic counts for better calibration beyond social media estimates.
- **Intelligent Signal Control:** Integrate Deep Reinforcement Learning (e.g., Q-learning) for signal phase optimization.
- **Behavioral Diversity:** Simulate AV behaviors like cooperative merging, rerouting, or V2V/V2I response.
- **Geographic Expansion:** Extend analysis to other Lagos corridors or pan-African urban settings.
- **Multi-agent Interaction Models:** Study AV-HDV negotiation in denser traffic or intersections.

---

## 🔧 Technologies Used

- **SUMO** (1.23.1) – Microscopic traffic simulator
- **Python** – with Traci API, Pandas, Matplotlib
- **NetEdit** – SUMO network editor
- **OpenStreetMap (OSM)** – Source for road geometry

---

## 🙋‍♂️ Author Profile

**Onabanjo Micheal**  
Engineer | Researcher | Builder  
Passionate about AI for urban mobility, intelligent systems, and climate-resilient infrastructure.  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/micheal-onabanjo/)

> Connect or collaborate: *Feel free to reach out for academic or mobility-focused collaborations!*
