class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Get indices sorted by position in ascending order
        sorted_indices = sorted(range(len(position)), key=lambda i: position[i])
      
        # Initialize fleet count and previous car's time to target
        fleet_count = 0
        previous_time = 0
      
        # Process cars from closest to target (rightmost) to furthest
        for index in sorted_indices[::-1]:
            # Calculate time for current car to reach target
            time_to_target = (target - position[index]) / speed[index]
          
            # If current car takes longer than previous car, it forms a new fleet
           
            if time_to_target > previous_time:
                fleet_count += 1
                previous_time = time_to_target
      
        return fleet_count
