# Floppy Disk Image Formats

A floppy *disk image* is a file or set of files that represents the data on a floppy disk. There are dozens of unique floppy disk formats, many of them specific to certain platforms, containing data specific to that platform.

A floppy disk image can capture data at different representational levels. At the lowest level, *flux-based* disk images capture individual read pulses from the floppy disk drive that generally correspond to individual flux transitions on the magnetic media. Above flux images, *bitstream* images encode the raw bits on a track. Above bitstream images, *sector-based* and *raw sector images* encode the individual sectors on a disk.

You are most likely to be familiar with *raw sector images* from the ubiquitous `.img` and `.ima` images made by utilities such as **WinImage**. 

Some floppy disk image formats can contain data at multiple representational levels. They may store a flux-based representation of some tracks, and bitstream representations of others. These are called *hybrid* image formats. 

Choosing what level of disk image largely depends on the intended goal when making the image. For archival preservation of floppy disks, *flux-based* images are best. For emulation of copy-protected titles, *flux-based* or *bitstream* level images are preferable. For normally formatted, non-copy-protected disk images, *sector-based* or *raw sector images* are sufficient. Raw sector images cannot hold the necessary metadata to encode unusual sector IDs, deliberately bad CRCs, weak bits, or other phenomena encountered on copy-protected diskettes.

## Disk Image Types

| Layer | What it stores | Best used for | Common examples |
| --- | --- | --- | --- |
| Raw sector image | Sector contents in logical order | Normal, unprotected disks | IMG, IMA, DSK |
| Sector-based image | Sector contents plus selected per-sector metadata | Disks with unusual sector numbering, deleted data marks, or recorded CRC state | TD0, IMD, PSI |
| Bitstream image | The encoded FM, MFM, or GCR bitstream for each track | Many copy-protected disks and controller-level emulation | PRI, MFM, HFE, 86F, IPF |
| Flux image | Raw or processed timing between flux transitions | Preservation, analysis, and difficult copy-protection schemes | PFI, SCP, KryoFlux RAW, MFI |
| Hybrid image | More than one representation level, often platform-specific | Systems with specialized track formats or mixed requirements | Not common on PC |

## Raw Sector Images

Raw sector images are the familiar `.img`, `.ima`, `.dsk`, and similar files used by many PC emulators. In the common PC case, they contain 512-byte sectors laid out in order, with no header and no explicit geometry or metadata. The disk layout is usually inferred from the file size.

This makes raw sector images simple, portable, and easy to edit. They are a good fit for ordinary disks in standard formats where no copy-protection is present and where the only thing that matters is the sector contents.

Raw sector images have no header, and contain no other data other than the contents of each sector. They cannot represent variable-size sectors, duplicate sector IDs, unusual address marks, bad CRCs, weak bits, or nonstandard gaps. If a program shipped on a copy-protected diskette depends on those details to function, a raw sector image is insufficient to make a working backup.

## Sector-Based Images

Sector-based formats still represent data in terms of sector contents, but these formats contain metadata about each sector. They may record sector ID information such as sector, cylinder and head numbers, unusual sector sizes, deleted data marks, CRC status, or other per-sector details. This makes them suitable for backup of some copy-protected titles, but they have largely been superseded by modern bitstream-level formats.

Common examples include:

* **Teledisk** (`.td0`)
    * A disk image format used by Sydex TELEDISK, an early commercial disk-copying program.
    * No official documentation exists, however Dave Dunfield published notes on the disk format and the format is
      supported by a number of tools and emulators.
    * Multiple versions exist, including different compression algorithms. 
        - Version 1.x images may use a custom LZW implementation instead.
        - Version 2 Teledisk images may be compressed with LZHUF compression. 
* **ImageDisk** (`.imd`)
    * ImageDisk is a format developed by Dave Dunfield as an open alternative to TeleDisk format images, although it
      has some encoding limitations.
* **PCE Sector Image** (`.psi`)
    * One of several image formats developed by Hampa Hug for use with his emulator, [PCE](http://www.hampa.ch/pce/). A flexible format based on RIFF-like data chunks. 
    * Perhaps the most advanced of all sector-based disk images, it has been used to encode a variety of copy-protected titles.

Sector-based images can handle many practical disk oddities, but they are still a reconstruction from decoded sectors. They may not be able to describe how the track was really arranged between sectors, and they can sometimes represent combinations of sectors that a real controller could never have read from a real track.

## Bitstream Images

Bitstream images store the low-level, encoded bit stream of each track on a diskette. On PC, this is typically an MFM-encoded bitstream.
These images typically can encode most protection types seen on the PC, given the appropriate metadata (weak and damaged bits), but are more
complex than sector images to manipulate and write back to.

This level is close to what a floppy controller consumes internally. It can preserve gap bytes, sync marks, unusual address marks, weak or damaged bit regions if the format supports them. What they cannot encode (without specialized metadata) is the actual flux timing, which some protections may rely on.

Common examples include:

* **PCE Raw Image** (`.pri`)
    * One of several image formats developed by Hampa Hug for use with his emulator, [PCE](http://www.hampa.ch/pce/).
      Along with track bitstream data, PRI supports weak bit masks.
* **MFM Bitstream Image** (`.mfm`)
    * A bitstream format created for use with the HxC drive emulation software.
    * Only MFM-encoded track data is included. There is no support for weak bits or other metadata.
* **HFE Bitstream Image** (`.hfe`)
    * Another format associated with the HxC software, HFE is also a bitstream container, however unlike MFM it supports
      multiple encoding types. There are several versions of HFE supported by HxC, HFEv3 being the newest, however the
      format is still considered experimental and not finalized. fluxfox supports HFE v1 files.
* **86Box Floppy Image** (`.86f`))
    * A format designed around the internal representation of disks in the 86Box emulator. Bitstream based and flexible
      in terms of per-track parameters, it also allows exact encoding of bitcell length to support track wrapping.
* **Interchangeable Preservation Format** (`.ipf`)
    * A format developed by the [Software Preservation Society](http://www.softpres.org/), originally designed to hold
      Amiga disk images, but expanded to Atari ST and theoretically capable of holding a variety of disk image types.
    * IPF files, unlike other bitstream-level images, divide a disk into elements which must be reconstructed to
      reproduce the original track data.
    * The SPS has curated official IPF disk image collections, although unofficial tools exist to create IPF files.
      These tools do not always create valid IPF images or properly set IPF metadata.

Bitstream images are much more capable than raw sector images, but they are also harder to manipulate. Editing a file inside a bitstream image means preserving the surrounding track structure, sector headers, checksums, gaps, and timing assumptions.

Some bitstream level formats, such as MFM and HFE, do not support specifying an absolute bit length. This can cause problems when emulating certain copy-protection schemes that involve precise handling of reading across the index (track wrapping).

## Flux Images

Flux-based images are created with specialized hardware that records the raw flux transitions reported by a disk drive. This is the lowest possible level of disk image. It is the closest representation we have of the actual contents of the disk — but still only a representation of the data as interpreted by a specific floppy disk drive.

Flux images are especially useful for preservation and research because they can retain information that decoding would otherwise discard. A flux capture can show damaged media, inconsistent reads, weak bits, speed variation, and ambiguous regions that need human or tool-assisted interpretation.

Flux images can be divided into two basic types: solved and unsolved flux.

 * **Unsolved** flux images are the most difficult of the three types of format to read and manipulate. Generally a sophisticated conversion process is required to analyze and combine the 3-5 revolutions of each track that is typically captured with a flux capture device. This makes them less than ideal for the purposes of emulation. Unsolved images with multiple revolutions cannot really be written to by an emulator in a sensible way - nor should you want to.

 * **Solved** flux images represent a post-processed flux capture where multiple revolutions have already been analyzed and combined into a single, corrected flux track. The resulting flux stream should represent a correct, clean read of each track. Metadata may need to be provided along with solved flux images as detection of weak bits, etc., is only possible by comparing multiple revolutions which are no longer present in a solved image. Solved flux images can technically be written to - but doing so is a complicated process.

### Raw Flux Images

* **PCE Flux Image** (`.pfi`)
    * One of several image formats developed by Hampa Hug for use with his emulator, [PCE](http://www.hampa.ch/pce/). 
      Contains raw flux stream data, for an arbitrary number of revolutions. Similar to Kryoflux, but in a single-file container.

* **SuperCardPro Image** (`.scp`)
    * A format designed for the [SuperCardPro](https://www.cbmstuff.com/index.php?route=product/product&product_id=52) flux imaging hardware, this format has become quite popular as a single-file flux container. The format supports several potentially useful metadata fields, but they are so frequently set to garbage values in SCP images in the wild that is impossible to trust them.
    * SCP images can also contain resolved flux tracks, if desired. Some emulators can write back to SCP, but typically write back a single revolution.

* **KryoFlux Stream Files** (`.raw`)
    * Less of an image format, and more of a collection of stream protocol dumps produced by
      the [Kryoflux](https://kryoflux.com/) flux imaging hardware. These 'images' comprise a set of files with the
      `.raw` extension, one file per track.
    * Each track file may contain an arbitrary number of revolutions.

### Resolved Flux Images

* **MAME Flux Image** (`.mfi`)
    * A resolved flux format designed for the famous MAME emulator (which emulates many kinds of computer, not just arcade machines.)
    * MFI images contain a single revolution, encoding "zones" of NFA's or surface damage to support various copy-protection methods.

### Hybrid and Multi-Resolution Images

Some formats deliberately mix levels of representation. Apple's MOOF format, for example, is a chunked Macintosh disk image format that can store MFM or GCR tracks at either bitstream or resolved-flux resolution.

Hybrid formats exist because no single abstraction is ideal for every disk. A normal track may be most compactly stored as decoded data, while a copy-protected track may need a bitstream or flux-level description. 

### Track Data Encodings

* **MFM**
    * Most floppy images used on the IBM PC
      primarily use [MFM](https://en.wikipedia.org/wiki/Modified_frequency_modulation) encoding. These disks are
      commonly referred to as 'double density'.
* **FM**
    * Earlier 8-inch floppies used FM encoding instead and were referred to as "standard density".
    * Commercial disk duplicators would sometimes include an FM-encoded track at the end of an otherwise MFM-encoded diskette, containing duplication info.
      Sometimes these "duplication marks" contain useful clues as to the type of copy-protection used.
* **GCR**
    * [Group Coded Recording](https://en.wikipedia.org/wiki/Group_coded_recording) is an encoding scheme that is more complex but also more efficient than either FM or MFM. It was not used on the PC.

## Primary References

 - (dunfield.classiccmp.org) ImageDisk source code: [Disk/Software Image Archive](http://dunfield.classiccmp.org/img/)
 - (dunfield.classiccmp.org) [Teledisk (td0) Notes](http://dunfield.classiccmp.org/img42841/td0notes.txt)
 - (86box.readthedocs.io) [86f v2.12 file format specification](https://86box.readthedocs.io/en/v5.0/dev/formats/86f.html)