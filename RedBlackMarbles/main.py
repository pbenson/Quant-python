class BagNode:
    def __init__(self, red, black, bag_nodes):
        self.red = red
        self.black = black
        self.bag_nodes = bag_nodes
        self.stop = False
        if red == 0:
            self.policy_winnings = black
            self.stop = True
        else:
            if black == 0:
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
                                  * self.bag_nodes.bag_node(self.red - 1, self.black).expected_winnings()
            if self.black > 0:
                winnings_if_go += float(self.black) / (self.red + self.black) \
                                  * self.bag_nodes.bag_node(self.red, self.black - 1).expected_winnings()
            self.stop = winnings_if_go < self.black - self.red
            if self.stop:
                self.policy_winnings = self.black - self.red
            else:
                self.policy_winnings = winnings_if_go
        return self.policy_winnings


class BagNodes:
    def __init__(self):
        self.red_black_pair_to_bag_dict = {}

    def bag_node(self, red, black):
        key = (red, black)
        if key not in self.red_black_pair_to_bag_dict:
            self.red_black_pair_to_bag_dict[key] = BagNode(red, black, self)
        return self.red_black_pair_to_bag_dict[key]


bag_nodes = BagNodes()
x = bag_nodes.bag_node(26, 17).expected_winnings()
print(x)