---
id: basic
title: Tutorial On RISC V 
sidebar_label: Tutorial On RISC V
---

## Simulator

* I'll be using [Rars](https://github.com/TheThirdOne/rars), also see description of system calls [here](https://github.com/TheThirdOne/rars/wiki/Environment-Calls). It as well have a nice companion [documentation](https://github.com/TheThirdOne/rars/wiki) to understand more about risc v, it is expected that one has given it a read.

* Can try [Venus](http://www.kvakil.me/venus/), Github repo: https://github.com/kvakil/venus. Note that for system calls, their argument register is different, see [this](https://github.com/TheThirdOne/rars/issues/45). 

* Can use spike, installed when using `riscv-gnu-toolchain`. Note it was as well required to install [pk](https://github.com/riscv/riscv-pk). System calls are different than RARS, basically it follows linux system calls. Can see these system calls [here1](https://github.com/riscv/riscv-pk/blob/master/pk/syscall.c), and [here2](https://github.com/riscv/riscv-pk/blob/master/pk/syscall.h). And linux system calls [here](http://man7.org/linux/man-pages/man2/syscalls.2.html), note system calls of interest can be concisely seen [here](https://rv8.io/syscalls.html).
  
  So to compile and run the program, do: (Don't know if this is the intended way but after a lot of trial and error, I found this)
  ```
  riscv64-unknown-elf-as -o filename.o filename.s 
  riscv64-unknown-elf-ld -o filename filename.o 
  spike pk filename
  ```

## Examples

* Note that dont use `$reg`, instead simply use `reg`.
* Always have two sections, one for data and another for text.
* During `ecall` all registers besides the output are guaranteed not to change.

### Hello Word

```asm
.data

msg: .string "hello world"

.text

start:
  li a7, 4
  la a0, msg
  ecall
  li a7, 10
  ecall
```

To get the same code working using spike. 

```asm
.globl _start # We must need to give _start, .globl helps to see it outside this file
.data # Tell the assembler we are defining data not code
str:  # Label this position in memory so it can be referred to in our code 
  .string "Hello World!\n" # Copy the string "Hello World!\n" into memory 

.text # Tell the assembler that we are writing code (text) now 
_start: # Make a label to say where our program should start from

  li a0, 1   # li means to Load Immediate and we want to load the value 1 into register a0
  la a1, str # la is similar to li, but works for loading addresses
  li a2, 13  # like the first line, but with 13. This is the final argument to the system call
  li a7, 64  # a7 is what determines which system call we are calling and we what to call write (64)
  ecall      # actually issue the call

  li a0, 0   # The exit code we will be returning is 0
  li a7, 93  # Again we need to indicate what system call we are making and this time we are calling exit(93)
  ecall 
```

### Fibonacci

```asm
.globl _start

.data
  msg1: .string "Please enter a number: "
  msg2: .string "The "
  msg3: .string " fibonnaci number is: "

.text

_start:
  # Initial 2 fibs
  li t0, 0
  li t1, 1
  # prints msg1
  la a0, msg1
  li a7, 4
  ecall
  # reads an int and moves it to register t3
  li a7, 5
  ecall
  mv t3, a0
  # prints a newline character
  li a7, 11
  li a0, '\n'
  ecall
  # prints msg2
  la a0, msg2
  li a7, 4
  ecall
  # prints the int value in t3
  mv a0, t3
  li a7, 1
  ecall
  # fibonnaci program
fib:
  beq t3, zero, finish
  add t2, t1, t0
  mv t0, t1
  mv t1, t2
  addi t3, t3, -1
  j fib
finish:
  # prints msg3
  la a0, msg3
  li a7, 4
  ecall
  # prints the result in t0
  mv a0, t0
  li a7, 1
  ecall
  # prints a newline
  li a0, '\n'
  li a7, 11
  ecall
  # ends the program with status code 0
  li a7, 10
  ecall
```

### Saving callee save registers 

```asm
.data

  bef: .string "Before modification, value is: "
  dur: .string "\nInside function, value is: "
  aft: .string "\nAfter function call, value is: "

.text 

main:
  addi s0, zero, 1
  # Print bef
  la a0, bef
  li a7, 4
  ecall
  # Print int
  li a7, 1
  mv a0, s0
  ecall
  jal increment
  # Print aft
  la a0, aft
  li a7, 4
  ecall
  # Print int
  li a7, 1
  mv a0, s0
  ecall
  # Exit
  li a7, 10
  ecall



increment:
  addi sp, sp, -4
  sw s0, 0(sp) # '0' denotes the offset
  addi s0, s0, 1
  # Print string
  la a0, dur
  li a7, 4
  ecall
  # Print the incremented integer
  mv a0, s0
  li a7, 1
  ecall
  lw s0, 0(sp)
  addi sp, sp, 4
  jr ra
```

### String comparison

```asm
.data 

  str1: .string "sourabh"
  str2: .string "saurabh"
  str3: .string "sourabz"
  str4: .string "sourabh"
  
.text 

main: 
  la a0, str1 
  la a1, str2 
  jal strcmp
  # Print int
  li a7, 1
  ecall
  la a0, str1 
  la a1, str3 
  jal strcmp 
  # Print int
  li a7, 1
  ecall
  la a0, str1 
  la a1, str4 
  jal strcmp 
  # Print int
  li a7, 1
  ecall
  # Exit
  li a7, 10
  ecall

strcmp:
  strcmptest:
    lb a2 (a0)
    lb a3 (a1)
    beq a2, zero, strcmpend
    beq a3, zero, strcmpend
    bgt a2, a3  strcmpgreat
    blt a2, a3  strcmpless
    addi a0, a0, 1
    addi a1, a1, 1
    j strcmptest
  strcmpgreat:
    li a0, 1
    jr ra
  strcmpless:
    li a0, -1
    jr ra
  strcmpend:
    bne a2 zero strcmpgreat
    bne a3 zero strcmpless
    li a0, 0
    jr ra
```