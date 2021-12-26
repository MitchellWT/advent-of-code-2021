
class CaveGraph:
    def __init__(self):
        self.graph_dict = {}
        self.visited_caves = []
        self.all_paths = []

    def keys(self) -> [str]:
        return self.graph_dict.keys()

    def add_key(self, key: str):
        self.graph_dict[key] = []

    def add_value(self, key: str, value: str):
        self.graph_dict[key].append(value)

    def depth_first_search(self, current_cave: str, ending_cave: str,
                           current_path: [str]):
        if current_cave.islower():
            self.visited_caves.append(current_cave)
        current_path.append(current_cave)

        if current_cave == ending_cave:
            self.all_paths.append(current_path.copy())
        else:
            for connected_cave in self.graph_dict[current_cave]:
                if connected_cave not in self.visited_caves:
                    self.depth_first_search(connected_cave, ending_cave,
                                            current_path)
        if current_cave.islower():
            self.visited_caves.remove(current_cave)
        current_path.pop()

    def count_paths(self) -> int:
        return len(self.all_paths)


if __name__ == '__main__':
    cave_graph = CaveGraph()
    with open('./input_data') as input_data:
        for input_line in input_data:
            input_line = input_line.replace('\n', '')
            input_caves = input_line.split('-')
            if input_caves[0] not in cave_graph.keys():
                cave_graph.add_key(input_caves[0])
            if input_caves[1] not in cave_graph.keys():
                cave_graph.add_key(input_caves[1])
            cave_graph.add_value(input_caves[0], input_caves[1])
            cave_graph.add_value(input_caves[1], input_caves[0])

    cave_graph.depth_first_search('start', 'end', [])
    print(cave_graph.count_paths())
