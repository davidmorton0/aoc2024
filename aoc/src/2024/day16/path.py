class Path:
    def __init__(self, locations):
        self.locations = locations
        self.status = 'in_progress'

    def latest_location(self):
        return self.locations[-1]

    def add_to_path(self, location):
        self.locations.append(location)

    def path_length(self):
        return len(self.locations)

    def path_up_to(self, n):
        return self.locations[0:n]

    def is_collision(self, path):
        return self.locations[-1] in path.locations

    def is_in_path(self, location):
        return location in self.locations

    def find_in_path(self, location):
        return self.locations.index(location)

    def current_score(self):
        return self.calculate_score(self.locations)

    def calculate_score(self, path):
        if len(path) < 2:
            return 0
        previous_moving_direction = None
        score = 0
        for n, [x, y] in enumerate(path[1:]):
            prev_x, prev_y = path[n - 1]
            if x != prev_x:
                current_moving_direction = 'NS'
            else:
                current_moving_direction = 'EW'

            if previous_moving_direction and current_moving_direction != previous_moving_direction:
                score += 1001
            else:
                score += 1
            previous_moving_direction = current_moving_direction
        return score