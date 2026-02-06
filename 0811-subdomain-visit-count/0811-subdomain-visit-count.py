class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map=defaultdict(int)

        for cpdomain in cpdomains:
            count_str,domain=cpdomain.split()
            count=int(count_str)

            sub_domains=domain.split('.')
            for i in range(len(sub_domains)):
                sub_domain='.'.join(sub_domains[i:])

                count_map[sub_domain]+=count

        return [f'{count} {sub}' for sub,count in count_map.items() ]
