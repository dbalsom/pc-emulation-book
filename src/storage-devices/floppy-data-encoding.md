# Floppy Data Encoding

If you are not already familiar with floppy disks, their operation and organization, you may wish to review the prior section on [floppy disk concepts](./floppy-concepts.md).

Before data can be written to a floppy disk, it must first be *encoded* using a scheme to make the data compatible with storage via timed *flux transitions*.

An encoding scheme has the primary job of making [clock recovery](https://en.wikipedia.org/wiki/Clock_recovery) possible, since data transfer to and from a floppy drive is a serial stream with no independent clock line. By inserting *clock bits*, an encoding scheme can allow the controller to synchronize with the rate data is being streamed from any given floppy drive while accounting for factors such as slightly too fast or slightly too slow spindle motors, RPM wobble, or basic signal jitter. 

A variety of encoding schemes have been used on floppy disks over the years, but only one — MFM — is primarily relevant on PC.

| Encoding | Name | Typical use | Notes |
| --- | --- | --- | --- |
| FM | Frequency modulation | Early 8" floppies and occasionally elsewhere | Simple, but inefficient |
| MFM | Modified frequency modulation | IBM PC-compatible floppy formats | The dominant PC floppy encoding for "double density" diskettes, more efficient than FM |
| GCR | Group coded recording | Apple, Commodore, and other non-PC floppy systems | Encodes groups of data bits into code words. |
| MMFM | Modified modified frequency modulation | Some non-PC or specialized floppy formats | A less common MFM variant that further improves efficiency |

Almost all floppy disks written for the IBM PC use primarily MFM encoding for user-accessible data. 

> [!NOTE]
> FM-encoded sectors do regularly appear on commercially duplicated software titles, usually on the very last track of a floppy. These are called duplication marks. They often contain metadata about the publisher, duplication parameters, and sometimes even the copy-protection scheme employed. It is not critical that your emulator be able to read them, and only certain disk images can encode them, anyway.

## FM Encoding

FM encoding is conceptually very simple. `1` bits are inserted between each data bit of the data stream to be encoded. An FM-encoded data stream will begin with an initial `1` clock bit.

If we begin with the bit sequence `1100_0101`, after inserting clock bits, we are left with the sequence `1111_1010_1011_1011`. 

The clock and data bits interleave like so:

|       Source       |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  |
| :----------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Original data bits |     | `1` |     | `1` |     | `0` |     | `0` |     | `0` |     | `1` |     | `0` |     | `1` |
|     Clock bits     | `1` |     | `1` |     | `1` |     | `1` |     | `1` |     | `1` |     | `1` |     | `1` |     |
|  FM-encoded byte   | `1` | `1` | `1` | `1` | `1` | `0` | `1` | `0` | `1` | `0` | `1` | `1` | `1` | `0` | `1` | `1` |

A trivial encoding table can be constructed:

| Data Bit | Output FM Sequence |
| :------: | :----------------: |
|   `0`    |        `10`        |
|   `1`    |        `11`        |

Since there are only two possible output sequences, FM-encoded data is magnetically encoded with two discrete *flux transition periods*, which we will call short and long transitions. These periods refer to the time between a pair of flux transitions.

| Period Type | Encodes | Period Length |
|-------------|-------|---------------|
| Short       | `1`   | 4 microseconds at a 250kHz FM write clock |
| Long        | `01`  | 8 microseconds at a 250kHz FM write clock |

Note that FM encoded data becomes twice as long as the source data it encodes. For this reason other, more efficient encoding schemes became more popular.


## MFM Encoding

MFM encoding improves on FM by only inserting clock bits where they are needed for clock recovery. A clock bit is written before a `0` data bit only when the previous data bit was also `0`; all other clock positions are left empty, represented as `0` in the encoded cell stream. Since encoding any particular bit sequence into MFM requires knowledge of the previous bit in the stream, we can say that MFM is a *stateful* encoding scheme. 

The mathematical representation of MFM encoding can be written as:

$$
(x, y, z) \to (x, \overline{x \vee y}, y, \overline{y \vee z}, z, \ldots)
$$

Some sort of data leader or *sync region* may be needed to initialize a MFM data stream since there will always be a first bit in any stream, which will by definition not have a valid previous bit.

If we begin with the same bit sequence as before, `1100_0101`, and assume that the previous data bit was `0`, MFM encoding gives us the sequence `0101_0010_1001_0001`.

The clock and data cells interleave like so:

|       Source       |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10  | 11  | 12  | 13  | 14  | 15  |
| :----------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Original data bits |     | `1` |     | `1` |     | `0` |     | `0` |     | `0` |     | `1` |     | `0` |     | `1` |
|    Clock cells     | `0` |     | `0` |     | `0` |     | `1` |     | `1` |     | `0` |     | `0` |     | `0` |     |
|  MFM-encoded byte  | `0` | `1` | `0` | `1` | `0` | `0` | `1` | `0` | `1` | `0` | `0` | `1` | `0` | `0` | `0` | `1` |

When encoding a stream of bits into MFM one has to account for the previous data bit. In the table below, `-` means that no clock bit is inserted:

| Current Data Bit | Previous Data Bit | Inserted Clock Bit | Output MFM Sequence |
| :--------------: | :---------------: | :----------------: | :-----------------: |
|       `0`        |        `0`        |        `1`         |        `10`         |
|       `0`        |        `1`        |        `-`         |        `00`         |
|       `1`        |        `0`        |        `-`         |        `01`         |
|       `1`        |        `1`        |        `-`         |        `01`         |

Although MFM still doubles the length of the encoded bitstream, it allows for more efficient representation as time between flux transitions, reducing the total number of transitions required. MFM is twice as efficient as FM as a result.

MFM-encoded data is magnetically encoded with three discrete *flux transition periods*. These periods refer to the time between a pair of flux transitions.

| Period Type | Encodes         | Period Length |
|-------------|-----------------|---------------|
| Short       | `10`            | 4 microseconds at a 500kHz MFM write clock |
| Medium      | `100`           | 6 microseconds at a 500kHz MFM write clock |
| Long        | `1000`          | 8 microseconds at a 500kHz MFM write clock |

> [!NOTE]
> You may see references begin the bitwise expansion of a flux transition time with either a `0` or `1`, putting the `1` bit on either end.
> Either notation is functionally equivalent, since the period between flux transitions essentially defines the number of `0`'s between two `1`'s.

## Marker Sequences

FM and MFM encoding specify standard rules by which data is encoded into clock and data bits, and subsequently into flux transitions. Breaking those rules would naturally produce an illegal stream, which we might refer to as an *MFM error* in the case of MFM encoding.

There are however circumstances where an invalid MFM sequence can be allowed. One such use case is for defining *track markers*. A track marker is a specially encoded run of data that uses a unique, detectable pattern of *clock bits* that essentially allows it to stand out from normally-encoded data. A sort of out-of-band signal, if you will.

For example, an MFM *sector ID address marker* (IDAM) contains three specially-encoded `A1` bytes. Each has the data pattern `A1`, but uses a clock pattern of `0A` instead of the normal MFM clock pattern of `0E`. This creates a single, missing `1` bit in the clock signal - enough for a floppy drive controller to identify the sequence as a marker.

<table class="mfm-marker-table mfm-fixed-width">
  <thead>
    <tr>
      <th>Source</th>
      <th>Hex</th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
      <th>13</th>
      <th>14</th>
      <th>15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Data cells</th>
      <td><code>A1</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>1</code></td>
    </tr>
    <tr>
      <th>Normal clock cells</th>
      <td><code>0E</code></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
    </tr>
    <tr>
      <th>Marker clock cells</th>
      <td><code>0A</code></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td class="missing-clock">0</td>
      <td></td>
      <td><code>1</code></td>
      <td></td>
      <td><code>0</code></td>
      <td></td>
    </tr>
    <tr>
      <th>Marker Encoding</th>
      <td><code>4489</code></td>
      <td><code>0</code></td>
      <td><code>1</code></td>
      <td><code>0</code></td>
      <td><code>0</code></td>
      <td><code>0</code></td>
      <td><code>1</code></td>
      <td><code>0</code></td>
      <td><code>0</code></td>
      <td><code>1</code></td>
      <td><code>0</code></td>
      <td class="missing-clock">0</td>
      <td><code>0</code></td>
      <td><code>1</code></td>
      <td><code>0</code></td>
      <td><code>0</code></td>
      <td><code>1</code></td>
    </tr>
  </tbody>
</table>

# Primary References

 - (floppy.cafe) [MFM Encoding](https://floppy.cafe/mfm.html)