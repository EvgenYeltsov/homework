# Task 3. TV controller.
class TVController:
    list_temp = []

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        print(self.channels[0])
        TVController.list_temp.append(self.channels[0])
        pass

    def last_channel(self):
        print(self.channels[-1])
        TVController.list_temp.append(self.channels[-1])
        pass

    def turn_channel(self, ind):
        print(self.channels[ind - 1])
        TVController.list_temp.append(self.channels[ind - 1])
        pass

    def next_channel(self):
        try:
            list_1 = []
            for i in self.channels:
                if i == TVController.list_temp[-1]:
                    current_ind = self.channels.index(i)
                    int(current_ind)
                    print(self.channels[current_ind + 1])
                    list_1.append(self.channels[current_ind + 1])
            TVController.list_temp.extend(list_1)
        except IndexError:
            print(self.channels[0])
            TVController.list_temp.append(self.channels[0])

    def previously_channel(self):
        for i in self.channels:
            if i == TVController.list_temp[-1]:
                current_ind = self.channels.index(i)
                int(current_ind)
                if current_ind == 0:
                    print(self.channels[0])
                    TVController.list_temp.append(self.channels[0])
                else:
                    print(self.channels[current_ind - 1])
                    TVController.list_temp.append(self.channels[current_ind - 1])

    def current_channel(self):
        # print(TVController.list_temp)
        print(TVController.list_temp.pop())
        # print(self.channels)

    def is_exit(self, arg_1):
        TVController.list_temp.clear()
        if arg_1 in self.channels:
            print("Yes")
        elif arg_1 in range(len(self.channels)+1):
            print("Yes")
        else:
            print("No")


Channels = ["BBC", "Discovery", "TV1000", "TV5", "TV"]
controller = TVController(Channels)

# controller.first_channel()
# controller.last_channel()
controller.turn_channel(4)
controller.next_channel()
controller.current_channel()
# controller.previously_channel()
# controller.current_channel()
# controller.is_exit('BBC')
