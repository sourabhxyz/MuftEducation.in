---
id: ll
title: Link Layer  
sidebar_label: Link Layer
---

* We will refer to any device that runs a link-layer protocol as node.
* The communication channels that connect adjacent nodes along the communication path as links.
* In order to transfer data transferred from source node to destination node, it must be moved over each of the individual links in the end-to-end path.
* Transmitting nodes encapsulate datagram in a link-layer frame and transmits the frame into the link.

## Link Layer Services

* **Framing**: A frame consists of a data field, in which the network-layer
datagram is inserted, and a number of header fields.
* **Reliable delivery**: When a link-layer protocol provides reliable
delivery service, it guarantees to move each network-layer datagram
across the link without error.
* **Link access**: A medium access control (MAC) protocol specifies the
rules by which a frame is transmitted onto the link. For
point-to-point links, the MAC protocol is simple. The more
interesting case is when multiple nodes share a single broadcast
link—the so-called multiple access problem.
* **Error detection and correction**: The link-layer hardware in a
receiving node can incorrectly decide that a bit in a frame is zero
when it was transmitted as a one, and vice versa

## Framing

* The bit stream received by the data link layer is not guaranteed to be error free.
* It is up to the data link layer to detect and, if necessary, correct errors.
* Data link layer to break up the bit stream into discrete frames, compute a short token called a checksum for each frame, and include the checksum in the frame when it is transmitted.
* When a frame arrives at the destination, the checksum is recomputed. If the newly computed checksum is different from the one contained in the frame, the data link layer knows that an error has occurred and takes steps to deal with it.
* Four methods for Framing:
  * Byte count.
  * Flag bytes with byte stuffing.
  * Flag bytes with bit stuffing.
  * Physical layer coding violations.

### Byte count

![byte count](../../../assets/btech/cs/computer_networks/ll1.png)
*Figure [Tanenbaum] A byte stream (a) Without errors. (b) With one error*

### Flag bytes with byte stuffing

Two consecutive flag bytes indicate the end of one frame and the start of the next. 
Thus, if the receiver ever loses synchronization it can just search for two flag bytes to find the end of the current frame and the start of the next frame

![flag bytes with byte stuffing](../../../assets/btech/cs/computer_networks/ll2.png)
*Figure [Tanenbaum] (a) A frame delimited by flag bytes. (b) Four examples of byte sequences before and after byte stuffing.*

$2B$ overhead.

### Flag bytes with bit stuffing

Each frame begins and ends with a special bit pattern, 01111110 or 0x7E in hexadecimal. This pattern is a flag byte. 

Whenever the sender’s data link layer encounters five consecutive 1s in the data, it automatically stuffs a 0 bit into the outgoing bit stream. 

When the receiver sees five consecutive incoming 1 bits, followed by a 0 bit, it automatically destuffs (i.e., deletes) the 0 bit.

![bit stuffing](../../../assets/btech/cs/computer_networks/ll3.png)
*Figure [Tanenbaum] (a) The original data. (b) The data as they appear on the line. (c) The data as they are stored in the receiver’s memory after destuffing*

$B/5$ overhead. (But hard disks prefer byte reads and writes)

### Physical layer coding violations

* Encoding of bits as signals often includes redundancy to help the receiver.
* For example, in the 4B/5B line code 4 data bits are mapped to 5 signal bits to ensure sufficient bit transitions. We can use some reserved signals to indicate the start and end of frames.
* We are using “coding violations” to delimit frames.
* It is easy to find the start and end of frames and there is no need to stuff the data.

## Error Control

Having solved the problem of marking the start and end of each frame, we
come to the next problem: how to make sure all frames are eventually delivered to
the network layer at the destination and in the proper order.

The usual way to ensure reliable delivery is to provide the sender with some
feedback about what is happening at the other end of the line. Typically, the protocol calls for the receiver to send back special control frames bearing positive or
negative acknowledgements about the incoming frames. If the sender receives a
positive acknowledgement about a frame, it knows the frame has arrived safely.
On the other hand, a negative acknowledgement means that something has gone
wrong and the frame must be transmitted again.

An additional complication comes from the possibility that hardware troubles
may cause a frame to vanish completely (e.g., in a noise burst). In this case, the
receiver will not react at all, since it has no reason to react. Similarly, if the acknowledgement frame is lost, the sender will not know how to proceed. It should
be clear that a protocol in which the sender transmits a frame and then waits for
an acknowledgement, positive or negative, will hang forever if a frame is ever lost
due to, for example, malfunctioning hardware or a faulty communication channel.
This possibility is dealt with by introducing timers into the data link layer.
When the sender transmits a frame, it generally also starts a timer. The timer is
set to expire after an interval long enough for the frame to reach the destination,
be processed there, and have the acknowledgement propagate back to the sender.
Normally, the frame will be correctly received and the acknowledgement will get
back before the timer runs out, in which case the timer will be canceled.

However, if either the frame or the acknowledgement is lost, the timer will go
off, alerting the sender to a potential problem. The obvious solution is to just
transmit the frame again. However, when frames may be transmitted multiple
times there is a danger that the receiver will accept the same frame two or more
times and pass it to the network layer more than once. To prevent this from hap-
pening, it is generally necessary to assign sequence numbers to outgoing frames,
so that the receiver can distinguish retransmissions from originals.

## Flow Control

Another important design issue that occurs in the data link layer (and higher
layers as well) is what to do with a sender that systematically wants to transmit
frames faster than the receiver can accept them. This situation can occur when
the sender is running on a fast, powerful computer and the receiver is running on a
slow, low-end machine.

Two approaches
are commonly used. In the first one, **feedback-based flow control**, the receiver
sends back information to the sender giving it permission to send more data, or at
least telling the sender how the receiver is doing. In the second one, **rate-based flow control**, the protocol has a built-in mechanism that limits the rate at which
senders may transmit data, without using feedback from the receiver.

## Error detection and correction

* Transmission errors are unavoidable. We need to develop techniques to deal with them.
* One strategy is to include enough redundant information to enable the receiver to deduce what the transmitted data must have been — Forward Error Correction (FEC)
* The other is to include only enough redundancy to allow the receiver to deduce that an error has occurred and have it request a retransmission.
* When noise is unavoidable like in wireless communication, FEC is must and when there is low probability of error then detection is better.

* A frame consists of m data (i.e., message) bits and r redundant (i.e. check) bits.
* Block code: the $r$ check bits are computed solely as a function of the $m$ data bits with which they are associated
* Systematic code: the $m$ data bits are sent directly, along with the check bits, rather than being encoded themselves before they are sent.
* Linear code: the $r$ check bits are computed as a linear function of the m data bits. Exclusive OR (XOR) or modulo 2 addition is a popular choice.
* The codes we will look at are linear, systematic block codes unless otherwise noted.
* Let the total length of a block be $n$ (i.e., $n = m + r$ ). We will describe this as an $(n, m)$ code. An $n$-bit unit containing data and check bits is referred to as an n-bit codeword. The code rate is the fraction of the codeword that carries non-redundant information i.e., $m/n$.

## Hamming Codes

* Given two code words 10001001 and 10110001 — is to possible to determine how many corresponding bits differ?
* This difference is called the Hamming distance
* If two code words are a Hamming distance of $d$ apart, $d$ single-bit errors are needed to convert one into the other.
* In most data transmission applications, all $2^m$ possible data messages are legal, but due to the way the check bits are computed, not all of the $2^n$ possible codewords are used. In fact, when there are $r$ check bits, only the small fraction of $2^m/2^n$ or $1/2^r$ of the possible messages will be legal codewords.
* Given the algorithm for computing the check bits, it is possible to construct a complete list of the legal codewords, and from this list to find the two codewords with the smallest Hamming distance. This distance is the Hamming distance of the complete code.
* To reliably detect $d$ errors, you need a distance $d + 1$ code because with such a code there is no way that $d$ single-bit errors can change a valid codeword into another valid codeword. When the receiver sees an illegal codeword, it can tell that a transmission error has occurred. 
* Similarly, to correct $d$ errors, you need a distance $2d + 1$ code because that way the legal codewords are so far apart that even with $d$ changes the original codeword is still closer than any other codeword. This means the original codeword can be uniquely determined based on the assumption that a larger number of errors are less likely.
* We want to design a code with $m$ message bits and $r$ check bits that will allow all single errors to be corrected.
* Each of the $2^m$ legal messages has $n$ illegal codewords at a distance of 1 from it.
* Each of the $2^m$ legal messages requires $n + 1$ bit patterns dedicated to it.
* We get the requirement that $2^m(n + 1) \leq 2^n \rightarrow (m + r + 1) \leq 2^r$. 
* To correct 2 bit errors $\rightarrow 2^m({n \choose 2} + 1) \leq 2^n$
* (For 1 bit error correction, consider $|m_i| = 7$) Place check bits at index power of two because then $d(C(m_1), C(m_2)) \geq 3$ whenever $d(m_1, m_2) \geq 1$ as index of bit difference will not be a power of 2.
