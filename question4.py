"""
    addition
"""
import random

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram
import json
class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: implement this method
        """
        return json.dumps(self.peer_pool)
        

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: implement this method
        """
        durations_ = random.sample(self.backend_database, int(self.number_of_peers/2))
        k = [i for j in durations_ for i in (json.loads(j).values())]
        data, bins, counts = compute_histogram_bins(k, BINS)
        
        return (data, bins, counts)

if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
