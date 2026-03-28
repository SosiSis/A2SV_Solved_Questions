class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        answer_counts = Counter(answers)
      
        total_rabbits = 0

        for answer_value, frequency in answer_counts.items():

            group_size = answer_value + 1

            num_groups = (frequency + group_size - 1) // group_size

            total_rabbits += num_groups * group_size
      
        return total_rabbits