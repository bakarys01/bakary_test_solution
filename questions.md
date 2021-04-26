### Questions

#### Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to `histogram_example.png` as a minimum result.

#### Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns an _array_ of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

#### Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
`question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> _answer here_

--------------------------------------------------------------------
Running peer simulation with:
 - number_of_peers: 10
 - max_peer_pool_size: 2
Backend processing time: 0:00:00.000050

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.035098

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 100
Backend processing time: 0:00:00.524125

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 1000
Backend processing time: 0:00:01.168818

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.292423

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 100
Backend processing time: 0:00:03.023390
-------------------------------------------------------
By looking at the results we can see that the computing time needed to process the data inceases quickly with the number of peers and the size of the pools. This was to be expected because with $N$ peers and a maximum size of $M$ for the pools we can expect in average $NM/2$ data points (given that the pool sizes are equiprobable like here).

With millions of peers we can expect a processing time of several minutes. There's maybe a more clever way to compute the bins and prepare the histogram that can save a lot of time while keeping a good quality of representation.


#### Question 4

Go to the file `question4.py`:
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.
>> _answer here_

Running peer simulation with:
 - number_of_peers: 10
 - max_peer_pool_size: 2
Backend processing time: 0:00:00.000164

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.050223

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 100
Backend processing time: 0:00:00.248525

Running peer simulation with:
 - number_of_peers: 1000
 - max_peer_pool_size: 1000
Backend processing time: 0:00:00.855408

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 10
Backend processing time: 0:00:00.242478

Running peer simulation with:
 - number_of_peers: 10000
 - max_peer_pool_size: 100
Backend processing time: 0:00:02.269441

-----------------------------------------------------------------
The result is similar to the question2.


The original idea behind my solution was that we have a lot of precision on the data points that maybe isn't necessary. Let's assume, to simplify things, that the distribution we want to represent is fairly smooth (the extrem case being the uniform distribution). Thus the bin widths might be roughly the same (This is a big assumption). Then we can estimate the precision that is necessary.

