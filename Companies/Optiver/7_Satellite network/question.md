Satellite Network Simulation

During system tests, the team wants to ensure that messages they sent are processed in the correct order.

Protocol Rules:
- Message is sent from Earth directly to one or more satellites .
- Every satellite that receives the message forwards it to all its direct connections, in increasing order of SatelliteId, as long as they haven't received it yet .
- Once all its direct connections have received the message, a satellite processes the message and reports back to Earth .

Important Notes:
- Forwarding Time: It takes 10 seconds for a satellite to forward a message to one of its connections .
- Synchronous & Atomic: For every sender, only one message can be forwarded at a time and it takes exactly 10s to complete .
- As soon as the forwarding procedure is complete, you may assume that the entire network knows that the receiver satellite has been notified, i.e., no further attempts to notify it must be performed .
- While the forwarding procedure is not complete, any other satellite may attempt to forward messages to the same connection. In this case, the same 10 seconds are spent by the sender .
- A satellite will never try to notify the satellite that notified it .
- Reporting Time: It takes a satellite 30 seconds to process the message and report back to Earth .
- Tie-Breaking: If two satellites report back to Earth at the same time, the one with the smaller SatelliteId arrives first .

Problem Statement:
You will receive a stream of N instructions . Complete the functions SatelliteConnected, RelationshipEstablished, and MessageReceived of the SatelliteNetwork class.

Class & Function Signatures:

class SatelliteNetwork:

    def SatelliteConnected(self, satellite_id: int):
        """
        Indicates that a satellite is connected to the network.
        If a satellite connects more than once, call ErrDuplicateSatellite(satellite_id).
        """
        ...

    def RelationshipEstablished(self, satellite_id1: int, satellite_id2: int):
        """
        Indicates a (two-way) relationship between two satellites.
        If any referenced SatelliteId does not exist, call ErrInvalidSatellite(satellite_id) for that ID, 
        and the whole instruction must be skipped.
        """
        ...

    def MessageReceived(self, satellite_ids: list[int]):
        """
        Indicates that a set of M satellites received a message simultaneously from Earth.
        If any referenced SatelliteId does not exist, call ErrInvalidSatellite(satellite_id) for that ID,
        and the whole instruction must be skipped.
        """
        ...


Callback / Helper Functions You Must Call:

- OnSatelliteReportedBack(satellite_id)
  Should be called to notify that a satellite reported back to Earth, in order of timestamp.

- ErrDuplicateSatellite(satellite_id)
  Should be called if a satellite connects more than once.

- ErrInvalidSatellite(satellite_id)
  Should be called if a referenced SatelliteId does not exist.