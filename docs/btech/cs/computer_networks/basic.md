---
id: basic
title: Basic  
sidebar_label: Basic
---


## Evaluation Criteria

* Scribe - 5%
* Weekly Quizzes - 20% 
* Mid term 1 - 15%
* Mid term 2 - 15%
* Final Exam - 45%
  
## Protocol

A protocol defines the format and the order of messages exchanged
between two or more communicating entities, as well as the actions taken
on the transmission and/or receipt of a message or other event.

## Packet Switching

* End systems exchange messages with each other.
* Long messages into smaller chunks of data known as packets.
* Between source and destination, each packet travels through
  communication links and packet switches
* Packets are transmitted over each communication link at a rate equal
  to the full transmission rate of the link. So, if a source end system or
  a packet switch is sending a packet of $L$ bits over a link with
  transmission rate $R$ bits/sec, then the time to transmit the packet is
  $L/R$ seconds.
* Each packet can transfer via different path.

### Store And Forward

Store-and-forward transmission means that the packet switch (router) must
receive the entire packet before it can begin to transmit the first bit of the packet onto the outbound link (Maybe because we need to process header). Router can store multiple packets.

**Question:** Consider a simple network consisting of two end systems connected by a single router, as shown in the figure. 

![question1](../../../assets/btech/cs/computer_networks/basic1.png)
*Figure: [Kurose and Ross] Store-and-forward packet switching.*

All links in the above figure have transmission rate R bits/sec. The source wants to send 4
packets of L bits each to the destination. If the source starts transmission of the first packet
at time 0, at what time would the destination receive all the packets?

**Answer:** $2L/R + 3L/R = 5L/R$.

### Delay in Packet-Switched Networks

* **Processing Delay:** The time required to examine the packets header and determine where to direct the packet is part of the processing delay. The processing delay can also include other factors, such as the time needed to check for bit-level errors in the packet that occurred in transmitting the packets bits from the upstream node to router A. Processing delay in high-speed routers are typically on the order of microseconds or less. After this nodal processing, the router directs the packet to the queue that precedes the link to router B.
* **Queuing Delay:** At the queue, the packet experiences a queuing delay as it waits to be transmitted onto the link. The length
  of the queuing delay of a specific packet will depend on the number of earlier-arriving packets that are queued
  and waiting for transmission onto the link. If the queue is empty and no other packet is currently being
  transmitted, then our packets queuing delay will be zero. On the other hand, if the traffic is heavy and many
  other packets are also waiting to be transmitted, the queuing delay will be long.Queuing delays can be on
  the order of microseconds to milliseconds in practice.
* **Transmission Delay:** Assuming that packets are transmitted in a first-come-first-served manner, as is common in packet-switched networks, our packet can be transmitted only after all the packets that have arrived before it have been transmitted. Denote the length of the packet by $L$ bits, and denote the transmission rate of the link from router A to router B by $R$ bits/sec. The transmission delay is $L/R$. This is the amount of time required to push (that is, transmit) all of the packets bits into the link.
* **Propagation Delay:** Once a bit is pushed into the link, it needs to propagate to router B. The time required to propagate from the beginning of the link to router B is the propagation delay. The bit propagates at the propagation speed of the link. The propagation speed depends on the physical medium of the link. The propagation delay is the distance between two routers divided by the propagation speed. That is, the propagation delay is d/s, where d is the distance between router A and router B and s is the propagation speed of the link. Once the last bit of the packet propagates to node B, it and all the preceding bits of the packet are stored in router B. The whole process then continues with router B now performing the forwarding.

## Circuit Switching

* Resources needed along a path (buffers, link transmission rate) to provide for communication between the end systems are reserved for the duration of the communication session between the end systems.
* A circuit in a link is implemented with either frequency-division
  multiplexing (FDM) or time-division multiplexing (TDM).
* In **FDM**, the frequency spectrum of a link is divided up among the connections established across
  the link. Specifically, the link dedicates a frequency band to each connection for the duration of the
  connection.
* **TDM** is considered to be a digital procedure which can be employed when the transmission
  medium data rate quantity is higher than the data rate requisite of the transmitting and receiving devices.
  In TDM, corresponding frames carry data to be transmitted from the different sources. Each frame consists
  of a set of time slots, and portions of each source is assigned a time slot per frame.
* Circuit Switching is basically used for real time applications
* Packet switching is better than circuit switching as even traditional applications of circuit switching such as phone calls is now being done with the help of packet switching which even allows for both of the things, i.e. internet and phone call to happen simultaneously (VoLTE). Also it can easily accommodate more sporadic users without change in configuration.

## Protocol Layering

![Protocol Layering OSI Model](../../../assets/btech/cs/computer_networks/basic2.png)
*Figure: [Kurose and Ross] The Internet protocol stack (a) and OSI (Open Systems Interconnection) reference model (b).*

Layer interacts with layers only next to it.

Benefits of layering:
* We can modify a layer freely, i.e. tweak it. 
* Layer acts as a wrapper which can be unwrapped at the other end.

### Application Layer

The application layer is where network applications and their application-layer protocols reside. (Like HTTP, FTP, DNS, etc)
An application-layer protocol is distributed over multiple end systems, with the
application in one end system using the protocol to exchange packets of information
with the application in another end system. We’ll refer to this packet of information
at the application layer as a message.

### Transport Layer

The Internet’s transport layer transports application-layer messages between
application endpoints. In the Internet there are two transport protocols, TCP and
UDP, either of which can transport application-layer messages. TCP provides a
connection-oriented service to its applications. This service includes guaranteed
delivery of application-layer messages to the destination and flow control (that is,
sender/receiver speed matching). TCP also breaks long messages into shorter segments and provides a congestion-control mechanism, so that a source throttles its
transmission rate when the network is congested. The UDP protocol provides a connectionless service to its applications. This is a no-frills service that provides no
reliability, no flow control, and no congestion control. We'll refer to a
transport-layer packet as a segment.

### Network Layer

The Internet’s network layer is responsible for moving network-layer packets
known as datagrams from one host to another. The Internet’s network layer includes the celebrated IP Protocol, which defines
the fields in the datagram as well as how the end systems and routers act on these
fields.

### Link Layer

The Internet’s network layer routes a datagram through a series of routers between
the source and destination. To move a packet from one node (host or router) to the
next node in the route, the network layer relies on the services of the link layer. In
particular, at each node, the network layer passes the datagram down to the link
layer, which delivers the datagram to the next node along the route. At this next
node, the link layer passes the datagram up to the network layer.
 Examples of linklayer protocols include Ethernet, WiFi. As datagrams typically need to traverse several links to travel from source to
destination, a datagram may be handled by different link-layer protocols at different
links along its route. We'll refer to the linklayer packets as frames.

### Physical Layer

While the job of the link layer is to move entire frames from one network element
to an adjacent network element, the job of the physical layer is to move the individual bits within the frame from one node to the next. The protocols in this layer are
again link dependent and further depend on the actual transmission medium of the
link (for example, twisted-pair copper wire, single-mode fiber optics). 


![Encapsulation](../../../assets/btech/cs/computer_networks/basic3.png)
*[Kurose and Ross] Hosts, routers, and link-layer switches; each contains a different set of layers, reflecting their differences in functionality.*


Thus, we see that at each layer, a packet has two types of
fields: header fields and a payload field. The payload is typically a packet from
the layer above.


