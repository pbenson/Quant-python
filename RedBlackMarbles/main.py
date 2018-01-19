class BagNode:
    def __init__(self, black, red, bag_nodes):
        self.black = black
        self.red = red
        self.bag_nodes = bag_nodes
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
                winnings_if_go += float(self.red) / (self.red + self.black) \
                                  * self.bag_nodes.bag_node(self.black, self.red - 1).expected_winnings()
            if self.black > 0:
                winnings_if_go += float(self.black) / (self.red + self.black) \
                                  * self.bag_nodes.bag_node(self.black  - 1, self.red).expected_winnings()
            winnings_if_stop = self.red - self.black
            self.stop = winnings_if_go < winnings_if_stop
            if self.stop:
                self.policy_winnings = winnings_if_stop
            else:
                self.policy_winnings = winnings_if_go
        return self.policy_winnings

    def stage(self):
        return self.red + self.black


class BagNodes:
    def __init__(self):
        self.red_black_pair_to_bag_dict = {}
        # the fewer red remaining in bag
        self.min_red_for_stop_by_stage = {}

    def bag_node(self, red, black):
        key = (red, black)
        if key not in self.red_black_pair_to_bag_dict:
            self.red_black_pair_to_bag_dict[key] = BagNode(red, black, self)
        return self.red_black_pair_to_bag_dict[key]


bag_nodes = BagNodes()
x = bag_nodes.bag_node(1000, 1000).expected_winnings()
print(x)