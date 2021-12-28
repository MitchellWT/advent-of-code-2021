
def read_data(input_file: str) -> ({str: int}, [[str, str]], str):
    polymer_dict = {}
    pair_insertion = []
    last_component = ''
    with open(input_file) as input_data:
        for input_line in input_data:
            if input_line == '\n':
                continue
            if '->' not in input_line:
                polymer_template = list(input_line.replace('\n', ''))
                last_component = polymer_template[-1]
                for index, polymer_compound in enumerate(polymer_template):
                    if index is (len(polymer_template) - 1):
                        continue
                    compound_pair = polymer_compound + polymer_template[index + 1]
                    if compound_pair in polymer_dict.keys():
                        polymer_dict[compound_pair] += 1
                        continue
                    polymer_dict[compound_pair] = 1
                continue
            insertion_data = input_line.split(' -> ')
            insertion_data[1] = insertion_data[1].replace('\n', '')
            first_product = insertion_data[0][0] + insertion_data[1]
            second_product = insertion_data[1] + insertion_data[0][1]
            pair_insertion.append([insertion_data[0].strip(), (first_product, second_product)])

    return polymer_dict, pair_insertion, last_component


def run_step(polymer_dict: {str: int}, pair_insertion: [[str, (str, str)]]) -> {str: int}:
    working_dict = {}

    for polymer_pair in polymer_dict.keys():
        for insertion in pair_insertion:
            if polymer_pair == insertion[0]:
                for insertion_product in insertion[1]:
                    if insertion_product in working_dict:
                        working_dict[insertion_product] += polymer_dict[polymer_pair]
                        continue
                    working_dict[insertion_product] = polymer_dict[polymer_pair]
                break

    return working_dict


def count_components(polymer_dict: {str: int}, last_component: str) -> {str: int}:
    component_dict = {}

    for component_pair in polymer_dict.keys():
        if component_pair[0] not in component_dict.keys():
            component_dict[component_pair[0]] = polymer_dict[component_pair]
            continue
        component_dict[component_pair[0]] += polymer_dict[component_pair]
    component_dict[last_component] += 1

    return component_dict


if __name__ == '__main__':
    polymer_dict, pair_insertion, last_component = read_data('./input_data')

    for _ in range(40):
        polymer_dict = run_step(polymer_dict, pair_insertion)

    component_dict = count_components(polymer_dict, last_component)
    max_component = max(component_dict.values())
    min_component = min(component_dict.values())

    print(max_component - min_component)
