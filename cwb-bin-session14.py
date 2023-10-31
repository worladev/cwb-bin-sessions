'''
SESSION 14 (/09/2023)
Mentor and Facilitator ==> ANDY AFFUL

PROBLEM STATEMENT: You are tasked with simulating the data acknowledgment process the the Transport Layer which
is responsible for ensuring reliable data transfer between two devices. It uses acknowledgment packets to confirm
the successful reception of data.

Write a Python function acknowledgment_checker(sent_packets, received_acknowledgments) that takes the following
arguments:

INPUT
sent_packets: A list of integers representing unique packet IDs sent from the sender device.
received_acknowledgments: A list of integers representing unique acknowledgment packet IDs received by the sender
device.

OUTPUT: The function should return a list of integers, indicating the IDs of packets that have not been
successfully acknowledged.

Example:
sent_packets = [1, 2, 3, 4, 5]
received_acknowledgments = [2, 4]

missing_packets = acknowledgment_checker(sent_packets, received_acknowledgments)
print(missing_packets)
# Output: [1, 3, 5]

Explanation:
In this question, the acknowledgment_checker function simulates the acknowledgment process of the Transport Layer.
It takes two lists as input: sent_packets representing unique packet IDs sent and received_acknowledgments
representing unique acknowledgment packet IDs received. The function calculates and returns the IDs of packets
that have not been successfully acknowledged.
'''
def acknowledgment_checker(sent_packets, received_acknowledgments):
    
    #variable to hold IDs that were not acknowledged
    failed_acknowledgments = list()

    #check for empty input list
    if len(sent_packets) == 0 or len(received_acknowledgments) == 0:
        return failed_acknowledgments

    #comprehension to get IDs that were not acknowledged
    failed_acknowledgments = [id for id in sent_packets if id not in received_acknowledgments]

    return failed_acknowledgments

