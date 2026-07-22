class Solution:
    def longestCommonPrefix(self, strs):
        
        # If the list is empty, return an empty string
        if not strs:
            return ""

        # Take the first string as the reference
        first = strs[0]

        # Check each character of the first string
        for i in range(len(first)):

            # Current character
            current = first[i]

            # Compare with every other string
            for j in range(1, len(strs)):

                # If the current string is shorter
                # OR the character is different
                if i >= len(strs[j]) or strs[j][i] != current:
                    # Return the common prefix found so far
                    return first[:i]

        # If no mismatch is found,
        # the whole first string is the common prefix
        return first