from test_framework import generic_test

def valid_ip_num(s):
	i = int(s)
	return (0 <= i < 256) and (str(i) == s)


def helper(s, lvl):
	n = len(s)
	if (not n) or (n > 3 * (4-lvl)):
		return []
	if lvl == 3:
		if valid_ip_num(s):
			return [s]
	ans = []
	for i in range(1, n):
		prefix = s[:i]
		if valid_ip_num(prefix):
			suffix = s[i:]
			if suffix:
				sub = helper(suffix, lvl+1)
				for p in sub:
					ans.append(f'{prefix}.{p}')
	return ans


def get_valid_ip_address(s):
	return helper(s, 0)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
