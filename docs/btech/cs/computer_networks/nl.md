---
id: nl
title: Network Layer
sidebar_label: Network Layer
---

Network links can be divided into two categories: those using point-to-point
connections and those using broadcast channels. We studied point-to-point links
in Physical Layer chapter; this chapter deals with broadcast links and their protocols.

In the literature, broadcast channels are sometimes referred to as multiaccess
channels or random access channels.

The protocols used to determine who goes next on a multiaccess channel be-
long to a sublayer of the data link layer called the MAC (Medium Access Con-
trol) sublayer.

## Static Channel Allocation

The traditional way of allocating a single channel, such as a telephone trunk,
among multiple competing users is to chop up its capacity by using one of the
multiplexing schemes we described previously, such as FDM (Frequency Division
Multiplexing). If there are N users, the bandwidth is divided into N equal-sized
portions, with each user being assigned one portion. Since each user has a private
frequency band, there is now no interference among users. When there is only a
small and constant number of users, each of which has a steady stream or a heavy
load of traffic, this division is a simple and efficient allocation mechanism. A
wireless example is FM radio stations. Each station gets a portion of the FM band
and uses it most of the time to broadcast its signal.

However, when the number of senders is large and varying or the traffic is
bursty, FDM presents some problems. If the spectrum is cut up into N regions and
fewer than N users are currently interested in communicating, a large piece of
valuable spectrum will be wasted. And if more than N users want to communi-
cate, some of them will be denied permission for lack of bandwidth, even if some
of the users who have been assigned a frequency band hardly ever transmit or re-
ceive anything.
