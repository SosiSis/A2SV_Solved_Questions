class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        """
        Partitions the string s into as many parts as possible such that each letter appears in at most one part.

        Args:
            s: The input string.

        Returns:
            A list of integers representing the size of each part.
        """
        last_occurrence = {char: index for index, char in enumerate(s)}
        partition_lengths = []

        start_index = 0
        end_index = 0

        for i, char in enumerate(s):
            end_index = max(end_index, last_occurrence[char])

            if i == end_index:
                partition_lengths.append(end_index - start_index + 1)
                start_index = i + 1

        return partition_lengths
