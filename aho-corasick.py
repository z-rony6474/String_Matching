from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.output = []

class AhoCorasick:
    def __init__(self, words):
        self.root = TrieNode()
        self.build_trie(words)
        self.build_automaton()

    def build_trie(self, words):
        for word in words:
            node = self.root
            for char in word:
                node = node.children[char]
            node.output.append(word)

    def build_automaton(self):
        queue = deque()

        # Set failure function for depth-1 nodes
        for key, node in self.root.children.items():
            node.fail = self.root
            queue.append(node)

        # Set failure function for other nodes using BFS
        while queue:
            current_node = queue.popleft()
            for key, child_node in current_node.children.items():
                queue.append(child_node)
                failure_state = current_node.fail

                while failure_state != self.root and key not in failure_state.children:
                    failure_state = failure_state.fail

                if key in failure_state.children:
                    child_node.fail = failure_state.children[key]
                else:
                    child_node.fail = self.root

                child_node.output.extend(child_node.fail.output)

    def search_words(self, text):
        results = defaultdict(list)
        current_state = self.root

        operations = 0
        for i, char in enumerate(text):
            operations += 1

            while current_state != self.root and char not in current_state.children:
                current_state = current_state.fail
                operations += 1

            if char in current_state.children:
                current_state = current_state.children[char]
                for word in current_state.output:
                    results[word].append(i - len(word) + 1)

        return results, operations

def get_user_input():
    text = input("Enter the text: ")
    words = input("Enter words to search for (comma-separated): ").split(',')
    words = [word.strip() for word in words]
    return text, words

# Example Usage
if __name__ == "__main__":
    text, words = get_user_input()

    start_time = time.time()
    aho_corasick = AhoCorasick(words)
    results, operations = aho_corasick.search_words(text)
    end_time = time.time()
    execution_time = end_time - start_time

    print("Input Text:", text)
    print("Words to Search For:", words)
    print("Aho-Corasick:")
    for word in results:
        for position in results[word]:
            print(f"Word '{word}' found at position {position}")
    print("Number of operations:", operations)
    print("Execution time:", execution_time, "seconds")