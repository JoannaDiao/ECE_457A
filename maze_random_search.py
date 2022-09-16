from random import randint
from random import seed
from datetime import datetime


class RandomSearch:
    def __init__(self, start_x, start_y, end_x_1, end_y_1, end_x_2, end_y_2, limit, maze) -> None:
        self.start_x_ = start_x
        self.start_y_ = start_y
        self.end_x_1_ = end_x_1
        self.end_y_1_ = end_y_1
        self.end_x_2_ = end_x_2
        self.end_y_2_ = end_y_2
        self.limit_ = limit
        self.moves_ = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.maze_ = maze

    def is_valid(self, x, y, prev_x, prev_y):
        if x < 0 or x >= len(self.maze_) or y < 0 or y >= len(self.maze_[0]) or (x == prev_x and y == prev_y) or self.maze_[x][y] == 1:
            return False
        return True

    def reached_goal(self, x, y):
        if (x == self.end_x_1_ and y == self.end_y_1_) or (x == self.end_x_2_ and y == self.end_y_2_):
            return True
        return False

    def random_search(self):
        x = self.start_x_
        y = self.start_y_
        prev_x = -1
        prev_y = -1
        move_count = 0
        while move_count <= self.limit_:
            print("x: ", x, " y: ", y)
            # Reached the goal state
            if self.reached_goal(x, y):
                print("Reached goal state")
                break

            cornered = True
            for move in self.moves_:
                next_x = x + move[0]
                next_y = y + move[1]
                if self.is_valid(next_x, next_y, prev_x, prev_y):
                    cornered = False
            if cornered:
                print("We have nowhere to go. x = ", x, " y = ", y)
                break

            now = datetime.now()
            seed(now)
            next_move = randint(0, 3)
            next_x = x + self.moves_[next_move][0]
            next_y = y + self.moves_[next_move][1]
            while not self.is_valid(next_x, next_y, prev_x, prev_y):
                next_move = randint(0, 3)
                next_x = x + self.moves_[next_move][0]
                next_y = y + self.moves_[next_move][1]

            prev_x = x
            prev_y = y
            x = next_x
            y = next_y
            move_count += 1

        print("final x: ", x, " final y: ", y)
        print("final cost: ", move_count)


if __name__ == "__main__":
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1,
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
            0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0,
            0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

    # limit = 1000: the agent was able to find the goal (3, 2) with a cost of 82
    # limit = 10k: the agent was stuck in a deadend at (22, 5) with a cost of 524. It did not find the exit.
    # limit = 100k:  the agent was able to find the goal (5, 23) with a cost of 105
    # limit = 1000k: the agent was able to find the goal (5, 23) with a cost of 699
    search = RandomSearch(13, 2, 5, 23, 3, 2, 1000000, maze)
    search.random_search()
