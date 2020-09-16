def autolabel(ax, rects, num = 0, percent = False):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        fmt = f'{height*100:.{num}f}%' if percent else f'{height:.{num}f}'
        ax.annotate(fmt,
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')