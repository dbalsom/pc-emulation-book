# Undefined Flags on the 8088

## The 8088 FLAGS Register 

As a quick-reference, here is the layout of the 8088's `FLAGS` register:

| Bit  | 15  | 14  | 13  | 12  | 11  | 10  |  9  |  8  |  7  |  6  |  5  |  4  |  3  |  2  |  1  |  0  |
| ---- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Flag |  1  |  1  |  1  |  1  | OF  | DF  | IF  | TF  | SF  | ZF  |  0  | AF  |  0  | PF  |  1  | CF  |

| Flag | Meaning          |
| ---- | ---------------- |
| OF   | Overflow         |
| DF   | Direction        |
| IF   | Interrupt enable |
| TF   | Trap             |
| SF   | Sign             |
| ZF   | Zero             |
| AF   | Auxiliary carry  |
| PF   | Parity           |
| CF   | Carry            |

As a shorthand, we can pack flags except for `TF` into an ASCII string, as `odiszapc`. 

Periods can substitute for individual letters to indicate that flag is unset. For example, if only the carry flag is set in the `FLAGS` register, we can indicate such as `.......c`.

## What does 'undefined' mean?

Several instructions in the 8088 ISA are described by Intel as leaving certain flags in an *undefined* state after completion. In practice, the CPU sets all flags to a deterministic state. Intel's choice of defining certain flags as *undefined* may reflect a lack of useful meaning for that flag after an operation, but the strict definition is a lack of any guarantees that future CPU models in the x86 family will produce the same undefined flag values. And in fact, undefined flag behavior does vary between the 8088 and 80286.

## Undefined Flag Table

Below is a table of all instructions that leave flags undefined on the 8088, and a short ASCII field indicating which flags are left undefined.

| Opcode  | Mnemonic | Flags      |
| ------- | -------- | ---------- |
| `08`    | OR       | `.....a..` |
| `09`    | OR       | `.....a..` |
| `0A`    | OR       | `.....a..` |
| `0B`    | OR       | `.....a..` |
| `0C`    | OR       | `.....a..` |
| `0D`    | OR       | `.....a..` |
| `20`    | AND      | `.....a..` |
| `21`    | AND      | `.....a..` |
| `22`    | AND      | `.....a..` |
| `23`    | AND      | `.....a..` |
| `24`    | AND      | `.....a..` |
| `25`    | AND      | `.....a..` |
| `27`    | DAA      | `o.......` |
| `2F`    | DAS      | `o.......` |
| `30`    | XOR      | `.....a..` |
| `31`    | XOR      | `.....a..` |
| `32`    | XOR      | `.....a..` |
| `33`    | XOR      | `.....a..` |
| `34`    | XOR      | `.....a..` |
| `35`    | XOR      | `.....a..` |
| `37`    | AAA      | `o..sz.p.` |
| `3F`    | AAS      | `o..sz.p.` |
| `80 /1` | OR       | `.....a..` |
| `80 /4` | AND      | `.....a..` |
| `80 /6` | XOR      | `.....a..` |
| `81 /1` | OR       | `.....a..` |
| `81 /4` | AND      | `.....a..` |
| `81 /6` | XOR      | `.....a..` |
| `82 /1` | OR       | `.....a..` |
| `82 /4` | AND      | `.....a..` |
| `82 /6` | XOR      | `.....a..` |
| `83 /1` | OR       | `.....a..` |
| `83 /4` | AND      | `.....a..` |
| `83 /6` | XOR      | `.....a..` |
| `84`    | TEST     | `.....a..` |
| `85`    | TEST     | `.....a..` |
| `A8`    | TEST     | `.....a..` |
| `A9`    | TEST     | `.....a..` |
| `D0 /4` | SHL      | `.....a..` |
| `D0 /5` | SHR      | `.....a..` |
| `D0 /6` | SETMO    | `o..szapc` |
| `D0 /7` | SAR      | `.....a..` |
| `D1 /4` | SHL      | `.....a..` |
| `D1 /5` | SHR      | `.....a..` |
| `D1 /6` | SETMO    | `o..szapc` |
| `D1 /7` | SAR      | `.....a..` |
| `D2 /0` | ROL      | `o.......` |
| `D2 /1` | ROR      | `o.......` |
| `D2 /2` | RCL      | `o.......` |
| `D2 /3` | RCR      | `o.......` |
| `D2 /4` | SHL      | `o....a..` |
| `D2 /5` | SHR      | `o....a..` |
| `D2 /6` | SETMOC   | `o..szapc` |
| `D2 /7` | SAR      | `o....a..` |
| `D3 /0` | ROL      | `o.......` |
| `D3 /1` | ROR      | `o.......` |
| `D3 /2` | RCL      | `o.......` |
| `D3 /3` | RCR      | `o.......` |
| `D3 /4` | SHL      | `o....a..` |
| `D3 /5` | SHR      | `o....a..` |
| `D3 /6` | SETMOC   | `o..szapc` |
| `D3 /7` | SAR      | `o....a..` |
| `D4`    | AAM      | `o....a.c` |
| `D5`    | AAD      | `o....a.c` |
| `F6 /0` | TEST     | `.....a..` |
| `F6 /1` | TEST     | `.....a..` |
| `F6 /4` | MUL      | `...szap.` |
| `F6 /5` | IMUL     | `...szap.` |
| `F6 /6` | DIV      | `o..szapc` |
| `F6 /7` | IDIV     | `o..szapc` |
| `F7 /0` | TEST     | `.....a..` |
| `F7 /1` | TEST     | `.....a..` |
| `F7 /4` | MUL      | `...szap.` |
| `F7 /5` | IMUL     | `...szap.` |
| `F7 /6` | DIV      | `o..szapc` |
| `F7 /7` | IDIV     | `o..szapc` |

## OR, AND, XOR, TEST

These four boolean operations leave the `AF` flag undefined.

On the 8088, `OR`, `AND`, `XOR`, and `TEST` all clear the `AF` flag.

## DAA

The `DAA` instruction leaves `OF` undefined. 

The overflow flag is set as normal for binary addition: it is set when the result's sign bit changes from 0 to 1.

```
OF = (~AL & RESULT & 0x80) != 0;
```

## DAS

The `DAS` instruction leaves `OF` undefined.

The overflow flag is set as normal for binary subtraction: it is set when the result's sign changes from 1 to 0.

```
OF = (AL & ~RESULT & 0x80) != 0;
```

## AAA 

The `AAA` instruction leaves `OF`, `SF`, `ZF`, and `PF` undefined.

The overflow flag is set as normal for binary addition: it is set when the result's sign bit (before masking with 0x0F) changes from 0 to 1.

```
OF = (~AL & RESULT & 0x80) != 0;
```

`SF`, `ZF`, and `PF` are set as normal for any binary addition based on the result before masking with 0x0F, using a byte operand size.

## AAS

The `AAS` instruction leaves `OF`, `SF`, `ZF`, and `PF` undefined.

The overflow flag is set as normal for binary subtraction: it is set when the result's sign bit (before masking with 0x0F) changes from 1 to 0.

```
OF = (AL & ~RESULT & 0x80) != 0;
```

`SF`, `ZF`, and `PF` are set as normal for any binary subtraction based on the result before masking with 0x0F, using a byte operand size.

## SETMO, SETMOC

The undocumented `SETMO` instruction clears `CF`, `OF` and `AF`. 
`SF`, `ZF`, and `PF` are set as normal for the resulting value of `0xFF` for byte operand size or `0xFFFF` for word operand size.

`SETMOC` behaves similarly, but no flags are modified if `CL` is 0.

## SHR

Shift instructions leave `AF` undefined.

Right shifts on the 8088 clear the `AF` flag for nonzero shift counts.

The `OF` flag is undefined for right-shifts greater than 1.
For a shift of 0, `OF` is unmodified.
For a shift of 1, `SHR` sets `OF` to the original MSB/sign bit.
For multiple shifts, `OF` will always be cleared since the MSB has been already cleared.

## SAR

Shift instructions leave `AF` undefined.

Right shifts on the 8088 clear the `AF` flag for nonzero shift counts.

For multiple shifts, Intel specifies that `OF` is undefined. 

The 8088 always clears the `OF` flag for nonzero counts.

## SHL

`SHL` leaves `AF` undefined for nonzero shift counts.

On the 8088, left shift operations compute `AF` as carry out of the bottom nibble, as normal. For shifts greater than 1, `AF` is computed for each step, the final value of which depends on the last shift performed.

Left shifts with a count greater than 1 leave `OF` undefined.

The 8088 has the following behavior:
For a shift of 0, `OF` is unmodified.
For a shift of 1, `OF` is set if the MSB changes, corresponding to the effective word size.
For multiple shifts, `OF` will be calculated per step, reflecting the state of the last shift performed.

Single-shift pseudocode
```
OF = MSB(v ^ a);
```

## ROL, RCL

Rotate instructions leave `AF` unchanged.

Rotate instructions on the 8088 do not modify the `AF` flag. 

Rotates with a count greater than 1 leave `OF` undefined.

The 8088 has the following behavior:
For a shift of 0, `OF` is unmodified.
For a shift of 1, `OF` is set to the XOR of the MSB of the result and the carry flag. 
For multiple shifts, `OF` will be calculated per step, reflecting the state of the last shift performed.

Single-shift pseudocode (CARRY is the carry from the final rotation step):
```
OF = MSB(RESULT) ^ CARRY
```

## ROR, RCR

Rotate instructions leave `AF` unchanged.

Rotate instructions on the 8088 do not modify the `AF` flag. 

Rotates with a count greater than 1 leave `OF` undefined.

For a shift of 0, `OF` is unmodified.
For a shift of 1, `OF` is set to XOR of the top two-bits of the result.
For multiple shifts, `OF` will be calculated per step, reflecting the state of the last shift performed.

Single-shift pseudocode
```
OF = MSB(RESULT) ^ SECOND_MSB(RESULT);
```

## AAM

The `AAM` instruction leaves `OF`, `AF` and `CF` undefined.

The 8088 clears all three of these flags.

## AAD

The `AAD` instruction leaves `OF`, `AF` and `CF` undefined.

All three flags are set as normal for binary arithmetic with an 8-bit operand, reflecting the final byte addition of the original `AL` register and the original `(AH * BASE) & 0XFF`.

## MUL / IMUL

`MUL` and `IMUL` leave `SF`, `ZF`, `AF` and `PF` undefined.

Flag calculation depends on word size:

| Operand Size | HIGH | LOW | MASK   |
| ------------ | ---- | --- | ------ |
| Byte         | AH   | AL  | 0xFF   |
| Word         | DX   | AX  | 0xFFFF |

MUL sets `SF`, `ZF`, and `PF` as normal from the value represented by `HIGH`.
MUL clears `AF`.

IMUL sets `SF`, `ZF` and `PF` based on the product term `T`:

```
T = (HIGH + MSB(LOW)) & MASK;
```

IMUL sets `SF` to `MSB(T)`.
IMUL sets `ZF` if `T==0`.
IMUL sets `AF` if a carry from the lower nibble occurred computing `T`.
IMUL sets `PF` based on `T & 0xFF`.

IMUL `AF` calculation pseudocode:
```
AF = MSB(LOW) && ((HIGH & 0x0F) == 0x0F);
```

## DIV / IDIV

`DIV` and `IDIV` leave `OF`, `SF`, `ZF`, `AF`, `PF` and `CF` undefined.

Division unfortunately represents a difficult scenario for emulating undefined flag behavior. Flags are updated within iterations of the microcode division loop.

There are still some easy to implement flag behaviors on the 8088:

`DIV` sets `CF` to the inverted MSB of the quotient.
`IDIV` clears `CF` and `OF` explicitly using the `CCOF` microcode operator.

For both `DIV` and `IDIV`, the `ZF` is set if the remainder is 0, and the quotient is odd.

`OF`, `SF`, `AF`, and `PF` are calculated from a flag-updating subtraction within the microcode loop, representing the last trial subtraction performed.
This means that `SF` does not indicate the sign of the quotient.

On division-by-zero, `CF`, `OF`, and `AF` are cleared by the 8088.