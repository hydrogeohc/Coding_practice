# [LeetCode](https://leetcode.com/)

* Notes: "🔒" means [LeetCode premium membership].

## Solutions
- [0001 - 1000](./0001-1000.md)

## Algorithms

* [Queue](https://github.com/hydrogeohc/Coding_practice#queue)
* [Recursion](https://github.com/hydrogeohc/Coding_practice#recursion)
* [Binary Search Tree](https://github.com/hydrogeohc/Coding_practice#binary-search-tree)



## Reference


* Python
    * [Time Complexity](https://wiki.python.org/moin/TimeComplexity)
* Algorithms
    * [Rosetta Code](https://rosettacode.org)
    * [CP-Algorithms](https://cp-algorithms.com)
    * [KACTL](https://github.com/kth-competitive-programming/kactl)
    * [Codeforces](https://codeforces.com/)
* Math
    * [Stack Exchange](https://math.stackexchange.com)     
* Visualization
    * [VisuAlgo](https://visualgo.net/en)
    * [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
    * [Algorithm Visualizer](https://algorithm-visualizer.org/)
 as follows:

| n | Complexity | Possible Algorithms & Techniques |
| - | - | - |
| 10<sup>18</sup>+ | _O(1)_ | Math |
| 10<sup>18</sup> | _O(logn)_ | Binary & Ternary Search / Matrix Power / Cycle Tricks / Big Simulation Steps / Values Reranking / Math |
| 10<sup>16</sup> | _O(n<sup>1/2</sup>)_ | Math |
| 10<sup>8</sup> | _O(n)_ | Greedy / Ad-hoc / DP |
| 4×10<sup>7</sup> | _O(nlogn)_ | Linear # Calls to Binary & Ternary Search / Pre-processing & Querying / Divide and Conquer |
| 10<sup>4</sup> | _O(n<sup>2</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 500 | _O(n<sup>3</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound  |
| 90 | _O(n<sup>4</sup>)_ | Ad-hoc / DP / Greedy / Divide and Conquer / Branch and Bound |
| 50 | _O(n<sup>5</sup>)_ | Branch and Bound |
| 40 | _O(nx2<sup>n/2</sup>)_ | 	Meet in the Middle |
| 20 | _O(n×2<sup>n</sup>)_ | Backtracking / Generating 2<sup>n</sup> Subsets / Bitmask Technique |
| 11 | _O(n!)_ | Factorial / Permutation / Combination Algorithm |

## String
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
0005 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) |[Python](./Python/longest-palindromic-substring.py) | _O(n)_ | _O(n)_ |  Medium || `Manacher's Algorithm`
0006 | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) |[Python](./Python/zigzag-conversion.py) | _O(n)_ | _O(1)_        | Easy           ||
0008 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) |[Python](./Python/string-to-integer-atoi.py) | _O(n)_ | _O(1)_ | Easy      ||
0014 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |[Python](./Python/longest-common-prefix.py) | _O(n * k)_   | _O(1)_  | Easy           ||
0028 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) |[Python](./Python/implement-strstr.py) | _O(n + k)_   | _O(k)_  | Easy           || `KMP Algorithm`
0038 | [Count and Say](https://leetcode.com/problems/count-and-say/) |[Python](./Python/count-and-say.py)| _O(n * 2^n)_  | _O(2^n)_        | Easy           ||
0043 | [Multiply Strings](https://leetcode.com/problems/multiply-strings/) |[Python](./Python/multiply-strings.py) | _O(m * n)_ | _O(m + n)_  | Medium         ||
0058 | [Length of Last Word](https://leetcode.com/problems/length-of-last-word/) |[Python](./Python/length-of-last-word.py) | _O(n)_   | _O(1)_  | Easy           ||
0067 | [Add Binary](https://leetcode.com/problems/add-binary/)    |[Python](./Python/add-binary.py) | _O(n)_          | _O(1)_          | Easy           ||
0068 | [Text Justification](https://leetcode.com/problems/text-justification/) |[Python](./Python/text-justification.py) | _O(n)_ | _O(1)_      | Hard           ||
0125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |[Python](./Python/valid-palindrome.py) | _O(n)_  | _O(1)_         | Easy           ||
0151 | [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) |[Python](./Python/reverse-words-in-a-string.py) | _O(n)_ | _O(1)_ | Medium         ||
0161 | [One Edit Distance](https://leetcode.com/problems/one-edit-distance/) |[Python](./Python/one-edit-distance.py) | _O(m + n)_ | _O(1)_    | Medium         |🔒 |
0165 | [Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/) |[Python](./Python/compare-version-numbers.py) | _O(n)_ | _O(1)_ | Easy     ||
0186 | [Reverse Words in a String II](https://leetcode.com/problems/reverse-words-in-a-string-ii/) |[Python](./Python/reverse-words-in-a-string-ii.py) | _O(n)_ | _O(1)_ | Medium         | 🔒 |
0214 | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) |[Python](./Python/shortest-palindrome.py) | _O(n)_ | _O(n)_ |  Hard || `KMP Algorithm`, `Manacher's Algorithm`
0242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/)|[Python](./Python/valid-anagram.py) | _O(n)_       | _O(1)_         | Easy         | LintCode |
0271 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) |[Python](./Python/encode-and-decode-strings.py) | _O(n)_ | _O(1)_ | Medium         | 🔒 |
0273 | [Integer to English Words](https://leetcode.com/problems/integer-to-english-words/) |[Python](./Python/integer-to-english-words.py) | _O(1)_ | _O(1)_ | Hard         | |
0306 | [Addictive Number](https://leetcode.com/problems/additive-number/) |[Python](./Python/additive-number.py) | _O(n^3)_ | _O(n)_ | Medium         | |
0383 | [Ransom Note](https://leetcode.com/problems/ransom-note/) |[Python](./Python/ransom-note.py) | _O(n)_ | _O(1)_ | Easy         | EPI |
0405 | [Convert a Number to Hexadecimal](https://leetcode.com/problems/convert-a-number-to-hexadecimal/) |[Python](./Python/convert-a-number-to-hexadecimal.py) | _O(n)_ | _O(1)_ | Easy         | |
0408 | [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation/) |[Python](./Python/valid-word-abbreviation.py) | _O(n)_ | _O(1)_ | Easy         | 🔒 |
0415 | [Add Strings](https://leetcode.com/problems/add-strings/) |[Python](./Python/add-strings.py) | _O(n)_ | _O(1)_ | Easy         | |
0420 | [Strong Password Checker](https://leetcode.com/problems/strong-password-checker/) |[Python](./Python/strong-password-checker.py) | _O(n)_ | _O(1)_ | Hard         | |
0434 | [Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/) |[Python](./Python/number-of-segments-in-a-string.py) | _O(n)_ | _O(1)_ | Easy         | |
0443 | [String Compression](https://leetcode.com/problems/string-compression/) |[Python](./Python/string-compression.py) | _O(n)_ | _O(1)_ | Easy         | |
0459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) |[Python](./Python/repeated-substring-pattern.py) | _O(n)_ | _O(n)_ | Easy         || `KMP Algorithm` |
0468 | [Validate IP Address](https://leetcode.com/problems/validate-ip-address/) |[Python](./Python/validate-ip-address.py) | _O(1)_ | _O(1)_ | Medium         | |
0481 | [Magical String](https://leetcode.com/problems/magical-string/) |[Python](./Python/magical-string.py) | _O(n)_       | _O(n)_          | Medium         || String |
0482 | [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) |[Python](./Python/license-key-formatting.py) | _O(n)_ | _O(1)_ | Easy | |
0500 | [Keyboard Row](https://leetcode.com/problems/keyboard-row/) |[Python](./Python/keyboard-row.py) | _O(n)_       | _O(1)_          | Easy         || String, Hash |
0520 | [Detect Capital](https://leetcode.com/problems/detect-capital/) |[Python](./Python/detect-capital.py) | _O(l)_ | _O(1)_ | Easy         | |
0521 | [Longest Uncommon Subsequence I](https://leetcode.com/problems/longest-uncommon-subsequence-i/) |[Python](./Python/longest-uncommon-subsequence-i.py) | _O(min(a, b))_ | _O(1)_ | Easy         | |
0522 | [Longest Uncommon Subsequence II](https://leetcode.com/problems/longest-uncommon-subsequence-ii/) |[Python](./Python/longest-uncommon-subsequence-ii.py) | _O(l * n^2)_ | _O(1)_ | Medium         | | Sort
0524 | [Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/) |[Python](./Python/longest-word-in-dictionary-through-deleting.py) | _O((d * l)  * logd)_ | _O(1)_ | Medium         | | Sort
0527 | [Word Abbreviation](https://leetcode.com/problems/word-abbreviation/) |[Python](./Python/word-abbreviation.py) | _O(n * l)_ ~ _O(n^2 * l^2)_  | _O(n * l)_ | Hard         |🔒|
0539 | [Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) |[Python](./Python/minimum-time-difference.py) | _O(nlogn)_ | _O(n)_ | Medium         | |
0541 | [Reverse String II](https://leetcode.com/problems/reverse-string-ii/) |[Python](./Python/reverse-string-ii.py) | _O(n)_ | _O(1)_ | Easy         | |
0551 | [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/) |[Python](./Python/student-attendance-record-i.py) | _O(n)_ | _O(1)_ | Easy |||
0555 | [Split Concatenated Strings](https://leetcode.com/problems/split-concatenated-strings/) |[Python](./Python/split-concatenated-strings.py) | _O(n^2)_       | _O(n)_          | Medium         || String |
0556 | [Next Greater Element III](https://leetcode.com/problems/next-greater-element-iii/) |[Python](./Python/next-greater-element-iii.py) | _O(1)_ | _O(1)_ | Medium         | |
0557 | [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/) |[Python](./Python/reverse-words-in-a-string-iii.py) | _O(n)_ | _O(1)_ | Easy         | |
0564 | [Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/) |[Python](./Python/find-the-closest-palindrome.py) | _O(l)_ | _O(l)_ | Hard         | |
0591 | [Tag Validator](https://leetcode.com/problems/tag-validator/) |[Python](./Python/tag-validator.py) | _O(n)_ | _O(n)_ | Hard         | |
0616 | [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) |[Python](./Python/add-bold-tag-in-string.py) | _O(n * d * l)_ | _O(n)_ |  Medium | 🔒 |
0647 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) |[Python](./Python/palindromic-substrings.py) | _O(n)_ | _O(n)_ |  Medium || `Manacher's Algorithm`
0648 | [Replace Words](https://leetcode.com/problems/replace-words/) |[Python](./Python/replace-words.py) | _O(n)_ | _O(t)_ | Medium         || Trie |
0657 | [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin/) |[Python](./Python/robot-return-to-origin.py) | _O(n)_ | _O(1)_ | Easy         | |
0678 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) |[Python](./Python/valid-parenthesis-string.py) | _O(n)_ | _O(1)_ | Medium         | |
0680 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) |[Python](./Python/valid-palindrome-ii.py) | _O(n)_  | _O(1)_         | Easy           ||
0681 | [Next Closest Time](https://leetcode.com/problems/next-closest-time/) |[Python](./Python/next-closest-time.py) | _O(1)_  | _O(1)_         | Medium           ||
0686 | [Repeated String Match](https://leetcode.com/problems/repeated-string-match/) |[Python](./Python/repeated-string-match.py) | _O(n + m)_ | _O(1)_ | Easy || `Rabin-Karp Algorithm` |
0696 | [Count Binary Substrings](https://leetcode.com/problems/count-binary-substrings/) |[Python](./Python/count-binary-substrings.py) | _O(n)_ | _O(1)_ | Easy||
0709 | [To Lower Case](https://leetcode.com/problems/to-lower-case/) |[Python](./Python/to-lower-case.py) | _O(n)_       | _O(1)_          | Easy         || String |
0720 | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) |[Python](./Python/longest-word-in-dictionary.py) | _O(n)_ | _O(t)_ | Easy         || Trie |
0722 | [Remove Comments](https://leetcode.com/problems/remove-comments/) |[Python](./Python/remove-comments.py) | _O(n)_ | _O(k)_ | Medium         |||
0751 | [IP to CIDR](https://leetcode.com/problems/ip-to-cidr/) |[Python](./Python/ip-to-cidr.py) | _O(n)_ | _O(1)_ | Medium         |||
0758 | [Bold Words in String](https://leetcode.com/contest/weekly-contest-66/problems/bold-words-in-string/) |[Python](./Python/bold-words-in-string.py) | _O(n * l)_ | _O(t)_ |  Easy | 🔒, variant of [Add Bold Tag in String](https://leetcode.com/problems/add-bold-tag-in-string/) |
0791 | [Custom Sort String](https://leetcode.com/problems/custom-sort-string/) |[Python](./Python/custom-sort-string.py) | _O(n)_ | _O(1)_ | Medium         |||
0796 | [Rotate String](https://leetcode.com/problems/rotate-string/) |[Python](./Python/rotate-string.py) | _O(n)_ | _O(1)_ | Easy         || `KMP Algorithm`, `Rabin-Karp Algorithm` |
0804 | [Unique Morse Code Words](https://leetcode.com/problems/unique-morse-code-words/) |[Python](./Python/unique-morse-code-words.py) | _O(n)_ | _O(n)_ | Easy         |||
0806 | [Number of Lines To Write String](https://leetcode.com/problems/number-of-lines-to-write-string/) |[Python](./Python/number-of-lines-to-write-string.py) | _O(n)_ | _O(1)_ | Easy         |||
0809 | [Expressive Words](https://leetcode.com/problems/expressive-words/) |[Python](./Python/expressive-words.py) | _O(n + s)_ | _O(l + s)_ | Medium         |||
0816 | [Ambiguous Coordinates](https://leetcode.com/problems/ambiguous-coordinates/) |[Python](./Python/ambiguous-coordinates.py) | _O(n^4)_ | _O(n)_ | Medium         |||
0819 | [Most Common Word](https://leetcode.com/problems/most-common-word/) |[Python](./Python/most-common-word.py) | _O(m + n)_ | _O(m + n)_ | Easy         |||
0820 | [Short Encoding of Words](https://leetcode.com/problems/short-encoding-of-words/) |[Python](./Python/short-encoding-of-words.py) | _O(n)_ | _O(t)_ | Medium         || Trie |
0824 | [Goat Latin](https://leetcode.com/problems/goat-latin/) |[Python](./Python/goat-latin.py) | _O(n + w^2)_ | _O(l)_ | Easy         |||
0831 | [Masking Personal Information](https://leetcode.com/problems/masking-personal-information/) |[Python](./Python/masking-personal-information.py) | _O(1)_ | _O(1)_ | Medium         |||
0833 | [Find And Replace in String](https://leetcode.com/problems/find-and-replace-in-string/) |[Python](./Python/find-and-replace-in-string.py) | _O(n + m)_ | _O(n)_ | Medium         |||
0839 | [Similar String Groups](https://leetcode.com/problems/similar-string-groups/) |[Python](./Python/similar-string-groups.py) | _O(n^2 * l)_ | _O(n)_ | Hard || Union Find
0848 | [Shifting Letters](https://leetcode.com/problems/shifting-letters/) |[Python](./Python/shifting-letters.py) | _O(n)_ | _O(1)_ | Medium ||
0859 | [Buddy Strings](https://leetcode.com/problems/buddy-strings/) |[Python](./Python/buddy-strings.py) | _O(n)_ | _O(1)_ | Easy ||
0880 | [Decoded String at Index](https://leetcode.com/problems/decoded-string-at-index/) |[Python](./Python/decoded-string-at-index.py) | _O(n)_ | _O(1)_ | Medium ||
0884 | [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/) |[Python](./Python/uncommon-words-from-two-sentences.py) | _O(m + n)_ | _O(m + n)_ | Easy ||
0890 | [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/) |[Python](./Python/find-and-replace-pattern.py) | _O(n * l)_ | _O(1)_ | Medium ||
0893 | [Groups of Special-Equivalent Strings](https://leetcode.com/problems/groups-of-special-equivalent-strings/) |[Python](./Python/groups-of-special-equivalent-strings.py) | _O(n * l)_ | _O(n)_ | Easy ||
0916 | [Word Subsets](https://leetcode.com/problems/word-subsets/) |[Python](./Python/word-subsets.py) | _O(m + n)_ | _O(1)_ | Medium ||
0917 | [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/) |[Python](./Python/reverse-only-letters.py) | _O(n)_ | _O(1)_ | Easy ||
0925 | [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/) |[Python](./Python/long-pressed-name.py) | _O(n)_ | _O(1)_ | Easy ||
0929 | [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/) |[Python](./Python/unique-email-addresses.py) | _O(n * l)_ | _O(n * l)_ | Easy ||
0939 | [Minimum Area Rectangle](https://leetcode.com/problems/minimum-area-rectangle/) |[Python](./Python/minimum-area-rectangle.py) | _O(n^1.5)_ on average | _O(n)_ | Medium ||
0942 | [DI String Match](https://leetcode.com/problems/di-string-match/) |[Python](./Python/di-string-match.py) | _O(n)_ | _O(1)_      | Easy         ||
0944 | [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/) |[Python](./Python/delete-columns-to-make-sorted.py) | _O(n * l)_ | _O(1)_      | Medium         ||
0953 | [Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/) |[Python](./Python/verifying-an-alien-dictionary.py) | _O(n * l)_ | _O(1)_      | Easy         ||
0955 | [Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii/) |[Python](./Python/delete-columns-to-make-sorted-ii.py) | _O(n * l)_ | _O(n)_      | Medium         ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>


## Queue
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
1424 | [Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)| [Python](./Python/diagonal-traverse-ii.py) | _O(m * n)_        | _O(m)_          | Medium           |||
1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/)| [Python](./Python/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit.py) | _O(n)_        | _O(n)_          | Hard           | | Mono Deque |
1499 | [Max Value of Equation](https://leetcode.com/problems/max-value-of-equation/)| [Python](./Python/max-value-of-equation.py) | _O(n)_        | _O(n)_          | Hard           | | Mono Deque |
1696 | [Jump Game VI](https://leetcode.com/problems/jump-game-vi/) | [Python](./Python/jump-game-vi.py) | _O(n)_ | _O(k)_ | Medium | | Mono Deque, Sliding Window |

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>


## Recursion
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
1106 | [Parsing A Boolean Expression](https://leetcode.com/problems/parsing-a-boolean-expression/) | [Python](./Python/parsing-a-boolean-expression.py) | _O(n)_          | _O(n)_          | Hard           ||

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>


## Binary Search Tree
|  #  | Title           |  Solution       |  Time           | Space           | Difficulty    | Tag          | Note| 
|-----|---------------- | --------------- | --------------- | --------------- | ------------- |--------------|-----|
1373 | [Maximum Sum BST in Binary Tree](https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/) |  [Python](./Python/maximum-sum-bst-in-binary-tree.py) | _O(n)_          | _O(h)_          | Hard           || DFS, Stack |
1382 | [Balance a Binary Search Tree](https://leetcode.com/problems/balance-a-binary-search-tree/) |  [Python](./Python/balance-a-binary-search-tree.py) | _O(n)_          | _O(h)_          | Medium           || DFS, Stack |
1902 | [Depth of BST Given Insertion Order](https://depth-of-bst-given-insertion-order/)|  [Python](./Python/depth-of-bst-given-insertion-order.py)   | _O(nlogn)_          | _O(n)_          | Medium         | 🔒 | Sorted Dict |
1932 | [Merge BSTs to Create Single BST](https://leetcode.com/problems/merge-bsts-to-create-single-bst/)|[Python](./Python/merge-bsts-to-create-single-bst.py) | _O(n)_      | _O(n)_          | Hard         | | BST, BFS

<br/>
<div align="right">
    <b><a href="#algorithms">⬆️ Back to Top</a></b>
</div>
<br/>

