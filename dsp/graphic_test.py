import matplotlib.pyplot as plt, mpld3
fig = plt.figure()
plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)

mpld3.save_html(fig, 'interactive_fig.html')