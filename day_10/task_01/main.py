
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

    def __str__(self):
        return str(self.stack)


def character_lookup(chunk_char: str) -> int:
    if chunk_char == ')':
        return 3
    if chunk_char == ']':
        return 57
    if chunk_char == '}':
        return 1197
    if chunk_char == '>':
        return 25137


if __name__ == '__main__':
    subsystem_lines = []
    with open('./input_data') as input_data:
        for input_line in input_data:
            subsystem_lines.append(input_line.replace('\n', ''))

    syntax_error_score = 0
    for subsystem_line in subsystem_lines:
        chunkStack = ChunkStack()
        for subsystem_char in subsystem_line:
            if not chunkStack.push_consume(subsystem_char):
                syntax_error_score += character_lookup(subsystem_char)
                break

    print(syntax_error_score)
