import matplotlib.pyplot as plt, mpld3
import numpy as np

def save_stem(p1, p2, name):
    fig = plt.figure()
    # plt.grid(True, color='w')
    plt.grid(color='#000000', linestyle='-', linewidth=0.2)
    plt.stem(np.arange(p1), p2)
    mpld3.save_html(fig, 'graphics/'+name)