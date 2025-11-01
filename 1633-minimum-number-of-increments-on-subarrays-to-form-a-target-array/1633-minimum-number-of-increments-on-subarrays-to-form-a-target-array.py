class Solution:
    # def find_s_e_idx(self, target) :
    #     # 가장 작은 값을 기준으로 여러 리스트 셋을 분리한다.
    #     n = len(target)
    #     min_val = min(target)
    #     s_idx, e_idx = [], []
    #     for i, e in enumerate(target):
    #         if e != min_val:
    #             if len(s_idx) == len(e_idx):
    #                 s_idx.append(i)
    #         else:
    #             if len(s_idx) != len(e_idx):
    #                 e_idx.append(i-1)
    #     if len(s_idx) != len(e_idx):
    #         e_idx.append(n-1)

    #     return [s_idx, e_idx, min_val]
    
    # def get_cnt_from_section(self, section):
    #     s_idx, e_idx, min_val = self.find_s_e_idx(section)

    #     cnt = min_val
    #     for i in range(len(section)):
    #         section[i] -= min_val

    #     for s, e in zip(s_idx, e_idx):
    #         # 분리된 작은 리스트에서 최소값을 찾는다.
    #         tmp = section[s:e+1]
    #         min_cnt = min(tmp)
    #         cnt += min_cnt
    #         for i in range(len(tmp)):
    #             tmp[i] -= min_cnt
    #         # 최소값을 뺀 상태에서 count 값을 얻는 것을 반복한다.
    #         cnt += self.get_cnt_from_section(tmp)

    #     return cnt


    def minNumberOperations(self, target: List[int]) -> int:
        # 회귀 함수 사용한 버전 -> MLE 
        # return self.get_cnt_from_section(target)

        # 리스트 개수만큼 벽이 세워져 있다고 할때, 내려가는 것은 일이 들지 않으나 올라가는 것은 일이 발생한다.
        cnt = target[0]
        prev = target[0]
        for e in target[1:]:
            if prev < e:
                cnt += e - prev
            prev = e
            print(cnt)
        return cnt


