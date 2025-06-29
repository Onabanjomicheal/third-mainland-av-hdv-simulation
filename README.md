# 🚗 Simulation of Autonomous Vehicle Penetration on Third Mainland Bridge, Lagos

This project explores how introducing Autonomous Vehicles (AVs) at varying penetration rates (10%, 30%, 50%) affects traffic dynamics, emission trends, and platooning behavior on the Third Mainland Bridge in Lagos, Nigeria.

---

## 📚 Table of Contents

- [📌 Overview](#-overview)
- [🧠 Motivation](#-motivation)
- [🌐 Network Setup](#-network-setup)
- [🔢 Traffic Volume Derivation](#-traffic-volume-derivation)
- [🚦 Penetration Scenarios](#-penetration-scenarios)
- [📈 Key Simulation Results](#-key-simulation-results)
- [📊 Insights](#-insights)
- [🚀 Future Work](#-future-work)
- [👤 Author](#-author)
- [📝 License](#-license)

---

## 📌 Overview

We used the open-source traffic simulator **SUMO (Simulation of Urban Mobility)** to study how increasing levels of AV adoption might transform mobility on Africa’s busiest bridge corridor. The simulation evaluates travel time performance, vehicular emissions (CO₂, NOₓ, fuel), and the formation of AV platoons under different adoption scenarios.

---

## 🧠 Motivation

Lagos, like many megacities, faces severe traffic congestion and pollution. This project envisions how integrating AVs can:

- Enhance traffic efficiency
- Lower greenhouse emissions
- Enable coordinated platooning

The results will help guide future research and urban mobility policy, especially in emerging cities.

---

## 🌐 Network Setup

- Extracted the **Third Mainland Bridge** layout from **OpenStreetMap (OSM)**
- Cleaned and optimized the network using `netconvert`
- Calibrated lanes and vehicle routes to reflect local traffic conventions

---

## 🔢 Traffic Volume Derivation

Since there are limited open-access traffic count datasets for Lagos, we estimated vehicle volumes using a blend of:

- **Eyewitness traffic reports**
- **Social media-based traffic updates**
- **Local transportation blogs and research**
- **Engineering intuition** based on road function and lane capacity

Final estimated volumes per hour:

| Vehicle Type     | Volume per Hour |
|------------------|-----------------|
| Private Cars     | 3,750           |
| Danfo Minibuses  | 1,560           |
| BRT Buses        | 125             |

We applied **AV–HDV penetration scenarios only to private cars**, assuming all buses remain human-driven for now.

---

## 🚦 Penetration Scenarios

| Scenario           | AV Cars | HDV Cars | Total Vehicles |
|--------------------|---------|----------|----------------|
| Conservative (10%) | 375     | 5,077    | 5,452          |
| Moderate (30%)     | 1,125   | 4,327    | 5,452          |
| Aggressive (50%)   | 1,875   | 3,577    | 5,452          |

Each simulation maintains a consistent traffic volume of 5,452 vehicles per run.

---

## 📈 Key Simulation Results

### ✅ 10% AV Penetration
- Simulation Time: `5471.00 s`
- Average Travel Time: `335.21 s`
- AV Platoon Pairs: `57`
- Emission Leaders: HDVs and Danfo

### ✅ 30% AV Penetration
- Simulation Time: `4903.00 s`
- Average Travel Time: `323.95 s`
- AV Platoon Pairs: `391`
- AVs emit more due to numbers, but remain more efficient per vehicle

### ✅ 50% AV Penetration
- Simulation Time: `4776.00 s`
- Average Travel Time: `343.44 s`
- AV Platoon Pairs: `924`
- Highest AV coordination and platooning efficiency, but also increased congestion from traffic merging

---

## 📊 Insights

1. **Traffic Flow**: AVs improve traffic flow up to 30%, but 50% begins to saturate capacity without dedicated infrastructure.
2. **Emissions**: AVs show lower emissions per vehicle, but their totals grow with volume.
3. **Platooning**: Emerges naturally with AV density; sharp rise from 57 pairs at 10% to 924 at 50%.
4. **Lane Dynamics**: Mixed traffic (AV–HDV) causes interruptions, especially for platooning under low penetration.

---

## 🚀 Future Work

- Simulate **dedicated AV lanes** or BRT-style corridors for platoons
- Model intersections, rerouting behavior, and network spillbacks
- Integrate **reinforcement learning-based traffic control**

---

## 👤 Author

**Onabanjo Michael**  
Simulation & Intelligent Transport Researcher  
_Passionate about building sustainable and tech-driven mobility systems in Africa._

---

