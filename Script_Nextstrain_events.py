import json

with open('data.json', 'r') as f:
    data = json.load(f)

def had_mutation(node):
    nucleotides = node.get("branch_attrs", {}).get("mutations", {}).get("nuc", [])
    if mutation_to_find in nucleotides:
        nodes_with[id(node)] = node
        return True
    return False
def number_of_mutations_subtree(node, nodes_with):
    count = 0
    for child in node.get("children", []):
        count += number_of_mutations_subtree(child, nodes_with)
        if not had_mutation(node):
            if had_mutation(child):
                count += 1 # count the mutation in the child if the parent doesn't have it
    return count

mutations = ["A954G","A1184G","A1306T"]

for mutation_to_find in mutations:
    nodes_with = dict()
    mutation_points_number = number_of_mutations_subtree(data["tree"], nodes_with)
    print(f"Number of mutation points for {mutation_to_find}: {mutation_points_number}")
    print(f"Number of nodes with mutation {mutation_to_find}: {len(nodes_with)}")
    for node_id, node in nodes_with.items():
        print(f"Node Name: {node.get('name', 'N/A')}")
