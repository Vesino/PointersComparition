package main

import "fmt"

// A pointer in go is a value that represents the memory address of another value

// The parameter of the function is a pointer to int
func pointerDemo(x *int) {
	fmt.Println("Before the assignment: *x =", *x, ", x = ", x)
	*x = 8 // pointer indirection allow
	fmt.Println("After the assignment: *x =", *x, ", x = ", x)
}

func main() {
	n := 1  // it is not possible to take the address of literal value n := &1
	x := &n // this is the address of n
	fmt.Println("Before the call: *x =", *x, ", x = ", x)
	pointerDemo(x)
	fmt.Println("After the call: *x =", *x, ", x = ", x)
}
