package main

func main() {
	test1()
}

func test1() {
	println(1 == 1)

	//stack := []int{9,9,9,9,9}
	//
	//for i, val := range stack {
	//	println(i, val)
	//}

	ss := "aaa"
	hashmap := map[byte]byte{}

	for i := range ss {
		x := ss[i]
		hashmap[x] = x
	}


}


// 一个很好的教学模板
func groupAnagrams(strs []string) [][]string {

	hashmap := map[[26]int][]string{}

	// 不用的index变量，就用_表示，因为不用的话会报错
	for _, str := range strs {
		cnt := [26]int{}
		for _, char := range str {
			// 这里ord相减，只能使用单引号
			cnt[char - 'a'] ++
		}

		hashmap[cnt] = append(hashmap[cnt], str)
	}

	res := [][]string{}
	for _, val := range hashmap {
		res = append(res, val)
	}

	return res

}