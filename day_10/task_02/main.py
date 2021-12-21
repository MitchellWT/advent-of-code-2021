from math import ceil, floor


class ChunkStack:
    def __init__(self):
        self.stack = []

    def push_consume(self, chunk_char: str) -> bool:
        if chunk_char == '(' or chunk_char == '[' or chunk_char == '{' or chunk_char == '<':
            self.stack.append(chunk_char)
            return True

        if self.stack[-1] == '(' and chunk_char == ')':
            self.stack.pop()
            return True
        if self.stack[-1] == '[' and chunk_char == ']':
            self.stack.pop()
            return True
        if self.stack[-1] == '{' and chunk_char == '}':
            self.stack.pop()
            return True
        if self.stack[-1] == '<' and chunk_char == '>':
            self.stack.pop()
            return True

        return False

    def get_completion_string(self) -> str:
        completion_string = ''
        while len(self.stack) != 0:
            if self.stack[-1] == '(':
                completion_string += ')'
                self.stack.pop()
            elif self.stack[-1] == '[':
                completion_string += ']'
                self.stack.pop()
            elif self.stack[-1] == '{':
                completion_string += '}'
                self.stack.pop()
            elif self.stack[-1] == '<':
                completion_string += '>'
                self.stack.pop()
        return completion_string

    def __str__(self):
        return str(self.stack)


def character_lookup(completion_char: str) -> int:
    if completion_char == ')':
        return 1
    if completion_char == ']':
        return 2
    if completion_char == '}':
        return 3
    if completion_char == '>':
        return 4


if __name__ == '__main__':
    subsystem_lines = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            subsystem_lines.append(input_line.replace('\n', ''))

    completion_scores = []
    for subsystem_line in subsystem_lines:
        chunkStack = ChunkStack()
        completion_score = 0
        corrupt = False
        for subsystem_char in subsystem_line:
            if not chunkStack.push_consume(subsystem_char):
                corrupt = True
                break
        if corrupt:
            continue
        completion_list = list(chunkStack.get_completion_string())
        for completion_char in completion_list:
            completion_score *= 5
            completion_score += character_lookup(completion_char)
        completion_scores.append(completion_score)

    completion_scores.sort()
    median_index = ceil(len(completion_scores) / 2) - 1

    print(completion_scores[median_index])
