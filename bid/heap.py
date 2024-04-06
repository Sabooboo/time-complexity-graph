import heapq

class Auction:
    def __init__(self, min_bid):
        self.min_bid = min_bid
        self.bids = []
        self.bidder_bids = {}

    def placeBid(self, bid, bidder_id):
        if bid < self.min_bid:
            return
        bid = -bid # python only has min heap so negate
        heapq.heappush(self.bids, (bid, bidder_id))
        if bidder_id not in self.bidder_bids:
            self.bidder_bids[bidder_id] = []
        self.bidder_bids[bidder_id].append(-bid)

    def closeAuction(self):
        if not self.bids:
            print("No bids were placed.")
            return
        highest_bid, highest_bidder_id = heapq.heappop(self.bids)
        highest_bid = -highest_bid # negate back to positive

        if self.bids and -self.bids[0][0] == highest_bid:
            print("Tie detected. Auction restarts with minimum bid of", highest_bid + 1)
            self.min_bid = highest_bid + 1
        else:
            print(f"Winner is bidder {highest_bidder_id} with a bid of {highest_bid}")
