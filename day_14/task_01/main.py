
def read_data(input_file: str) -> (str, [[str, str]]):
    polymer_template = ''
    pair_insertion = []
    with open(input_file) as input_data:
        for input_line in input_data:
            if input_line == '\n':
                continue
            if '->' not in input_line:
                polymer_template = input_line.replace('\n', '')
                continue
            insertion_data = input_line.split('->')
            pair_insertion.append([insertion_data[0].strip(), insertion_data[1].strip()])

    return polymer_template, pair_insertion


def run_step(polymer_template: str, pair_insertion: [[str, str]]) -> str:
    working_polymer = polymer_template
    insertion_counter = 1

    for index in range(len(polymer_template)):
        polymer_segment = polymer_template[index:index + 2]
        for pair in pair_insertion:
            if polymer_segment == pair[0]:
                insertion_index = index + insertion_counter
                working_polymer = working_polymer[:insertion_index] + pair[1] + working_polymer[insertion_index:]
                insertion_counter += 1

    return working_polymer


if __name__ == '__main__':
    working_polymer, pair_insertion = read_data('./input_data')
    compound_count = []

    for _ in range(10):
        working_polymer = run_step(working_polymer, pair_insertion)

    for compound in set(working_polymer):
        compound_count.append(working_polymer.count(compound))

    most_compound = compound_count[0]
    least_compound = compound_count[0]

    for count in compound_count:
        if count > most_compound:
            most_compound = count
        if count < least_compound:
            least_compound = count

    print(most_compound - least_compound)
