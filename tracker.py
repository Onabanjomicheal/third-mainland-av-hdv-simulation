import os
import sys
import traci
import matplotlib.pyplot as plt
import pandas as pd
import xml.etree.ElementTree as ET
from collections import defaultdict

# Step 1: Setup SUMO environment
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# Step 2: Simulation config
sumo_config = [
    'sumo-gui',
    '-c', 'third_mainland_bridge.sumocfg'
]

# Step 3: Start simulation
traci.start(sumo_config)

# Step 4: Initialize tracking
depart_times = {}
travel_times = {}
vehicle_types = {}
platooned_pairs = set()

# Step 5: Travel time updater
def update_vehicle_times(current_time):
    for veh_id in traci.vehicle.getIDList():
        if veh_id not in depart_times:
            depart_times[veh_id] = current_time
            vehicle_types[veh_id] = traci.vehicle.getTypeID(veh_id)
    for veh_id in traci.simulation.getArrivedIDList():
        if veh_id in depart_times:
            travel_times[veh_id] = current_time - depart_times[veh_id]

# Step 6: Platoon tracker
def detect_av_platoons():
    for veh_id in traci.vehicle.getIDList():
        if "av" in vehicle_types.get(veh_id, "").lower():
            try:
                leader_info = traci.vehicle.getLeader(veh_id)
                if leader_info:
                    leader_id, gap = leader_info
                    if "av" in vehicle_types.get(leader_id, "").lower() and gap < 10:
                        pair = tuple(sorted((veh_id, leader_id)))
                        platooned_pairs.add(pair)
            except traci.exceptions.TraCIException:
                pass

# Step 7: Run simulation loop
max_time_limit = 10000
idle_steps = 0

while traci.simulation.getTime() < max_time_limit:
    traci.simulationStep()
    update_vehicle_times(traci.simulation.getTime())
    detect_av_platoons()

    if traci.simulation.getMinExpectedNumber() == 0:
        idle_steps += 1
        if idle_steps > 100:
            break
    else:
        idle_steps = 0

final_time = traci.simulation.getTime()
traci.close()

# Step 8: Travel stats
print(f"\n✅ Simulation ended at: {final_time:.2f} seconds")
print(f"📦 Vehicles completed: {len(travel_times)}")
print(f"🚀 Vehicles departed: {len(depart_times)}")
print(f"🛑 Vehicles still in network: {len(depart_times) - len(travel_times)}")

if travel_times:
    avg_time = sum(travel_times.values()) / len(travel_times)
    print(f"🚗 Overall average travel time: {avg_time:.2f} s")

# Step 9: Travel time by type
df = pd.DataFrame({
    'veh_id': list(travel_times.keys()),
    'travel_time': list(travel_times.values()),
    'type': [vehicle_types[v] for v in travel_times]
})
avg_by_type = df.groupby('type')['travel_time'].mean()
print("\n📊 Average Travel Time by Vehicle Type:")
print(avg_by_type)

# Step 10: Travel time bar chart
plt.figure(figsize=(6, 4))
avg_by_type.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Travel Time by Vehicle Type')
plt.ylabel('Time (s)')
plt.xlabel('Vehicle Type')
plt.tight_layout()
plt.show()

# Step 11: Emission Analysis (trend + total)
def analyze_emissions(emission_file):
    print(f"\n--- 📊 Emission Analysis by Real Vehicle Type: {emission_file} ---")
    try:
        tree = ET.parse(emission_file)
        root = tree.getroot()

        emissions_by_type = defaultdict(lambda: {'CO2': 0.0, 'NOx': 0.0, 'fuel': 0.0})
        time_series = {'time': [], 'CO2': [], 'NOx': [], 'fuel': []}

        for timestep in root.findall('timestep'):
            time = float(timestep.get('time'))
            co2_sum, nox_sum, fuel_sum = 0.0, 0.0, 0.0

            for vehicle in timestep.findall('vehicle'):
                veh_id = vehicle.get('id')
                vtype = vehicle_types.get(veh_id, 'unknown')

                co2 = float(vehicle.get('CO2', 0))
                nox = float(vehicle.get('NOx', 0))
                fuel = float(vehicle.get('fuel', 0))

                emissions_by_type[vtype]['CO2'] += co2
                emissions_by_type[vtype]['NOx'] += nox
                emissions_by_type[vtype]['fuel'] += fuel

                co2_sum += co2
                nox_sum += nox
                fuel_sum += fuel

            time_series['time'].append(time)
            time_series['CO2'].append(co2_sum)
            time_series['NOx'].append(nox_sum)
            time_series['fuel'].append(fuel_sum)

        df_emissions = pd.DataFrame(emissions_by_type).T
        print(df_emissions.sort_values(by='CO2', ascending=False))

        # Emission trend chart
        plt.figure(figsize=(10, 5))
        for pollutant in ['CO2', 'NOx', 'fuel']:
            plt.plot(time_series['time'], time_series[pollutant], label=pollutant)
        plt.title('Emission Trend Over Time')
        plt.xlabel('Simulation Time (s)')
        plt.ylabel('Emission Value')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        # Total Emissions by Type
        df_emissions.plot(kind='bar', figsize=(10, 5))
        plt.title('Total Emissions by Vehicle Type')
        plt.ylabel('Emission Value')
        plt.xlabel('Vehicle Type')
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Error processing emission file: {e}")

analyze_emissions('emission_output.xml')

# Step 12: Platooning Summary
print(f"\n🤖 Estimated AV Platoon Pairs (gap < 10m): {len(platooned_pairs)}")

