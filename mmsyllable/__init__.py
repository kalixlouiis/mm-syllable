"""
MM-Syllable: A lightweight, rule-based Burmese syllable tokenizer.
"""

import re

class SyllableBreaker:
    def __init__(self):
        # Burmese character ranges and special symbols
        self._consonant_block = 'က-အ'
        self._special_chars = 'ဣဤဥဦဧဩဪဿ၌၍၏၀-၉၊။!-/:-@[-`{-~\\s.,'
        
        # Suffixes that should be merged with the preceding syllable
        self._sticky_suffixes = {'င့်', 'ည့်', 'န့်', 'မ့်', 'ယ့်'}

    def split(self, text: str) -> list:
        """
        Main method to break a Burmese string into syllables.
        """
        if not text:
            return []

        # 1. Primary breaking logic using Lookbehind and Lookahead
        # Inserts a space before consonants (not preceded by a Virama) and other symbols
        pattern = f"(?<![္])([{self._consonant_block}])(?![်္])|([{self._special_chars}])"
        segmented = re.sub(pattern, r" \1\2", text).strip()

        # 2. Handle alphanumeric transitions
        # Ensures spaces between Burmese script and English/numbers
        segmented = re.sub(r'(?<=[က-ၴ])([a-zA-Z0-9])', r' \1', segmented)
        
        # 3. Clean up number grouping
        segmented = re.sub(r'([0-9၀-၉])\s+([0-9၀-၉])\s*', r'\1\2 ', segmented)
        segmented = re.sub(r'([0-9၀-၉])\s+(\+)', r'\1 \2 ', segmented)

        raw_tokens = segmented.split()
        return self._recombine_components(raw_tokens)

    def _recombine_components(self, tokens: list) -> list:
        """
        Internal logic to fix over-segmented syllables like 'င့်' or 'ဿ'
        """
        final_list = []
        idx = 0
        limit = len(tokens)

        while idx < limit:
            current_unit = tokens[idx]
            
            # Check if there is a next token to merge with
            if idx + 1 < limit:
                next_unit = tokens[idx + 1]

                # Condition A: Merging common grammatical suffixes
                if next_unit in self._sticky_suffixes:
                    final_list.append(current_unit + next_unit)
                    idx += 2
                    continue
                
                # Condition B: Handling stacked characters
                if next_unit.startswith('ဿ'):
                    final_list.append(current_unit + next_unit)
                    idx += 2
                    continue

            final_list.append(current_unit)
            idx += 1

        return final_list

# Easy access alias
def tokenize(text):
    return SyllableBreaker().split(text)
