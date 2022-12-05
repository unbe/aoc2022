package main

import (
	"bufio"
	"fmt"
	"encoding/json"
	"os"
	"regexp"
	"strconv"
)

func Reverse(input []string) []string {
    var output []string

    for i := len(input) - 1; i >= 0; i-- {
        output = append(output, input[i])
    }

    return output
}

func main() {
  scanner := bufio.NewScanner(os.Stdin)
  stack_re := regexp.MustCompile(`\[(\w)\]|   ( |$)`)
  move_re := regexp.MustCompile(`move (\d+) from (\d+) to (\d+)`)

  var stacks [][]string
  for scanner.Scan() {
	line := scanner.Text()
	stack_match := stack_re.FindAllStringSubmatch(line, -1)
	if stack_match != nil {
		for idx, groups := range stack_match {
			if groups[1] != "" {
				for len(stacks) <= idx {
					stacks = append(stacks, nil)
				}
				stacks[idx] = append(stacks[idx], groups[1])
			}
		}
	}
	move_match := move_re.FindStringSubmatch(line)
	if move_match != nil {
		fmt.Printf("move: %v\n", move_match)
		b, _ := json.Marshal(move_match)
		fmt.Printf("move: %v\n", string(b))
		cnt, _ := strconv.Atoi(move_match[1])
		from, _ := strconv.Atoi(move_match[2])
		to, _ := strconv.Atoi(move_match[3])
		from -= 1
		to -= 1
		fmt.Printf("move: %d %d -> %d\n", cnt, from, to)
		b, _ = json.Marshal(stacks)
		fmt.Printf("stacks: %v\n", string(b))
		stacks[to] = append(Reverse(stacks[from][:cnt]), stacks[to]...)
		stacks[from] = stacks[from][cnt:]
		b, _ = json.Marshal(stacks)
		fmt.Printf("stacks: %v\n", string(b))
	}
  }
  for _, stack := range stacks {
	  fmt.Printf("%s", stack[0])
  }
  b, _ := json.Marshal(stacks)
  fmt.Printf("\nstacks: %v\n", string(b))
}
