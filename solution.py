import json
import math
import random
import sys


# read json
def read_json(file_name):
    # open json file in read mode
    with open(file_name, "r") as file:
        # convert json data into python dictionary
        data = json.load(file)

    return data


# # function to calculate distance between two points
def calculate_distance(p1, p2):

    x1, y1 = p1
    x2, y2 = p2
    # apply Euclidean distance formula
    value = math.sqrt((x2 - x1) ** 2 +(y2 - y1) ** 2)

    return value


# function to convert warehouse data into dictionary format
# supports both list and dictionary json structures
def get_warehouse_locations(data):
    # create empty warehouse dictionary
    warehouse_dict = {}
    # check if input data is already dictionary format
    if isinstance(data, dict):
        # copy warehouse id and location
        for key in data:
            warehouse_dict[key] = data[key]

    else:
        # handle list format input
        for item in data:
            # store warehouse id and location
            warehouse_dict[item["id"]] = item["location"]

    return warehouse_dict


# create agent data in a single format
# supports both dictionary and list style inputs
def get_agent_locations(data):

    # store agent information here
    agent_dict = {}

    # check if agent data is already dictionary type
    if isinstance(data, dict):

        # copy agent id and location
        for key in data:

            agent_dict[key] = data[key]
    else:
        # process list based agent records
        for item in data:

            # save agent id with coordinates
            agent_dict[
                item["id"]
            ] = item["location"]

    # return prepared agent data
    return agent_dict


# find which agent is closest to the warehouse
def find_nearest_agent(warehouse_location,agents):

    # store selected agent name
    selected = None

    # start with very large value
    minimum = float("inf")

    # check distance for every agent
    for agent in agents:

        current = calculate_distance(agents[agent], warehouse_location)

        # update if smaller distance is found
        if current < minimum:

            minimum = current

            selected = agent

    # return nearest agent id
    return selected

# assign packages to the nearest available agent
def assign_packages(packages,warehouses,agents):

    # store package list for each agent
    result = {}

    # create empty delivery list
    for agent in agents:
        result[agent] = []

    # process all packages one by one
    for package in packages:

        # support both warehouse formats
        if "warehouse_id" in package:

            warehouse_id = package["warehouse_id"]

        else:

            warehouse_id = package["warehouse"]

        # get warehouse coordinates
        warehouse_location = warehouses[warehouse_id]

        # find closest agent
        agent = find_nearest_agent(warehouse_location,agents)

        # add package to selected agent
        result[agent].append( package)

    # return final assignment data
    return result


# add a new delivery agent during running process
def add_new_agent(
        agents,
        agent_name,
        location
):

    # save new agent name and location
    agents[
        agent_name
    ] = location

    # show joining message
    print(
        agent_name,
        "joined mid-day"
    )


# simulate delivery process
def delivery_simulation(assignments,warehouses,agents):

    # store final report
    report = {}

    # check each agent
    for agent in agents:

        # current agent location
        current = agents[agent]

        # total travel distance
        distance = 0

        # delivered package count
        delivered = 0

        # total delay time
        delay_total = 0

        # get assigned packages
        package_list = assignments.get(agent, [])

        # process packages
        for package in package_list:

            # support both json formats
            if "warehouse_id" in package:

                warehouse_id = package[
                    "warehouse_id"
                ]

            else:

                warehouse_id = package[
                    "warehouse"
                ]

            # warehouse position
            warehouse_location = warehouses[
                warehouse_id
            ]

            # customer location
            destination = package[ "destination"]

            # agent to warehouse distance
            move1 = calculate_distance(current,warehouse_location)

            # warehouse to destination distance
            move2 = calculate_distance( warehouse_location,destination)

            # update total distance
            distance += move1
            distance += move2

            # create random delay
            delay = random.randint(5,30)

            delay_total += delay

            # update current location
            current = destination

            delivered += 1

        # calculate efficiency
        if delivered > 0:

            efficiency = (distance /delivered)

        else:

            efficiency = 0

        # save agent report
        report[agent] = {

            "packages_delivered":
            delivered,

            "total_distance":
            round(
                distance,
                2
            ),

            "efficiency":
            round(
                efficiency,
                2
            ),

            "delay_minutes":
            delay_total
        }

    # return report
    return report


# combine both delivery reports
def merge_reports(
        r1,
        r2,
        agents
):

    # store final data
    final = {}

    # check each agent
    for agent in agents:

        delivered = 0
        distance = 0
        delay = 0

        # read both reports
        for report in [r1, r2]:

            if agent in report:

                # add package count
                delivered += report[
                    agent
                ][
                    "packages_delivered"
                ]

                # add distance
                distance += report[
                    agent
                ][
                    "total_distance"
                ]

                # add delay
                delay += report[
                    agent
                ][
                    "delay_minutes"
                ]

        # calculate efficiency
        if delivered > 0:

            efficiency = (
                distance /
                delivered
            )

        else:

            efficiency = 0

        # save final result
        final[agent] = {

            "packages_delivered":
            delivered,

            "total_distance":
            round(
                distance,
                2
            ),

            "efficiency":
            round(
                efficiency,
                2
            ),

            "delay_minutes":
            delay
        }

    # return merged report
    return final

# find agent with best efficiency
def get_best_agent(report):

    # store best agent name
    best = None

    # start with large value
    minimum = float("inf")

    # check all agents
    for agent in report:

        # get delivered count
        delivered = report[
            agent
        ][
            "packages_delivered"
        ]

        # skip empty delivery
        if delivered == 0:
            continue

        # get efficiency value
        value = report[
            agent
        ][
            "efficiency"
        ]

        # update best agent
        if value < minimum:

            minimum = value

            best = agent

    # return best performer
    return best


# save final report into json file
def save_report(data):

    # output file name
    output_file = "report.json"

    # create report file
    with open(
            output_file,
            "w"
    ) as file:

        # write report data
        json.dump(
            data,
            file,
            indent=4
        )

    # show success message
    print(
        "\nReport generated successfully"
    )

    # display output file name
    print(
        "Output file:",
        output_file
    )
    
# main function
def main():

    # check command input
    if len(sys.argv) < 2:

        print(
            "python solution.py base_case.json"
        )

        return

    # get json file name
    file_name = sys.argv[1]

    # read input file
    data = read_json(
        file_name
    )

    # load warehouse data
    warehouses = get_warehouse_locations(
        data["warehouses"]
    )

    # load agent data
    agents = get_agent_locations(
        data["agents"]
    )

    # get package list
    packages = data["packages"]

    # divide packages into two parts
    middle = len(packages) // 2

    first = packages[:middle]

    second = packages[middle:]

    # first delivery assignment
    assign1 = assign_packages(
        first,
        warehouses,
        agents
    )

    # first delivery report
    report1 = delivery_simulation(
        assign1,
        warehouses,
        agents
    )

    # add new agent
    add_new_agent(
        agents,
        "A_NEW",
        [50, 50]
    )

    # second delivery assignment
    assign2 = assign_packages(
        second,
        warehouses,
        agents
    )

    # second delivery report
    report2 = delivery_simulation(
        assign2,
        warehouses,
        agents
    )

    # combine reports
    final_report = merge_reports(
        report1,
        report2,
        agents
    )

    # find best agent
    final_report[
        "best_agent"
    ] = get_best_agent(
        final_report
    )

    # save output file
    save_report(
        final_report
    )

    # print final result
    print(
        json.dumps(
            final_report,
            indent=4
        )
    )

# run main program
if __name__ == "__main__":
    main()

