from random import randint
import matplotlib.pyplot as plt
def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    new_bins = bins[1:]
    new_bins.append(max(data)*2)
    
    counts = [0] * len(bins)
    for d in data:
        for i in range(len(bins)):
            if d >= bins[i] and d < new_bins[i]:
                counts[i] += 1
    return (data, bins, counts)


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    data, bins, counts = bins_count
    bin_labels = ["00"+str(bins[0])+"-"+"0"+str(bins[1])]
    bin_labels.extend(["0"+str(bins[i+1])+"-"+"0"+str(bins[i+2]) for i in range(len(bins)-3)])
    bin_labels.extend(["0"+str(bins[-2])+"-"+str(bins[-1])])
    bin_labels.append(str(bins[-1])+"+")
    
    ticks = [i for i in range(len(bins))]
    
    plt.bar(ticks, counts)
    plt.xticks(ticks, bin_labels)
    for i in range(len(ticks)):
        
        plt.annotate(str(counts[i]), xy=(ticks[i], counts[i]), ha='center', va='bottom')
        
    plt.title('Data Distribution')
    plt.xlabel('bins')
    plt.show()

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
