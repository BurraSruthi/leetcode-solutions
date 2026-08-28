class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        half_len = n // 2

        cnt = Counter(s)

        # A palindrome can have at most one odd-frequency character
        odd = [ch for ch in cnt if cnt[ch] % 2]

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Counts available for the left half
        half = [0] * 26

        for ch in cnt:
            half[ord(ch) - ord('a')] = cnt[ch] // 2

        t = target[:half_len]

        def build(left):
            return left + middle + left[::-1]

        # Check if target's left half can be formed
        remaining = half[:]
        possible_prefix = True

        for ch in t:
            x = ord(ch) - ord('a')

            if remaining[x] == 0:
                possible_prefix = False
                break

            remaining[x] -= 1

        # Case 1:
        # target's left half can be formed.
        # Check whether its palindrome is already greater.
        if possible_prefix:
            candidate = build(t)

            if candidate > target:
                return candidate

        # Case 2:
        # Find the smallest left half greater than target's left half.
        #
        # We try to make:
        # target[0:i] + bigger_character + smallest_remaining

        for i in range(half_len - 1, -1, -1):

            remaining = half[:]
            ok = True

            # Use target characters before position i
            for j in range(i):
                x = ord(target[j]) - ord('a')

                if remaining[x] == 0:
                    ok = False
                    break

                remaining[x] -= 1

            if not ok:
                continue

            # Find the smallest character greater than target[i]
            x = ord(target[i]) - ord('a')

            bigger = -1

            for c in range(x + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            # Put the bigger character
            remaining[bigger] -= 1

            left = target[:i] + chr(bigger + ord('a'))

            # Fill the rest with smallest characters
            for c in range(26):
                left += chr(c + ord('a')) * remaining[c]

            candidate = build(left)

            if candidate > target:
                return candidate

        return ""