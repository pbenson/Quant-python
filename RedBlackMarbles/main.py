class DPNode:
    def __init__(self, black, red, dp):
        self.black = black
        self.red = red
        self.dp = dp
        if black == 0:
            self.stop = True
            self.policy_winnings = red
        else:
            if red == 0:
                self.stop = False
                self.policy_winnings = 0
            else:
                self.policy_winnings = None

    def __str__(self):
        return "Bag(" + str(self.red) + ', ' + str(self.black) + ')'

    def expected_winnings(self):
        if not self.policy_winnings:
            winnings_if_go = 0
            if self.red > 0:
                winnings_if_go += self.red / (self.red + self.black) \
                                  * self.dp.node(self.black, self.red - 1).expected_winnings()
            if self.black > 0:
                winnings_if_go += self.black / (self.red + self.black) \
                                  * self.dp.node(self.black  - 1, self.red).expected_winnings()
            winnings_if_stop = self.red - self.black
            self.stop = winnings_if_go < winnings_if_stop
            if self.stop:
                self.policy_winnings = winnings_if_stop
            else:
                self.policy_winnings = winnings_if_go
        return self.policy_winnings

    def stage(self):
        return self.red + self.black


class DP:
    def __init__(self):
        self.red_black_pair_to_node_dict = {}
        # the fewer red remaining in bag
        self.min_red_for_stop_by_stage = {}

    def node(self, red, black):
        key = (red, black)
        if key not in self.red_black_pair_to_node_dict:
            self.red_black_pair_to_node_dict[key] = DPNode(red, black, self)
        return self.red_black_pair_to_node_dict[key]


dp = DP()
x = dp.node(30, 30).expected_winnings()
print(x)