#Mystery Delivery System

#Project Description

This project simulates package delivery operations for the FastBox logistics system.

python code contain in solution.py

The program reads warehouse, agent, and package data from JSON files, assigns packages to nearest agents, simulates deliveries, calculates travel distance, and generates `report.json`.

Extra features:
- Random delivery delays
- New agent joining mid-day
- Multiple JSON format support

#Requirements

Project features:

1. Read JSON input data
2. Calculate Euclidean distance
3. Assign nearest agent
4. Simulate deliveries
5. Generate report
6. Save output in `report.json`

Bonus:
- Random delays
- Mid-day agent joining

#Project Structure

```text
FastBox_Project/
│
├── solution.py
├── README.md
├── report.json
├── base_case.json
├── test_case_1.json
├── test_case_2.json
├── ...
└── test_case_10.json
```

#Input Formats

Format 1:

```json
{
   "warehouses":{
      "W1":[0,0]
   },
   "agents":{
      "A1":[5,5]
   }
}
```

Format 2:

```json
{
   "warehouses":[
      {
         "id":"W1",
         "location":[0,0]
      }
   ]
}
```

Supported files:
- `base_case.json`
- `test_case_1.json` to `test_case_10.json`

#Function Logic

#1.read_json()
Reads JSON input file.

calculate_distance()`
Calculates Euclidean distance:

```text
√((x2-x1)^2 + (y2-y1)^2)
```

#2.get_warehouse_locations()
Converts warehouse data into dictionary format.

#3.get_agent_locations()
Creates agent location mapping.

#4.find_nearest_agent()
Finds closest delivery agent.

#4.`assign_packages()`
Assigns packages to nearest agents.

#5.`delivery_simulation()`
Simulates:

```text
Agent → Warehouse → Destination
```

Calculates:
- Distance
- Delay
- Delivered packages
- Efficiency

#6.`add_new_agent()`
Adds new delivery agent:

```python
A_NEW
```

#7.`merge_reports()`
Combines first and second delivery phases.

#8.`save_report()`
Creates output file:

```text
report.json
```

#9.Random Delay Feature

Delay range:

```python
random.randint(5,30)
```

Example:

```json
"delay_minutes":15
```

#11.Mid-Day Agent Feature

New agent joins after first delivery phase.

Example:

```python
add_new_agent(
    agents,
    "A_NEW",
    [50,50]
)
```

#Output Example
```json
{
   "A1":{
      "packages_delivered":2,
      "total_distance":85.33,
      "efficiency":42.66,
      "delay_minutes":18
   },

   "best_agent":"A1"
}
```

#Run Project

Base case:

```bash
python solution.py base_case.json
```

Test cases:

```bash
python solution.py test_case_1.json
python solution.py test_case_2.json
python solution.py test_case_3.json
python solution.py test_case_4.json
python solution.py test_case_5.json
python solution.py test_case_6.json
python solution.py test_case_7.json
python solution.py test_case_8.json
python solution.py test_case_9.json
python solution.py test_case_10.json
```

#Technologies Used

- Python 3
- JSON
- Math
- Random

