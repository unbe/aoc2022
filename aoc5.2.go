package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func Dup[T any](src []T) []T {
    dup := make([]T, len(src))
    copy(dup, src)
    return dup
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
		cnt, _ := strconv.Atoi(move_match[1])
		from, _ := strconv.Atoi(move_match[2])
		to, _ := strconv.Atoi(move_match[3])
		from -= 1
		to -= 1
		stacks[to] = append(Dup(stacks[from][:cnt]), stacks[to]...)
		stacks[from] = stacks[from][cnt:]
	}
  }
  for _, stack := range stacks {
	  fmt.Printf("%s", stack[0])
  }
}
