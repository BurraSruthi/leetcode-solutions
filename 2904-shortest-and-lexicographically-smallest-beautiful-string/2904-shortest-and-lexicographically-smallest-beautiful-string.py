class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        count = 0
        left = 0
        stack = []

        for right in range(n):

            if s[right] == '1':
                count += 1

            # We have exactly k ones
            if count == k:

                # Shrink from the left while the first character is 0
                while s[left] == '0':
                    left += 1

                # Store the current valid substring
                stack.append(s[left:right + 1])

                # Move left past the first 1
                left += 1
                count -= 1

        if not stack:
            return ""

        # Shortest length first, then lexicographically smallest
        stack.sort(key=lambda x: (len(x), x))

        return stack[0]