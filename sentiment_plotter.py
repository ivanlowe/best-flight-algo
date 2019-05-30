import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def plotResults(p, n, s):
    objects = ("Positive Words", "Negative Words", "Stop words")
    y_pos = np.arange(len(objects))
    values = [p, n, s]

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel("Count")
    plt.title("Distribution of positive, negative and stop words")

    plt.savefig("static\\word_dist.png")