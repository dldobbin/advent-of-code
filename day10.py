input = [
144,
10,
75,
3,
36,
80,
143,
59,
111,
133,
1,
112,
23,
62,
101,
137,
41,
24,
8,
121,
35,
105,
161,
69,
52,
21,
55,
29,
135,
142,
38,
108,
141,
115,
68,
7,
98,
82,
9,
72,
118,
27,
153,
140,
61,
90,
158,
102,
28,
134,
91,
2,
17,
81,
31,
15,
120,
20,
34,
56,
4,
44,
74,
14,
147,
11,
49,
128,
16,
99,
66,
47,
125,
155,
130,
37,
67,
54,
60,
48,
136,
89,
119,
154,
122,
129,
163,
73,
100,
85,
95,
30,
76,
162,
22,
79,
88,
150,
53,
63,
92
]

countCache = {}

def count(fromAdapter, toAdapter, adapters):
	if (fromAdapter, toAdapter) in countCache:
		return countCache[(fromAdapter, toAdapter)]

	if (fromAdapter > toAdapter):
		return 0
	if fromAdapter == toAdapter:
		countCache[(fromAdapter, toAdapter)] = 1
		return 1
	nextAdapters = [a for a in adapters if 0 < a-fromAdapter <= 3]
	res = sum([count(a, toAdapter, [x for x in adapters if x > a]) for a in nextAdapters])
	countCache[(fromAdapter, toAdapter)] = res
	return res

if __name__ == '__main__':
	ads = sorted(input)
	fromAds = [0] + ads
	toAds = ads + [ads[-1]+3]
	diffs = [t-f for t,f in zip(toAds,fromAds)]
	print("Part 1: ", diffs.count(1) * diffs.count(3))
	print("Part 2: ", count(0, ads[-1]+3, toAds))