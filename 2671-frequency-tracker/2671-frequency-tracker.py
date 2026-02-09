from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        
        self.count = defaultdict(int)
        
        self.freqCount = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.count[number]
        if old_freq > 0:
            self.freqCount[old_freq] -= 1

        self.count[number] += 1
        new_freq = self.count[number]
        self.freqCount[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if self.count[number] == 0:
            return

        old_freq = self.count[number]
        self.freqCount[old_freq] -= 1

        self.count[number] -= 1
        new_freq = self.count[number]
        if new_freq > 0:
            self.freqCount[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqCount[frequency] > 0
