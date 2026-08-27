class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        ans = []

        # Try to keep the prefix equal to target
        for i in range(n):
            x = ord(target[i]) - ord('a')

            # Can we put target[i] itself?
            if count[x] > 0:
                ans.append(target[i])
                count[x] -= 1
                continue

            # We cannot continue with an equal prefix.
            # Find the smallest character greater than target[i].
            for c in range(x + 1, 26):
                if count[c] > 0:
                    ans.append(chr(c + ord('a')))
                    count[c] -= 1

                    # Append all remaining characters in sorted order
                    for j in range(26):
                        ans.extend(chr(j + ord('a')) * count[j])

                    return ''.join(ans)

            # No greater character at this position.
            # We must backtrack to an earlier position.
            break

        # The whole string was equal to target, so backtrack.
        for i in range(len(ans) - 1, -1, -1):
            prev = ord(ans[i]) - ord('a')
            count[prev] += 1

            x = ord(target[i]) - ord('a')

            for c in range(x + 1, 26):
                if count[c] > 0:
                    result = ans[:i] + [chr(c + ord('a'))]
                    count[c] -= 1

                    for j in range(26):
                        result.extend(chr(j + ord('a')) * count[j])

                    return ''.join(result)

        return ""