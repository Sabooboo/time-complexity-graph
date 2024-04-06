import heapq
import time

class AuctionWithPriorityQueue:
    def __init__(self, min_bid):
        self.min_bid = min_bid
        self.bids = []
        self.bidder_bids = {} 

    def placeBid(self, bid, bidder_id):
        if bid < self.min_bid:
            return # discard
        timestamp = time.time()
        heapq.heappush(self.bids, (-bid, timestamp, bidder_id))
        if bidder_id not in self.bidder_bids:
            self.bidder_bids[bidder_id] = []
        self.bidder_bids[bidder_id].append(bid)

    def closeAuction(self):
        if not self.bids:
            print("No bids were placed.")
            return
        highest_bid, _, highest_bidder_id = heapq.heappop(self.bids)
        highest_bid = -highest_bid

        # tie!?!?!?!?!?
        if self.bids and -self.bids[0][0] == highest_bid:
            print("Tie detected based on bid amount. Checking timestamps...")
            _, next_bid_timestamp, _ = self.bids[0]
            if self.bids and -self.bids[0][0] == highest_bid and self.bids[0][1] == next_bid_timestamp:
                print("Tie detected. Auction restarts with minimum bid of", highest_bid + 1)
                self.min_bid = highest_bid + 1
            else:
                print(f"Winner is bidder {highest_bidder_id} with a bid of {highest_bid}")
        else:
            print(f"Winner is bidder {highest_bidder_id} with a bid of {highest_bid}")

# Example usage
auction = AuctionWithPriorityQueue(min_bid=100)
auction.placeBid(150, "Bidder1")
auction.placeBid(200, "Bidder2")
auction.placeBid(200, "Bidder3") # tie
auction.closeAuction()
